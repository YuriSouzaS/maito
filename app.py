from flask import Flask, render_template, request, url_for, redirect
import os
import Institution 



app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '088011'
# app.config['MYSQL_DB'] = 'DB_MAITO'

# mysql = MYSQL(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login/user")
def user():
    return render_template('login_usr.html')

@app.route("/login/school")
def school():
    return render_template('login_school.html')

@app.route("/login/security")
def security():
    return render_template('login_security.html')

@app.route("/account")
def account():
    return render_template('new_account.html')

@app.route("/homeSchool", methods=['GET', 'POST'])
def homeSchool():
    
    datas = []
    
    escola = request.form['escola']
    diretor = request.form['diretor']
    tipo = request.form['tipo']
    ensino = request.form['ensino']
    estado = request.form['estado']
    cidade = request.form['cidade']
    cep = request.form['cep']
    rua = request.form['rua']
    num = request.form['numero_casa']
    senha = request.form['senha']

    inst = Institution.Institution(escola, diretor, tipo, ensino, estado, cidade, cep, rua, num, senha)

    datas.append(escola)
    datas.append(diretor)
    datas.append(tipo)
    datas.append(ensino)
    datas.append(estado)
    datas.append(cidade)
    datas.append(cep)
    datas.append(rua)
    datas.append(num)
    datas.append(senha)

    # print(datas)
    return render_template('home_school.html', inst = inst )

if(__name__ == "__main__"):
    app.run(debug=True)