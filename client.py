# views.py
from flask import Blueprint, request
from functions import *
from database import Database

# Creamos un blueprint llamado 'main'
client = Blueprint('client', __name__)

db = Database()

@client.route('/client')
def client_list():
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM client'
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0], 
                'name': row[1], 
                'email': row[2],
                'cellphone': row[3],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@client.route('/client/<int:client_id>')
def client_show(client_id):
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM client where id = {}'.format(client_id)
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0], 
                'name': row[1], 
                'email': row[2],
                'cellphone': row[3],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@client.route('/client', methods=['POST'])
def client_create():    
    try:    
        #getting data
        name = request.json['name']
        email = request.json['email']
        cellphone = request.json['cellphone']
        #execuitng query
        cur = db.getCursor()
        query = "INSERT INTO client (name, email, cellphone) VALUES (%s, %s, %s);"
        val = (name, email, cellphone)
        cur.execute(query, val)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha agregado el cliente'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@client.route('/client', methods=['PUT'])
def client_update():    
    try:    
        #getting data
        client_id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        cellphone = request.json['cellphone']
        #execuitng query
        cur = db.getCursor()
        query = '''
        UPDATE client
        set name = %s, email = %s, cellphone = %s
        where id = %s
        '''
        values = (name, email, cellphone, client_id)
        cur.execute(query, values)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha actualizado el cliente'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@client.route('/client/<int:client_id>', methods=['DELETE'])
def client_delete(client_id):    
    try:    
        #execuitng query
        cur = db.getCursor()
        query = f'DELETE FROM client WHERE id = {client_id}'
        cur.execute(query)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha eliminado el cliente'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
