from flask import Flask, request, jsonify, render_template
from models import db, Cliente, Habitacion, Hotel, Reserva
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://fundamentalistas:fundamentalistas@localhost:5432/intro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def Hello_world():
    return 'Hola que tal'

if __name__ == '__main__':
    print('arrancando')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    print('arrancado ..')
    app.run(host='0.0.0.0', debug=True, port=port)


@app.route('/registrar_cliente', methods=['POST'])
def registrar_cliente():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['DNI']
    telefono = request.form['telefono']
    cant_dias = request.form['cant_dias']
    edad = request.form['edad']

    nuevo_cliente = Cliente(
        nombre=nombre,
        apellido=apellido,
        DNI=dni,
        telefono=telefono,
        cant_dias=cant_dias,
        edad=edad
    )

    db.session.add(nuevo_cliente)
    db.session.commit()

    return jsonify({'mensaje': 'Cliente registrado con éxito'})