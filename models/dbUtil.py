import configparser
import psycopg2
from flask_sqlalchemy import SQLAlchemy

class connection:
  def getConnection():
    config = configparser.ConfigParser()
    config.read('settings.conf')

    db_host = config.get('database', 'host')
    db_port = config.get('database', 'port')
    db_name = config.get('database', 'name')
    db_user = config.get('database', 'user')
    db_pass = config.get('database', 'pass')
    
    connection = psycopg2.connect("host=%s port=%s dbname=%s user=%s password=%s" % (db_host,db_port,db_name,db_user,db_pass))
    cur = connection.cursor()
    
    
    print(db_host)