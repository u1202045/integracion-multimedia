from flask import Flask, render_template, request

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

@app.route('/red', methods = ['POST'])
def red():
    Tiempo=request.form['Tiempo']
    Ejercicios=request.form['Ejercicios']
    NotaTest=request.form['NotaTest']


    return render_template("ver.html", time=Tiempo, exer=Ejercicios, notaT=NotaTest)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

#python .\index.py