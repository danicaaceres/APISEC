from __future__ import print_function
from __main__ import app
from flask import request
import os
import sys
import json
import subprocess
import utilidades

@app.route('/ver/<archivo>', methods=['GET']) 
def ver(archivo):
    try:
        sanitized_filename = utilidades.sanitize_input(archivo)
        basepath = os.path.dirname(__file__)  # ruta del archivo actual
        upload_path = os.path.join(basepath, 'static', sanitized_filename)

        if not os.path.exists(upload_path):
            return json.dumps({"status": "ERROR", "mensaje": "El archivo no existe"}), 404

        with open(upload_path, "r", encoding="utf-8") as file:
            salida = file.read()

        return json.dumps({"status": "OK", "contenido": salida}), 200
    except Exception as e:
        print("Error al leer archivo:", e, file=sys.stderr)
        return json.dumps({"status": "ERROR"}), 500