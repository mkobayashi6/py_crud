from flask import *
from models import dbUtil

app = Flask(__name__)

@app.route('/')
def index():
    dbUtil.connection.getConnection()
    return render_template('index.html', title='hello py')

if __name__ == '__main__':
    app.run(debug=True)