from flask import Flask, render_template, request, session, url_for, redirect, flash
import os
import build.config as config 
from build.geradorKey import sessionKey
from build.model.db import select_user, buscar_alunos_resp, contarRegistros, buscar_temporario

app = Flask(__name__)


# usar gerador randon para as keys
app.secret_key = sessionKey()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login/user", methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        print(request.form['email'])
        user = select_user("responsavel", request.form['email'])
        try:
            if user[5] == request.form['senha']:
                # iniciada a session
                session['email'] = user[4]
                return redirect(url_for('homeResponsavel') )
        except:
            flash('Email ou senha estão errados.')
            return redirect(url_for('user'))
    return render_template('user/login_usr.html')
    
@app.route("/login/school")
def school():
    return render_template('school/login_school.html')

@app.route("/login/security")
def security():
    return render_template('setor/login_security.html')

@app.route("/account", methods=['GET', 'POST'])
def account():

    # O metodo sendo post, salvara os dados no db e iniciara o session na pagina home
    if request.method == 'POST':
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

        #instancia da class institution
        inst = config.Institution(escola, diretor, classificacao, ensino, estado, cidade, cep, rua, num, email, senha)

        # iniciada a session
        session['nome'] = inst.nome

        # redireciona para home do instituição
        return redirect(url_for('homeSchool') )
    
    # se não for post, mostre esta pagina
    return render_template('school/new_account.html')

@app.route("/account_resp", methods=['GET', 'POST'])
def account_resp():
    
    # O metodo sendo post, salvara os dados no db e iniciara o session na pagina home
    if request.method == 'POST':
        
        # armazemando dados o db
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        nascimento = request.form['nascimento']
        documento = request.form['documento']
        email = request.form['usremail']
        senha = request.form['usrsenha']
    
        # instancia da class Responsavel
        resp = config.Responsavel(nome, sobrenome, nascimento, documento, email, senha)

        # iniciada a session
        # session['nome'] = resp.nome
        session['email'] = resp.email
        
        # redireciona para home do usuario
        return redirect(url_for('homeResponsavel'))
    
    # se não for post, mostre esta pagina
    return render_template('user/new_account_usr.html')


@app.route("/homeSchool", methods=['GET', 'POST'])
def homeSchool():
    if 'email' in session:
        return render_template('school/home_school.html')
    return f"You are not logged in"


@app.route("/profileSchool")
def profileSchool():
    return render_template('school/profileSchool.html')


@app.route("/homeResponsavel", methods=['GET', 'POST'])
def homeResponsavel():
    if 'email' in session:
        data_resp = select_user("responsavel", session['email'] )
        data_aluno = buscar_alunos_resp("responsavel", session['email'] )
        data_temp = contarRegistros("responsavel_aluno", "resp_temp", data_resp[0])
        if data_aluno == False:
            data_aluno == "Sem registros"
        return render_template('user/homeResponsavel.html', usr=data_resp, data_aluno=data_aluno, data_temp=data_temp)
    return f"You are not logged in"


@app.route('/logout')
def logout():
    # remove a sessão
    session.pop('nome', None)
    return redirect(url_for('index'))


@app.get("/homeResponsavel/temporarios")
def homeResponsavelTemp():
    if 'email' in session:
        data_resp = select_user("responsavel", session['email'])
        data_temp = buscar_temporario("responsavel_aluno", data_resp[0])
        data = config.Temporario.formatarDados(data_temp)
    return render_template("user/temporario/ResponsavelTemp.html", data_resp=data_resp, data_temp = data)


if(__name__ == "__main__"):
    app.run(debug=True)