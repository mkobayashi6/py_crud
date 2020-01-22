from flask import *
from controller import controller

app = Flask(__name__)

@app.route('/')
def index():
    return controller.IndexController.show()
    
@app.route('/create')
def create():
    return controller.WriteController.create()
    
@app.route('/new', methods=['POST'])
def new():
    return controller.WriteController.new(request.form)
    
@app.route('/read', methods=['GET', 'POST'])
def read():
    return controller.ReadController.read(request)
    
@app.route('/update', methods=['GET', 'POST'])
def update():
    return controller.WriteController.update(request)
    
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    return controller.WriteController.delete(request)

if __name__ == '__main__':
    app.run(debug=True)