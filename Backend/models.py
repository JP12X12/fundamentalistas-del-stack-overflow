import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.column(db.integer, primary_key=True)
    nombre = db.column(db.string(50), nullable=False)
    apellido = db.column(db.string(50), nullable=False)
    DNI = db.column(db.integer, nullable=False)
    telefono = db.column(db.integer, nullable=False)
    cant_dias = db.column(db.integer, nullable=False)
    edad = db.column(db.integer, nullable=False)

class Hotel(db.Model):
    __tablename__ = 'hoteles'
    id = db.column(db.integer, primary_key=True)
    nombre = db.column(db.string(50), nullable=False)
    estrellas = db.column(db.integer, nullable=False)
    pisos = db.column(db.integer, nullable=False)
    ubicacion = db.column(db.string(100), nullable=False)

class Habitacion(db.Model):
    __tablename__ = 'habitaciones'
    id = db.column(db.integer, primary_key=True)
    hotel_id = db.column(db.integer, db.foreignkey('hoteles.id'))
    numero = db.column(db.integer, nullable=False)
    cant_personas = db.column(db.integer, nullable=False)
    service = db.column(db.string(15), nullable=False)
    precio_dia = db.column(db.integer, nullable=False)
    estado = db.column(db.string(50), nullable=False)

class reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.column(db.integer, primary_key=True)
    cliente_id = db.column(db.integer, db.foreignkey('clientes.id'))
    hotel_id = db.column(db.integer, db.foreignkey('hoteles.id'))
    habitacion_id = db.column(db.integer, db.foreignkey('habitaciones.id'))
    horario_ingreso = db.column(db.Datetime, nullable=False)
    horario_salida = db.column(db.Datetime, nullable=False)
    precio = db.column(db.integer, nullable=False)