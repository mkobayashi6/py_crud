from flask import *
from db import models

class IndexController:
    def show():
        return render_template('index.html', title='hello py')

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
        return render_template('read.html', title='read done', list = users)
        
class WriteController:
    def create():
        print('create')
        #create record
        return render_template('create.html', title='create show')
        
    def new(form):
        print('new')
        print(form['name'])
        #create record
        return render_template('index.html', title='create done')
        
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
            return render_template('read.html', title='update done', list = users)
        else:
            # todo: not repeat user select
            users = []
            result = models.User.all()
            for row in result:
                print(row.name)
                users.append((row.id, row.name))
            return render_template('read.html', title='read done', list = users)
        
    def delete(request):
        if request.method == 'POST':
            print('delete')
            #delete record
            return render_template('index.html', title='delete done')
        else:
            users = []
            result = models.User.all()
            for row in result:
                print(row.name)
                users.append((row.id, row.name))
            return render_template('read.html', title='read done', list = users)