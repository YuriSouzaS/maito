from flask import Flask, render_template, request, session, url_for, redirect
import os
import config
from geradorKey import sessionKey

app = Flask(__name__)


# usar gerador randon para as keys
app.secret_key = sessionKey()

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
    return render_template('new_account.html')

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
        qrcode = request.form['qrcode']
    
        # instancia da class Responsavel
        resp = config.Responsavel(nome, sobrenome, nascimento, documento, email, senha, qrcode )

        # iniciada a session
        session['nome'] = resp.nome
        
        # redireciona para home do usuario
        return redirect(url_for('homeResponsavel'))
    
    # se não for post, mostre esta pagina
    return render_template('new_account_usr.html')


@app.route("/homeSchool", methods=['GET', 'POST'])
def homeSchool():
    if 'nome' in session:
        return render_template('home_school.html')
    return f"You are not logged in"


@app.route("/profileSchool")
def profileSchool():
    return render_template('profileSchool.html')


@app.route("/homeResponsavel", methods=['GET', 'POST'])
def homeResponsavel():
    if 'nome' in session:
        return render_template('homeResponsavel.html')
    return f"You are not logged in"


@app.route('/logout')
def logout():
    # remove a sessão
    session.pop('nome', None)
    return redirect(url_for('index'))


@app.get("/homeResponsavel/temporarios")
def homeResponsavelTemp():
    return render_template("ResponsavelTemp.html")


if(__name__ == "__main__"):
    app.run(debug=True)