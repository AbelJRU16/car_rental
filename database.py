import mysql.connector as mysql

class Database():
    db = None
    
    def __init__(self):
        self.db = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="car_rental"
        )
    
    def getCursor(self):
        return self.db.cursor()
    
    def commit(self):
        self.db.commit()