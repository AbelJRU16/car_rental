# views.py
from flask import Blueprint, request
from functions import *
from database import Database

# Creamos un blueprint llamado 'main'
brand = Blueprint('brand', __name__)

db = Database()

@brand.route('/brand')
def brand_list():
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM brand'
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
    
@brand.route('/brand/<int:brand_id>')
def brand_show(brand_id):
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM brand where id = {}'.format(brand_id)
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

@brand.route('/brand', methods=['POST'])
def brand_create():    
    try:    
        #getting data
        name = request.json['name']
        #execuitng query
        cur = db.getCursor()
        query = "INSERT INTO brand (name) VALUES (%s);"
        val = (name,)
        cur.execute(query, val)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha agregado la marca'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@brand.route('/brand', methods=['PUT'])
def brand_update():    
    try:    
        #getting data
        brand_id = request.json['id']
        name = request.json['name']
        #execuitng query
        cur = db.getCursor()
        query = '''
        UPDATE brand
        set name = %s
        where id = %s
        '''
        values = (name, brand_id)
        cur.execute(query, values)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha actualizado la marca'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@brand.route('/brand/<int:brand_id>', methods=['DELETE'])
def brand_delete(brand_id):    
    try:    
        #execuitng query
        cur = db.getCursor()
        query = f'DELETE FROM brand WHERE id = {brand_id}'
        cur.execute(query)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha eliminado la marca'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
