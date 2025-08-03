import joblib
import pandas as pd
import os

from app.ml.config_vars import categoricas

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../ml/modelo_bank.joblib')
COLUMNAS_PATH = os.path.join(BASE_DIR, '../ml/columnas_entrenamiento.joblib')

print("RUTA DEL MODELO:", MODEL_PATH)

modelo = joblib.load(os.path.abspath(MODEL_PATH))
columnas_entrenamiento = joblib.load(os.path.abspath(COLUMNAS_PATH))

def hacer_predicciones(filepath):

    extension = os.path.splitext(filepath)[1].lower()

    if extension == ".csv":
        df = pd.read_csv(filepath)
        output_format = "csv"
    elif extension in [".xlsx", ".xls"]:
        df = pd.read_excel(filepath)
        output_format = "xlsx"
    else:
        raise ValueError("Formato no soportado. Usa un archivo .csv o .xlsx")
    
    # preprocesamiento adicional
    df_codificado = pd.get_dummies(df, columns = categoricas, drop_first = False).astype(float)

    for col in columnas_entrenamiento:
        if col not in df_codificado.columns:
            df_codificado[col] = 0.0

    df_codificado = df_codificado[columnas_entrenamiento]

    predicciones = modelo.predict(df_codificado)
    df["prediccion"] = predicciones

    # Guardar archivo de salida en el mismo formato que la entrada
    output_path = filepath.replace(extension, f"_prediccion{extension}")
    if output_format == "csv":
        df.to_csv(output_path, index = False)
    elif output_format == "xlsx":
        df.to_excel(output_path, index = False)

    return df