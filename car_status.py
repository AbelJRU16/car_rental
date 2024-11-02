# views.py
from flask import Blueprint, request
from functions import *
from database import Database

# Creamos un blueprint llamado 'main'
car_status = Blueprint('car_status', __name__)

db = Database()

@car_status.route('/car_status')
def car_status_list():
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM car_status'
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0], 
                'name': row[1], 
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@car_status.route('/car_status/<int:car_status_id>')
def car_status_show(car_status_id):
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM car_status where id = {}'.format(car_status_id)
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0], 
                'name': row[1], 
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@car_status.route('/car_status', methods=['POST'])
def car_status_create():    
    try:    
        #getting data
        name = request.json['name']
        #execuitng query
        cur = db.getCursor()
        query = "INSERT INTO car_status (name) VALUES (%s);"
        val = (name,)
        cur.execute(query, val)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha agregado el estado'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@car_status.route('/car_status', methods=['PUT'])
def car_status_update():    
    try:    
        #getting data
        car_status_id = request.json['id']
        name = request.json['name']
        #execuitng query
        cur = db.getCursor()
        query = '''
        UPDATE car_status
        set name = %s
        where id = %s
        '''
        values = (name, car_status_id)
        cur.execute(query, values)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha actualizado el estado'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@car_status.route('/car_status/<int:car_status_id>', methods=['DELETE'])
def car_status_delete(car_status_id):    
    try:    
        #execuitng query
        cur = db.getCursor()
        query = f'DELETE FROM car_status WHERE id = {car_status_id}'
        cur.execute(query)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha eliminado el estado'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
