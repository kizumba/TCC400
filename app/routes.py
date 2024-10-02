from app import app
from flask import render_template
from flask import request
from flask import flash
from flask import redirect

@app.route('/')
@app.route('/index')
#@app.route('/index/<nome>/<profissao>/<canal>')
def index():
    return render_template('index.html')

@app.route('/evento')
def evento():
    return render_template('evento.html')

@app.route('/eventos_lista')
def eventos_lista():
    return render_template('eventos_lista.html')

@app.route('/assentos_lista')
def assentos_lista():
    return render_template('assentos_lista.html')

@app.route('/assento/<fileira>/<int:j>')
def assento(fileira,j):
    return render_template('assento.html',fileira=fileira, j=j)

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
    
# ------------- CRUD ----------------
@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

#inserir usuário

#ver usuário

#editar usuário

#apagar usuário