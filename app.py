from flask import Flask, render_template, request, jsonify, redirect, url_for, session, abort
import requests
from functools import wraps

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'your_secret_key'

def auth_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if 'user_name' not in session:
            return render_template('403.html'), 403
        return func(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        session['user_name'] = name
        return redirect(url_for('lobby'))
    return render_template('index.html')

@app.route('/lobby', methods=['GET', 'POST'])
@auth_required
def lobby():
    user_name = session.get('user_name')
    return render_template('lobby.html', user_name=user_name)

@app.route('/save-name', methods=['POST'])
def save_name():
    data = request.get_json()
    name = data['name']
    session['user_name'] = name
    return jsonify({'status': 'ok'}), 200

@app.route('/playa-escena', methods=['GET','POST'])
@auth_required
def playa():
    return render_template('playa.html')

@app.route('/templo-zen-escena',methods=['GET','POST'])
@auth_required
def templo_zen():
    return render_template('templo_zen.html')

@app.route('/bosque-escena',methods=['GET','POST'])
@auth_required
def bosque():
    return render_template('bosque.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_server():
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
