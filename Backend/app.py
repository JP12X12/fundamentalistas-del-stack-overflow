from flask import Flask, request, jsonify, render_template
from models import db, Cliente, Habitacion, Hotel, Reserva
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

port = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://fundamentalistas:fundamentalistas@localhost:5432/intro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def Hello_world():
    return 'Hola que tal'

@app.route('/hoteles/', methods=["GET"])
def hoteles():
    try:
        hoteles = Hotel.query.all()
        hoteles_data = []
        for hotel in hoteles:
            hotel_data = {
                'id': hotel.id,
                'nombre': hotel.nombre,
                'estrellas': hotel.estrellas,
                'pisos': hotel.pisos
            }
            hoteles_data.append(hotel_data)
        return jsonify(hoteles_data)
    except:
        return jsonify({"mensaje": "No hay hoteles"})



@app.route('/registrar_cliente', methods=['POST'])
def registrar_cliente():
    print(request.form['nombre'])
    print(request.form['apellido'])
    print(request.form['DNI'])
    print(request.form['telefono'])
    print(request.form['cant_dias'])
    print(request.form['edad'])
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


@app.route('/ver_clientes', methods=['GET'])
def ver_clientes():
    clientes = Cliente.query.all()
    clientes_lista = [
        {
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'DNI': cliente.DNI,
            'telefono': cliente.telefono,
            'cant_dias': cliente.cant_dias,
            'edad': cliente.edad
        } for cliente in clientes
    ]
    return jsonify(clientes_lista)


if __name__ == '__main__':
    print('arrancando')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    print('arrancado ..')
    app.run(host='0.0.0.0', debug=True, port=port)
