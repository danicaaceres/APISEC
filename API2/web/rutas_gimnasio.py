from flask import request, session
import json
import decimal
from __main__ import app
import controlador_gimnasio
import utilidades

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)

@app.route("/gimnasio", methods=["GET"])
def gimnasio():
    gimnasio, code = controlador_gimnasio.obtener_gimnasio()
    return json.dumps(gimnasio, cls=Encoder), code

@app.route("/gimnasio/<id>", methods=["GET"])
def gimnasio_por_id(id):
    id = utilidades.sanitize_input(id)
    gimnasio, code = controlador_gimnasio.obtener_gimnasio_por_id(id)
    return json.dumps(gimnasio, cls=Encoder), code

@app.route("/gimnasio", methods=["POST"])
def guardar_gimnasio():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        gimnasio_json = request.json
        nombre = utilidades.sanitize_input(gimnasio_json["nombre"])
        descripcion = utilidades.sanitize_input(gimnasio_json["descripcion"])
        precio = float(utilidades.sanitize_input(gimnasio_json["precio"]))
        foto = utilidades.sanitize_input(gimnasio_json["foto"])
        ret, code = controlador_gimnasio.insertar_gimnasio(nombre, descripcion, precio, foto)
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

@app.route("/gimnasio/<id>", methods=["DELETE"])
def eliminar_gimnasio(id):
    id = utilidades.sanitize_input(id)
    ret, code = controlador_gimnasio.eliminar_gimnasio(id)
    return json.dumps(ret), code

@app.route("/gimnasio", methods=["PUT"])
def actualizar_gimnasio():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        gimnasio_json = request.json
        id = utilidades.sanitize_input(gimnasio_json["id"])
        nombre = utilidades.sanitize_input(gimnasio_json["nombre"])
        descripcion = utilidades.sanitize_input(gimnasio_json["descripcion"])
        precio = float(utilidades.sanitize_input(gimnasio_json["precio"]))
        foto = utilidades.sanitize_input(gimnasio_json["foto"])
        ret, code = controlador_gimnasio.actualizar_gimnasio(id, nombre, descripcion, precio, foto)
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code