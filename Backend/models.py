import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    DNI = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    edad = db.Column(db.Integer, nullable=False)

class Hotel(db.Model):
    __tablename__ = 'hoteles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    estrellas = db.Column(db.Integer, nullable=False)
    pisos = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(100), nullable=False)
    habitaciones = db.relationship("Habitacion")

class Habitacion(db.Model):
    __tablename__ = 'habitaciones'
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hoteles.id'))
    numero = db.Column(db.Integer, nullable=False)
    cant_personas = db.Column(db.Integer, nullable=False)
    service = db.Column(db.String(15), nullable=False)
    precio_dia = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Boolean, default=False)

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hoteles.id'))
    habitacion_id = db.Column(db.Integer, db.ForeignKey('habitaciones.id'))
    cant_dias = db.Column(db.Integer, nullable=False)
    horario_ingreso = db.Column(db.DateTime, nullable=False)
    horario_salida = db.Column(db.DateTime, nullable=False)
    precio = db.Column(db.Integer, nullable=False)

