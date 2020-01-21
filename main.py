from flask import *
from controller import controller

app = Flask(__name__)

@app.route('/')
def index():
    return controller.IndexController.show()
@app.route('/create')
def create():
    return controller.WriteController.create()
@app.route('/read')
def read():
    return controller.ReadController.read()
@app.route('/update')
def update():
    return controller.WriteController.update()
@app.route('/delete')
def delete():
    return controller.WriteController.delete()

if __name__ == '__main__':
    app.run(debug=True)