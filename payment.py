# views.py
from flask import Blueprint, request
from functions import *
from database import Database

# Creamos un blueprint llamado 'main'
payment = Blueprint('payment', __name__)

db = Database()

@payment.route('/payment')
def payment_list():
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM payment'
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0],
                'id_employee': row[1],
                'id_rent': row[2],
                'id_method': row[3],
                'payment_date': row[4],
                'amount': row[5],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@payment.route('/payment/<int:payment_id>')
def payment_show(payment_id):
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM payment where id = {}'.format(payment_id)
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0],
                'id_employee': row[1],
                'id_rent': row[2],
                'id_method': row[3],
                'payment_date': row[4],
                'amount': row[5],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@payment.route('/payment', methods=['POST'])
def payment_create():    
    try:    
        #getting data
        id_employee = request.json['id_employee']
        id_rent = request.json['id_rent']
        id_method = request.json['id_method']
        payment_date = request.json['payment_date']
        amount = request.json['amount']
        #execuitng query
        cur = db.getCursor()
        query = "INSERT INTO payment (id_employee, id_rent, id_method, payment_date, amount) VALUES (%s);"
        val = (id_employee, id_rent, id_method, payment_date, amount)
        cur.execute(query, val)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha agregado el pago'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@payment.route('/payment', methods=['PUT'])
def payment_update():    
    try:    
        #getting data
        payment_id = request.json['id']
        id_employee = request.json['id_employee']
        id_rent = request.json['id_rent']
        id_method = request.json['id_method']
        payment_date = request.json['payment_date']
        amount = request.json['amount']
        #execuitng query
        cur = db.getCursor()
        query = '''
        UPDATE payment
        set id_employee = %s, id_rent = %s, id_method = %s, payment_date = %s, amount = %s
        where id = %s
        '''
        values = (id_employee, id_rent, id_method, payment_date, amount, payment_id)
        cur.execute(query, values)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha actualizado el pago'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@payment.route('/payment/<int:payment_id>', methods=['DELETE'])
def payment_delete(payment_id):    
    try:    
        #execuitng query
        cur = db.getCursor()
        query = f'DELETE FROM payment WHERE id = {payment_id}'
        cur.execute(query)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha eliminado el pago'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
