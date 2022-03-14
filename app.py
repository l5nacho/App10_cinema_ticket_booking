from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(port=8000, debug=True)
