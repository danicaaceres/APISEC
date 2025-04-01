from __future__ import print_function
from __main__ import app
from flask import request
import os
import json
import sys
import utilidades

@app.route('/upload', methods=['POST']) 
def upload():
    try:
        if 'fichero' not in request.files:
            return json.dumps({"status": "ERROR", "mensaje": "No se ha enviado ningún fichero"}), 400

        f = request.files['fichero']
        user_input = request.form.get("nombre")
        
        if not user_input:
            return json.dumps({"status": "ERROR", "mensaje": "Nombre no proporcionado"}), 400

        sanitized_name = utilidades.sanitize_input(user_input)
        basepath = os.path.dirname(__file__)  # ruta del archivo actual
        upload_path = os.path.join(basepath, 'static', sanitized_name)

        print('Lugar: ' + upload_path, file=sys.stdout)
        f.save(upload_path)

        return json.dumps({"status": "OK"}), 200
    except Exception as e:
        print("Error al subir archivo:", e, file=sys.stderr)
        return json.dumps({"status": "ERROR"}), 500