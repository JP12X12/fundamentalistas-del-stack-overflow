from flask import Flask, request, jsonify, render_template
from models import db, Cliente, Habitacion, Hotel, Reserva
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://fundamentalistas:fundamentalistas@localhost:5432/intro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def Home():
    return 'Hola que tal'

if __name__ == '__main__':
    print('arrancando')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    print('arrancado ..')
    app.run(host='0.0.0.0', debug=True, port=port)



