from flask import Flask, escape, request
app = Flask(__name__)
@app.route('/')

def hello():
    nombre = request.args.get("nombre", "Mundo")
    return 'Hola, {nombre}'.format(nombre=escape(nombre))

@app.route('/despedida')

def despedida(name="Carlos"):
    return 'Hasta la proxima, ' + name

def main():
 app.run(host='0.0.0.0', debug=True)
if __name__ == '__main__':
 main()