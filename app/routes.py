from app import app
from flask import render_template
from flask import request
from flask import flash
from flask import redirect

@app.route('/')
@app.route('/index')
#@app.route('/index/<nome>/<profissao>/<canal>')
def index():
    nome = "André L"
    dados = {"profissao":"Auxiliar Administrativo","salario":1500.00}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/evento')
def evento():
    return render_template('evento.html')

@app.route('/assentos')
def assentos():
    return render_template('assentos.html')

@app.route('/contato', defaults={"nome":"usuário"})
@app.route('/contato/<nome>')
def contato(nome):
    return render_template('contato.html', nome=nome)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    #usuario = request.args.get('usuario')
    #senha = request.args.get('senha')
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == 'robocop@usuario' and senha=='123':
       return "usuario: {} e senha: {}".format(usuario, senha)
    else:
        flash("Dados inválidos.")
        flash("Senha ou Usuário errado(s)")
        return redirect('/login')