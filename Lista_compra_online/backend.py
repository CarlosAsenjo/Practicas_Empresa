from flask import Flask, escape, request, jsonify, render_template

import json

app=Flask(__name__)

@app.route('/')
def home():
#: Devuelve el fichero con la implementación de la lista de la compra
    with open('lista.html') as f:
        return f.read()

@app.route('/api/lista')
@app.route('/api/lista/<id>')
def lista_GET(id=None):
#: Abre y lee la base de datos
    with open('database.json') as f:
        database = json.loads(f.read())
    res=database
    if id:
        item =[x for x in database if x['id']==id]
        res =item[0] if item else None
#: Devuelve en formato JSON
    return jsonify(res)

@app.route('/api/lista', methods=['POST'])
def lista_POST():
#: Carga los datos pasados en la petición en formato JSON
    data=request.json
#: Lectura de la base de datos
    with open('database.json') as f:
        database= json.loads(f.read())
#: Crea un nuevo elemento, asigna un nuevo id
    res=dict(
        id=len(database),
        texto=data['texto'],
        comprado=False,
    )
#: Añade el elemento a la lista...
    database.append(res)
#: ... y escribe la base de datos en formato JSON
    with open('lista.json','w') as f:
        f.write(json.dumps(database))
    return jsonify(res)

@app.route('/api/lista/<id>',methods=['PUT'])
def lista_PUT(id):
     with open('database.json') as f:
        data = json.loads(f.read())
        res = data
        item = [x for x in data if x['id']==id]
        res = item[0] if item else None
        data.update(data)
        return jsonify(res)

@app.route('/api/lista/<id>', methods=['DELETE'])
def lista_DELETE(id):
    data = request.json
    data(id)
    return jsonify(id)

def main():
    app.run(host='0.0.0.0', debug=True)

if __name__=='__main__':
    main()