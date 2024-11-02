# views.py
from flask import Blueprint, request
from functions import *
from database import Database

# Creamos un blueprint llamado 'main'
rent = Blueprint('rent', __name__)

db = Database()

@rent.route('/rent')
def rent_list():
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM rent'
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0], 
                'name': row[1],
                'id_employee': row[2],
                'id_client': row[3],
                'id_vehicle': row[4],
                'start_date': row[5],
                'end_date': row[6],
                'delivery_date': row[7],
                'cost': row[8],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@rent.route('/rent/<int:rent_id>')
def rent_show(rent_id):
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM rent where id = {}'.format(rent_id)
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0], 
                'name': row[1],
                'id_employee': row[2],
                'id_client': row[3],
                'id_vehicle': row[4],
                'start_date': row[5],
                'end_date': row[6],
                'delivery_date': row[7],
                'cost': row[8],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@rent.route('/rent', methods=['POST'])
def rent_create():    
    try:    
        #getting data
        name = request.json['name']
        id_employee = request.json['id_employee']
        id_client = request.json['id_client']
        id_vehicle = request.json['id_vehicle']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        delivery_date = request.json['delivery_date']
        cost = request.json['cost']
        #execuitng query
        cur = db.getCursor()
        query = '''INSERT INTO rent 
        (name, id_employee, id_client, id_vehicle, start_date, end_date, delivery_date, cost) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
        val = (name, id_employee, id_client, id_vehicle, start_date, end_date, delivery_date, cost)
        cur.execute(query, val)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha agregado el alquiler'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@rent.route('/rent', methods=['PUT'])
def rent_update():    
    try:    
        #getting data
        rent_id = request.json['id']
        name = request.json['name']
        id_employee = request.json['id_employee']
        id_client = request.json['id_client']
        id_vehicle = request.json['id_vehicle']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        delivery_date = request.json['delivery_date']
        cost = request.json['cost']
        #execuitng query
        cur = db.getCursor()
        query = '''
        UPDATE rent
        set name = %s, id_employee = %s, id_client = %s, id_vehicle = %s,
        start_date = %s, end_date = %s, delivery_date = %s, cost = %s
        where id = %s
        '''
        values = (name, id_employee, id_client, id_vehicle, start_date, end_date, delivery_date, cost, rent_id)
        cur.execute(query, values)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha actualizado el alquiler'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@rent.route('/rent/<int:rent_id>', methods=['DELETE'])
def rent_delete(rent_id):    
    try:    
        #execuitng query
        cur = db.getCursor()
        query = f'DELETE FROM rent WHERE id = {rent_id}'
        cur.execute(query)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha eliminado el alquiler'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
