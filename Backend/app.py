from flask import Flask, request, jsonify, render_template
from models import db, Cliente, Habitacion, Hotel, Reserva
from flask_cors import CORS
from datetime import timedelta
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

port = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://fundamentalistas:fundamentalistas@localhost:5432/intro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def Hello_world():
    return 'Hola que tal'




@app.route('/registrar_cliente', methods=["POST"])
def registrar_cliente():

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['DNI']
    telefono = request.form['telefono']
    edad = request.form['edad']

    nuevo_cliente = Cliente(
        nombre=nombre,
        apellido=apellido,
        DNI=dni,
        telefono=telefono,
        edad=edad
    )

    db.session.add(nuevo_cliente)
    db.session.commit()

    return jsonify({'mensaje': 'Cliente registrado con éxito'})




@app.route('/clientes/', methods=["GET"])
def clientes():
    try:
        clientes = Cliente.query.all()
        clientes_data = []
        for cliente in clientes:
            cliente_data = {
                'nombre': cliente.nombre,
                'apellido': cliente.apellido,
                'DNI': cliente.DNI,
                'telefono': cliente.telefono,
                'cant_dias': cliente.cant_dias,
                'edad': cliente.edad
            }
            clientes_data.append(cliente_data)
        return jsonify(clientes_data)
    except:
        return jsonify({"mensaje": "No hay clientees"})
    
@app.route('/lista-clientes/', methods=["GET"])
def listaclientes():
    try:
        clientes = Cliente.query.all()
        clientes_data = []
        for cliente in clientes:
            cliente_data = {
                'id': cliente.id,
                'DNI': cliente.DNI,
                'apellido':cliente.apellido,
            }
            clientes_data.append(cliente_data)
        return jsonify(clientes_data)
    except Exception as e:
        return jsonify({"mensaje": str(e)})










@app.route('/hoteles/', methods=["GET"])
def get_hoteles():
    try:
        hoteles = Hotel.query.all()
        hoteles_data = []
        for hotel in hoteles:
            hotel_data = {
                'id': hotel.id,
                'nombre': hotel.nombre,
            }
            hoteles_data.append(hotel_data)
        return jsonify(hoteles_data)
    except Exception as e:
        return jsonify({"mensaje": str(e)})

@app.route('/habitaciones_disponibles/<int:hotel_id>', methods=["GET"])
def get_habitaciones_disponibles(hotel_id):
    try:
        habitaciones = Habitacion.query.filter_by(hotel_id=hotel_id, estado=False).all()
        habitaciones_data = []
        for habitacion in habitaciones:
            habitacion_data = {
                'id': habitacion.id,
                'numero': habitacion.numero,
                'cant_personas': habitacion.cant_personas,
                'service': habitacion.service
            }
            habitaciones_data.append(habitacion_data)
        return jsonify(habitaciones_data)
    except Exception as e:
        return jsonify({"mensaje": str(e)})

@app.route('/precio_habitacion/<int:habitacion_id>', methods=["GET"])
def get_precio_habitacion(habitacion_id):
    try:
        habitacion = Habitacion.query.filter_by(id=habitacion_id).first()
        if habitacion:
            habitacion_data = {
                'id': habitacion.id,
                'precio': habitacion.precio_dia
            }
            return jsonify(habitacion_data)
        else:
            return jsonify({"mensaje": "Habitación no encontrada"}), 404
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500





@app.route('/crear_reservas/', methods=["POST"])
def registrar_reservas():

    cliente_id = request.form['cliente']
    hotel_id = request.form['hotel']
    Habitacion_id = request.form['habitacion']
    cant_dias= int(request.form['cant_dias'])
    horario_ingreso = request.form['fecha_hora_ingreso']
    precio_habitacion=request.form['precio_habitacion']
    
    nueva_reserva = Reserva(
        cliente_id=cliente_id,
        hotel_id=hotel_id,
        Habitacion_id=Habitacion_id,
        cant_dias=cant_dias,
        horario_ingreso=horario_ingreso,
        horario_salida= horario_ingreso + timedelta(days=cant_dias) - timedelta(hours=4),
        precio=cant_dias * precio_habitacion,
        
    )

    db.session.add(nueva_reserva)
    db.session.commit()

    return jsonify({'mensaje': 'reserva con exito '})



if __name__ == '__main__':
    print('arrancando')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    print('arrancado ..')
    app.run(host='0.0.0.0', debug=True, port=port)