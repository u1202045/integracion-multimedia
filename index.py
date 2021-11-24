import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
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

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/registro_mascotas/<string:Nombre>/')
def registro_mascotas(Nombre):
    return render_template('registro_mascotas.html', Nombre=Nombre)

@app.route('/log', methods = ['POST'])
def log():
    nombre=request.form['Name']
    email=request.form['E-mail']
    nickname=request.form['Nickname']
    contraseña=request.form['Contraseña']
    
    img=0

    data = {'Nombre': nombre, 'E-mail': email, 'Nickname': nickname, 'Contraseña': contraseña} #Firesotre

    db.collection('users').document(nombre).set(data)
    return render_template("ver.html", Nombre=nombre, Email=email, Nickname = nickname, Contraseña=contraseña,img=img)


@app.route('/log_in', methods = ['POST'])
def log_in():
    nickname=request.form['Nickname']
    contraseña=request.form['Contraseña']

    docs= db.collection('users').where("Nickname", "==", nickname).get()

    img=0

    for d in docs:
        s = d.to_dict()
        print('Nombre: {} \n Correo: {} \n Nickname: {} \n Contraseña: {}\n'.format(s['Nombre'],s['E-mail'], s['Nickname'],s['Contraseña']))

    nombre=s['Nombre']
    email = s['E-mail']

    if s['Nickname'] == nickname and s['Contraseña'] == contraseña:
        y = 'Verdadero :)'
        return render_template("ver.html", Nombre=nombre, Email=email, Nickname = nickname, Contraseña=contraseña,img=img)

    else:
        return render_template("datos_ingreso.html")


@app.route('/log_mascota/<string:Nombre>/', methods = ['POST'])
def log_mascota(Nombre):
    #Nombre=request.form['Nombre']
    nombre_mascota=request.form['Name']
    edad=request.form['Edad']
    sexo=request.form['Sexo']
    descripcion=request.form['Descripcion']
    cualidades=request.form['Cualidades']

    docs= db.collection('users').where("Nombre", "==", Nombre).get()

    img=0

    for d in docs:
        s = d.to_dict()
        print('Nombre: {} \n Correo: {} \n Nickname: {} \n Contraseña: {}\n'.format(s['Nombre'],s['E-mail'], s['Nickname'],s['Contraseña']))

    nickname=s['Nickname']
    email = s['E-mail']
    contraseña=s['Contraseña']

    data_mascota = {'Nombre': nombre_mascota, 'Edad': edad, 'Sexo':sexo, 'Descripcion':descripcion, 'Cualidades':cualidades}
    db.collection('users').document(Nombre).collection(nombre_mascota).document('Datos').set(data_mascota)

    return render_template("ver.html", Nombre_masc=nombre_mascota, Edad=edad, Sexo=sexo, Descripcion=descripcion, Cualidades=cualidades, Nombre=Nombre, Email=email, Nickname = nickname, Contraseña=contraseña,img=img)

@app.route('/bus_mas/<string:Nombre>/', methods = ['POST'])
def bus_mas(Nombre):
    nombre_mascota=request.form['Name_mas']


    funda_a_ref = db.collection('users').document(Nombre)
    docs = funda_a_ref.collection(nombre_mascota).where("Nombre", "==", nombre_mascota).get()

    #docs= db.collection(nombre_mascota).where("Nombre", "==", nombre_mascota).get()

    for d in docs:
        s = d.to_dict()
        print('Nombre: {} \n Edad: {} \n Sexo: {} \n Descripcion: {}\n Cualidades: {}\n'.format(s['Nombre'],s['Edad'], s['Sexo'],s['Descripcion'],s['Cualidades']))

    edad = s['Edad']
    sexo = s['Sexo']
    descripcion = s['Descripcion']
    cualidades = s['Cualidades']

    ids=random.randrange(0, 110, 1)
    img=nombre_mascota

    return render_template("ver.html", Nombre=Nombre, Nombre_masc=nombre_mascota, Edad=edad, Sexo=sexo, Descripcion=descripcion, Cualidades=cualidades, id=ids, img=img)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

#python .\index.py