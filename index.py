import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flask import Flask, render_template, request

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

"""@app.route('/')
def principal():
    return "Bienvenid@ a mi pagina"""

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/datos')
def datos():
    return render_template('datos.html')

@app.route('/ver')
def ver():
    return render_template('ver.html')

@app.route('/log', methods = ['POST'])
def log():
    nombre=request.form['Name']
    email=request.form['E-mail']
    contraseña=request.form['Contraseña']

    db.collection('users').add({'Mombre': nombre, 'E-mail': email, 'Contraseña': contraseña})

    return render_template("ver.html", Nombre=nombre, Email=email, Contraseña=contraseña)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

#python .\index.py