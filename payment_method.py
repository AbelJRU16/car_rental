# views.py
from flask import Blueprint, request
from functions import *
from database import Database

# Creamos un blueprint llamado 'main'
payment_method = Blueprint('payment_method', __name__)

db = Database()

@payment_method.route('/payment_method')
def payment_method_list():
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM payment_method'
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
    
@payment_method.route('/payment_method/<int:payment_method_id>')
def payment_method_show(payment_method_id):
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM payment_method where id = {}'.format(payment_method_id)
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0], 
                'description': row[1], 
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@payment_method.route('/payment_method', methods=['POST'])
def payment_method_create():    
    try:    
        #getting data
        description = request.json['description']
        #execuitng query
        cur = db.getCursor()
        query = "INSERT INTO payment_method (description) VALUES (%s);"
        val = (description,)
        cur.execute(query, val)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha agregado el metodo de pago'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@payment_method.route('/payment_method', methods=['PUT'])
def payment_method_update():    
    try:    
        #getting data
        payment_method_id = request.json['id']
        description = request.json['description']
        #execuitng query
        cur = db.getCursor()
        query = '''
        UPDATE payment_method
        set description = %s
        where id = %s
        '''
        values = (description, payment_method_id)
        cur.execute(query, values)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha actualizado el metodo de pago'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@payment_method.route('/payment_method/<int:payment_method_id>', methods=['DELETE'])
def payment_method_delete(payment_method_id):    
    try:    
        #execuitng query
        cur = db.getCursor()
        query = f'DELETE FROM payment_method WHERE id = {payment_method_id}'
        cur.execute(query)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha eliminado el metodo de pago'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
