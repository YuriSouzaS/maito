from flask import Flask, render_template, request
import os
import config 
from db import inserir_db, inserir_usr
from validation import *

app = Flask(__name__)

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

@app.route("/account_resp")
def account_resp():
    return render_template('new_account_usr.html')


@app.route("/homeSchool", methods=['GET', 'POST'])
def homeSchool():
    
    escola = request.form['escola']
    diretor = request.form['diretor']
    classificacao = request.form['tipo']
    ensino = request.form['ensino']
    estado = request.form['estado']
    cidade = request.form['cidade']
    cep = request.form['cep']
    rua = request.form['rua']
    num = request.form['numero_casa']
    email = request.form['email']
    senha = request.form['senha']

    
    # instancia da class institution
    inst = config.Institution(escola, diretor, classificacao, ensino, estado, cidade, cep, rua, num, email, senha)
    # Metodo que faz o envio ao banco
    inserir_db(inst.nome, inst.diretor, inst.tipo, inst.ensino, inst.estado, inst.municipio, inst.cep, inst.rua, inst.numero, inst.email, inst.senha)
    
    return render_template('home_school.html', inst = inst )

@app.route("/profileSchool")
def profileSchool():
    return render_template('profileSchool.html')


@app.route("/homeResponsavel", methods=['GET', 'POST'])
def homeResponsavel():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    nascimento = request.form['nascimento']
    documento = request.form['documento']
    email = request.form['usremail']
    senha = request.form['usrsenha']
    qrcode = request.form['qrcode']

    # instancia da class Responsavel
    resp = config.Responsavel(nome, sobrenome, nascimento, documento, email, senha, qrcode )

    # Metodo faz o envio ao banco
    inserir_usr(resp.nome, resp.data_nascimento, resp.documento, resp.email, resp.senha, resp.qrcode)
    
    return render_template('homeResponsavel.html', resp = resp)

if(__name__ == "__main__"):
    app.run(debug=True)