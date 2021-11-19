import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flask import Flask, render_template, request

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/datos_registro')
def datos_registro():
    return render_template('datos_registro.html')

@app.route('/datos_ingreso')
def datos_ingreso():
    return render_template('datos_ingreso.html')

@app.route('/ver')
def ver():
    return render_template('ver.html')

@app.route('/log', methods = ['POST'])
def log():
    nombre=request.form['Name']
    email=request.form['E-mail']
    contraseña=request.form['Contraseña']

    db.collection('users').add({'Mombre': nombre, 'E-mail': email, 'Contraseña': contraseña}) #Firesotre
    return render_template("ver.html", Nombre=nombre, Email=email, Contraseña=contraseña)


@app.route('/log_in', methods = ['POST'])
def log_in():
    nombre=request.form['Name']
    contraseña=request.form['Contraseña']

    docs= db.collection('users').where("Mombre", "==", "Omar" ).get()
    
    for doc in docs:
        lista = doc.to_dict()
    
    n = "'Contraseña' : '" + nombre + "'" 
    c = 'hola'
        

    return render_template("ver.html", Nombre=n, Contraseña=c)



if __name__ == '__main__':
    app.run(debug=True, port=5000)


#Obtener datos Firestore
'''doc = db.collection('users').get

for doc in docs:
    print(doc.to_dict())'''


#python .\index.py