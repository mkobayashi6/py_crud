from datetime import datetime
from db import db_util
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def find(id):
        engine = db_util.Connection.getEngine()
        # todo: use ORM instead of sql
        result = engine.execute("select * from users where id = %s" % (id))
        
        return result
    
    def all():
        # todo: dont repeat engine def
        engine = db_util.Connection.getEngine()
        
        result = engine.execute("select * from users order by id")
        
        return result
        
    def create(form):
        engine = db_util.Connection.getEngine()
        result = engine.execute("insert into users (name, email, password, hint, pass_default, administrator) values ('%s', '%s', crypt('%s', gen_salt('md5')), '%s', false, true)"
         % (form['name'], form['email'], form['password'], form['hint']))
        return result
    
    def update(id, name):
        # todo: dont repeat engine def
        engine = db_util.Connection.getEngine()
        
        result = engine.execute("update users set name = \'%s\' where id = %s" % (name, id))
        
        return result