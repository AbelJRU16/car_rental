# views.py
from flask import Blueprint, request
from functions import *
from database import Database

# Creamos un blueprint llamado 'main'
vehicle = Blueprint('vehicle', __name__)

db = Database()

@vehicle.route('/vehicle')
def vehicle_list():
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM vehicle'
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id' : row[0],
                'plate' : row[1],
                'id_brand' : row[2],
                'id_status' : row[3],
                'id_type' : row[4],
                'description' : row[5],
                'long_description' : row[6],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@vehicle.route('/vehicle/<int:vehicle_id>')
def vehicle_show(vehicle_id):
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM vehicle where id = {}'.format(vehicle_id)
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id' : row[0],
                'plate' : row[1],
                'id_brand' : row[2],
                'id_status' : row[3],
                'id_type' : row[4],
                'description' : row[5],
                'long_description' : row[6],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@vehicle.route('/vehicle', methods=['POST'])
def vehicle_create():    
    try:    
        #getting data
        plate = request.json['plate']
        id_brand = request.json['id_brand']
        id_status = request.json['id_status']
        id_type = request.json['id_type']
        description = request.json['description']
        long_description = request.json['long_description']
        #execuitng query
        cur = db.getCursor()
        query = '''INSERT INTO vehicle 
        (plate, id_brand, id_status, id_type, description, long_description) 
        VALUES (%s, %s, %s, %s, %s, %s);'''
        val = (plate, id_brand, id_status, id_type, description, long_description)
        cur.execute(query, val)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha agregado el vehiculo'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@vehicle.route('/vehicle', methods=['PUT'])
def vehicle_update():    
    try:    
        #getting data
        vehicle_id = request.json['id']
        plate = request.json['plate']
        id_brand = request.json['id_brand']
        id_status = request.json['id_status']
        id_type = request.json['id_type']
        description = request.json['description']
        long_description = request.json['long_description']
        #execuitng query
        cur = db.getCursor()
        query = '''
        UPDATE vehicle
        set plate = %s, id_brand = %s, id_status = %s, id_type = %s, description = %s, long_description = %s
        where id = %s
        '''
        values = (plate, id_brand, id_status, id_type, description, long_description, vehicle_id)
        cur.execute(query, values)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha actualizado el vehiculo'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@vehicle.route('/vehicle/<int:vehicle_id>', methods=['DELETE'])
def vehicle_delete(vehicle_id):    
    try:    
        #execuitng query
        cur = db.getCursor()
        query = f'DELETE FROM vehicle WHERE id = {vehicle_id}'
        cur.execute(query)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha eliminado el vehiculo'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
