from flask import *
from db import models

class IndexController:
    def show():
        return render_template('index.haml', title='hello py')

class ReadController:
    def read(request):
        users = []
        if request.method == 'POST':
            print('read')
            result = models.User.find(request.form['id'])
        else:
            result = models.User.all()
        for row in result:
            print(row.name)
            users.append((row.id, row.name))
        return render_template('read.haml', title='read done', list = users)
        
class WriteController:
    def create():
        print('create')
        
        return render_template('create.haml', title='create show')
        
    def new(form):
        print('new')
        #TODO: validation
        if models.User.create(form):
            print("succeed")
        else:
            print("failed")
        return render_template('index.haml', title='create done')
        
    def update(request):
        if request.method == 'POST':
            print('update')
            #update record
            # todo: add varidate
            models.User.update(request.form['id'], request.form['name'])
            # todo: not repeat user select
            users = []
            result = models.User.all()
            for row in result:
                print(row.name)
                users.append((row.id, row.name))
            return render_template('read.haml', title='update done', list = users)
        else:
            # todo: not repeat user select
            users = []
            result = models.User.all()
            for row in result:
                print(row.name)
                users.append((row.id, row.name))
            return render_template('read.haml', title='read done', list = users)
        
    def delete(request):
        if request.method == 'POST':
            print('delete')
            #delete record
            return render_template('index.haml', title='delete done')
        else:
            users = []
            result = models.User.all()
            for row in result:
                print(row.name)
                users.append((row.id, row.name))
            return render_template('read.haml', title='read done', list = users)