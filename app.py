from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import requests

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        session['user_name'] = name
        return redirect(url_for('lobby'))
    return render_template('index.html')

@app.route('/lobby', methods=['GET', 'POST'])
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
def playa():
    return render_template('playa.html')

@app.route('/templo-zen-escena',methods=['GET','POST'])
def templo_zen():
    return render_template('templo_zen.html')

@app.route('/bosque-escena',methods=['GET','POST'])
def bosque():
    return render_template('bosque.html')

if __name__ == '__main__':
    app.run(debug=True)
