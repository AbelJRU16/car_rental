# views.py
from flask import Blueprint, request
from functions import *
from database import Database

# Creamos un blueprint llamado 'main'
car_type = Blueprint('car_type', __name__)

db = Database()

@car_type.route('/car_type')
def car_type_list():
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM car_type'
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0], 
                'description': row[1],
                'long_description': row[2],
                'rent_cost': float(row[3]),
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@car_type.route('/car_type/<int:car_type_id>')
def car_type_show(car_type_id):
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM car_type where id = {}'.format(car_type_id)
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0], 
                'description': row[1],
                'long_description': row[2],
                'rent_cost': float(row[3]),
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@car_type.route('/car_type', methods=['POST'])
def car_type_create():    
    try:    
        #getting data
        description = request.json['description']
        long_description = request.json['long_description']
        rent_cost = request.json['rent_cost']
        #execuitng query
        cur = db.getCursor()
        query = "INSERT INTO car_type (description, long_description, rent_cost) VALUES (%s, %s, %s);"
        val = (description, long_description, rent_cost)
        cur.execute(query, val)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha agregado el tipo de auto'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@car_type.route('/car_type', methods=['PUT'])
def car_type_update():    
    try:    
        #getting data
        car_type_id = request.json['id']
        description = request.json['description']
        long_description = request.json['long_description']
        rent_cost = request.json['rent_cost']
        #execuitng query
        cur = db.getCursor()
        query = '''
        UPDATE car_type
        set description = %s, long_description = %s, rent_cost = %s
        where id = %s
        '''
        values = (description, long_description, rent_cost, car_type_id)
        cur.execute(query, values)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha actualizado el tipo de auto'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@car_type.route('/car_type/<int:car_type_id>', methods=['DELETE'])
def car_type_delete(car_type_id):    
    try:    
        #execuitng query
        cur = db.getCursor()
        query = f'DELETE FROM car_type WHERE id = {car_type_id}'
        cur.execute(query)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha eliminado el tipo de auto'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
