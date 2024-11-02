# views.py
from flask import Blueprint, request
from functions import *
from database import Database

# Creamos un blueprint llamado 'main'
employee = Blueprint('employee', __name__)

db = Database()

@employee.route('/employee')
def employee_list():
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM employee'
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'cellphone': row[3],
                'user': row[4],
                'password': row[5],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@employee.route('/employee/<int:employee_id>')
def employee_show(employee_id):
    result = []
    try:    
        #execuitng query
        cur = db.getCursor()
        query = 'SELECT * FROM employee where id = {}'.format(employee_id)
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            content = {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'cellphone': row[3],
                'user': row[4],
                'password': row[5],
            }
            result.append(content)
        db.commit()
        cur.close()
        return make_response({'message': 'OK', 'data': result}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@employee.route('/employee', methods=['POST'])
def employee_create():    
    try:    
        #getting data
        name = request.json['name']
        email = request.json['email']
        cellphone = request.json['cellphone']
        user = request.json['user']
        password = request.json['password']
        #execuitng query
        cur = db.getCursor()
        query = "INSERT INTO employee (name, email, cellphone, user, password) VALUES (%s);"
        val = (name, email, cellphone, user, password)
        cur.execute(query, val)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha agregado el empleado'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)

@employee.route('/employee', methods=['PUT'])
def employee_update():    
    try:    
        #getting data
        employee_id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        cellphone = request.json['cellphone']
        user = request.json['user']
        password = request.json['password']
        #execuitng query
        cur = db.getCursor()
        query = '''
        UPDATE employee
        set name = %s, email = %s, cellphone = %s, user = %s, password = %s
        where id = %s
        '''
        values = (name, email, cellphone, user, password, employee_id)
        cur.execute(query, values)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha actualizado el empleado'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
    
@employee.route('/employee/<int:employee_id>', methods=['DELETE'])
def employee_delete(employee_id):    
    try:    
        #execuitng query
        cur = db.getCursor()
        query = f'DELETE FROM employee WHERE id = {employee_id}'
        cur.execute(query)
        db.commit()
        cur.close()
        return make_response({'message': 'Se ha eliminado el empleado'}, 200)
    except Exception as e:
        return make_response({'message': f"Ha sucedido un error: {e}"}, 400)
