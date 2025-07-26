from flask import Blueprint, request, send_file, render_template
from utils.predict import hacer_predicciones
import os

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

# Asegura que las carpetas existan
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Guardar archivo subido
            input_filename = file.filename
            input_path = os.path.join(UPLOAD_FOLDER, input_filename)
            file.save(input_path)

            # Realizar predicciones
            df_resultado = hacer_predicciones(input_path)

            # Determinar extensión del archivo original
            extension = os.path.splitext(input_filename)[1].lower()
            output_filename = f"predicciones_{input_filename}"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)

            # Guardar archivo con predicciones en el formato correcto
            if extension == ".csv":
                df_resultado.to_csv(output_path, index = False)
            elif extension in [".xlsx", ".xls"]:
                df_resultado.to_excel(output_path, index = False)           

            # Ofrecer archivo para descarga
            return send_file(output_path, as_attachment=True)

    return render_template('index.html')
