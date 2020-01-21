from flask import *
from db import models

class IndexController:
    def show():
        return render_template('index.html', title='hello py')

class ReadController:
    def read():
        print('read')
        user = models.User.find(1)
        print(user)
        return render_template('index.html', title='read done')
        
class WriteController:
    def create():
        print('create')
        #create record
        return render_template('index.html', title='create done')
        
    def update():
        print('update')
        #update record
        return render_template('index.html', title='update done')
        
    def delete():
        print('delete')
        #delete record
        return render_template('index.html', title='delete done')