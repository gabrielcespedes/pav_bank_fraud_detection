# extract.py
import boto3
import pandas as pd
from io import StringIO
import config
import os

def extract_multiple_from_s3(save_local: bool = True) -> dict:
    print("Iniciando conexión con S3...")

    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=config.AWS_ACCESS_KEY,
            aws_secret_access_key=config.AWS_SECRET_KEY,
            region_name=config.AWS_REGION
        )

        # Probar conexión y existencia del bucket
        response = s3.list_objects_v2(Bucket=config.S3_BUCKET)
        print("Conexión con S3 exitosa. Archivos disponibles:")
        if "Contents" in response:
            for obj in response["Contents"]:
                print(f"   - {obj['Key']}")
        else:
            print("No se encontraron archivos en el bucket.")
    except Exception as e:
        print(f"Error al conectar con el bucket: {e}")
        return {}

    filenames = config.S3_SOURCE_KEYS
    datasets = {}

    # Directorio de guardado
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    for filename in filenames:
        local_filename = filename.replace(" ", "_")
        full_path = os.path.join(data_dir, local_filename)

        print(f"Procesando archivo: {filename}")

        if os.path.exists(full_path):
            print(f"Ya existe localmente: {local_filename}, se omite descarga.")
            df = pd.read_csv(full_path)
        else:
            try:
                obj = s3.get_object(Bucket=config.S3_BUCKET, Key=filename)
                data = obj['Body'].read().decode('utf-8')
                df = pd.read_csv(StringIO(data))
                print(f"Descargado desde S3: {filename}")

                if save_local:
                    df.to_csv(full_path, index=False)
                    print(f"Guardado en local como: {local_filename}")
            except Exception as e:
                print(f"Error al descargar {filename}: {e}")
                continue

        datasets[filename] = df

    print("Proceso finalizado.")
    return datasets

# Solo ejecuta si se corre directamente
if __name__ == "__main__":
    print("Ejecutando extract.py")
    extract_multiple_from_s3()
