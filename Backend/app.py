from flask import Flask, request, jsonify
from models import db, Cliente, Habitacion, Hotel, Reserva

app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://fundamentalistas:fundamentalistas@localhost:5432/intro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def hello_world():
    return 'Hola mundo!'

if __name__ == '__main__':
    print('arrancando')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    print('arrancado ..')
    app.run(host='0.0.0.0', debug=True, port=port)



