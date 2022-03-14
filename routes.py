from app import app

@app.route('/index')
def index():
    return '<h1>Indice</h1>'