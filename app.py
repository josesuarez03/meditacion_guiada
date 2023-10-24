from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

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
