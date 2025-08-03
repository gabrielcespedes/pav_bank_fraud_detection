from flask import Blueprint, request, send_file, render_template, flash, redirect, url_for, session
from app.utils.predict import hacer_predicciones
import os

from werkzeug.security import generate_password_hash, check_password_hash
from models import Usuario, db

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

# Asegura que las carpetas existan
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@main.route('/', methods = ['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        usuario_input = request.form.get('usuario')
        password_input = request.form.get('password')

        # Buscar usuario en la base de datos
        usuario_db = Usuario.query.filter_by(usuario = usuario_input).first()

        if usuario_db and check_password_hash(usuario_db.password, password_input):
            session["usuario"] = usuario_db.usuario # guarda en sesión
            flash(f"Bienvenido {usuario_db.nombre}")
            return redirect(url_for('main.prediccion'))  # Redirige a predicción
        else:
            flash("Credenciales incorrectas. Intenta nuevamente.")
            return redirect(url_for('main.inicio'))
    return render_template('index.html') # login visual

@main.route('/prediccion', methods=['GET', 'POST'])
def prediccion():
    if 'usuario' not in session:
        flash("Debes iniciar sesión para acceder.")
        return redirect(url_for('main.inicio'))
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

    return render_template('prediccion.html')

@main.route('/registro', methods = ["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        confirmar = request.form.get('confirmar')

        if not usuario or not password or not confirmar:
            flash("Por favor completa todos los campos.")
            return render_template("registro.html")

        if password != confirmar:
            flash("Las contraseñas no coinciden.")
            return render_template('registro.html')
        
        # Verificar si el usuario ya existe
        usuario_existente = Usuario.query.filter_by(usuario = usuario).first()
        correo_existente = Usuario.query.filter_by(correo = correo).first()

        if usuario_existente or correo_existente:
            flash("Ya existe un usuario con ese nombre o correo.")
            return render_template("registro.html")

        # Hashear contraseña
        hashed_password = generate_password_hash(password)

        # Crear usuario
        nuevo_usuario = Usuario(
            nombre = nombre,
            correo = correo,
            usuario = usuario,
            password = hashed_password
        )

        # Guardar en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash("Usuario registrado con éxito.")
        return redirect(url_for('main.inicio'))
    
    return render_template('registro.html')

@main.route('/logout')
def logout():
    session.pop('usuario', None)
    flash("Sesión cerrada correctamente.")
    return redirect(url_for('main.inicio'))