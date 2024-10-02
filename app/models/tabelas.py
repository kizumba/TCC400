import datetime
from app import db


class User(db.Model):
    __tablename__="usuarios"

    id = db.Column(db.Integer, primary_key=True)
    apelido =db.Column(db.String(80), unique=True)
    senha = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(15), unique=True)
    admin = db.Column(db.Boolean, default=False)

    def __init__(self, nome, email, telefone, apelido, senha, admin):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.apelido = apelido
        self.senha = senha
        self.admin = admin
    
    def __repr__(self):
        return '<User %r>' % self.apelido


'''
class Evento(db.Model):
    __tablename__="eventos"    

    id = db.Column(db.Integer, primary_key=True)
    tema = db.Column(db.String(80))
    descricao = db.Column(db.String(256))
    lotacao = db.Column(db.Integer)
    
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_evento = db.Column(db.DateTime)

    hora_inicio = db.Column(db.Time)
    duracao = db.Column(db.Numeric(9, 2))

class Assento(db.Model):
    __tablename__="assentos"

    id = db.Column(db.Integer, primary_key=True)
    fileira = db.Column(db.Char(1))
    numero = db.Column(db.Integer)
    livre = db.Column(db.Boolean, default=True)
    tipo_assento = db.Column(db.String(80))
    cor = db.Column(db.String(10))


class Ingresso(db.Model):
    __tablename__="ingressos"

    id = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float)
    data_venda = db.Column(db.DateTime, default=datetime.utcnow)
    hora_venda = db.Column(db.Time)
    tipo_ingresso = db.COlumn(db.String(80))


class Cliente(db.Model):
    __tablename__="clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11), unique=True)

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __repr__(self):
        return '<Cliente %r, CPF %r>' % self.nome, self.cpf
    

'''