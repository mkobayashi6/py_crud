from datetime import datetime
from db import db_util

class User:
    __tablename__ = 'users'
    
    def find(id):
        cursol = db_util.Connection.getConnection()
        print(cursol)
        
        return None