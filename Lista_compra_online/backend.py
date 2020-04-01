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
    with open('database.json','w') as f:
        f.write(json.dumps(database))
    return jsonify(res)

@app.route('/api/lista/<int:id>',methods=['PUT'])
def lista_PUT(id):
    data = request.json
    with open('database.json') as f:
        db = json.loads(f.read())
    item =[x for x in db if x['id']==id]
    res=item[0]
    res.update(data)

    with open('database.json','w') as f:
        f.write(json.dumps(db))
    return jsonify(res)

@app.route('/api/lista/<int:id>', methods=['DELETE'])
def lista_DELETE(id):
    data = request.json
    with open('database.json') as f:
        db = json.loads(f.read())
    
        for ix, item in enumerate(db):
            if item['id']==id:
                break
        del(db[ix])

        for ix, item in enumerate(db):
            item['id']==ix
    
    with open('database.json','w') as f:
        f.write(json.dumps(db))
    return jsonify(id)

def main():
    app.run(host='0.0.0.0', debug=True)

if __name__=='__main__':
    main()