from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from functions import *
from brand import brand
from car_status import car_status
from payment_method import payment_method
from car_type import car_type
from vehicle import vehicle
from client import client
from employee import employee
from rent import rent

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'car_rental'
# mysql = MySQL(app)

app.register_blueprint(brand)
app.register_blueprint(car_status)
app.register_blueprint(payment_method)
app.register_blueprint(car_type)
app.register_blueprint(vehicle)
app.register_blueprint(client)
app.register_blueprint(employee)
app.register_blueprint(rent)

@app.route('/')
def index():
    return make_response({'message': 'Hello World'}, 200)

if __name__ == '__main__':
    app.run(None, 3000, True)