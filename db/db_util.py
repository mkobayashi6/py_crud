import configparser
from sqlalchemy import create_engine

class Connection:
  def getEngine():
    config = configparser.ConfigParser()
    config.read('settings.conf')

    db_host = config.get('database', 'host')
    db_port = config.get('database', 'port')
    db_name = config.get('database', 'name')
    db_user = config.get('database', 'user')
    db_pass = config.get('database', 'pass')
    
    db_declare = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (db_user,db_pass,db_host,db_port,db_name)
    engine = create_engine(db_declare, echo=True)
    
    return engine