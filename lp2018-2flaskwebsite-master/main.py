# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from flask import session, flash, abort, send_from_directory

from random import randint
from json import JSONEncoder
from hashlib import sha256

from sql import DataBase
from imagem import carteirinha

import os
import datetime as dt
import jsonpickle

HOST = '127.0.0.1'
PORT = 5000

# JSON Encoding
def _default_encoder_(self, obj):
    return getattr(obj.__class__, "__json__", _default_encoder_.default)(obj)
_default_encoder_.default = JSONEncoder.default

JSONEncoder.default = _default_encoder_

def unjson(user):
    return jsonpickle.decode(user) if type(user) is str else user

def dropsession(session):
    if os.name == 'posix':
        temp = "{}/temp".format(os.getcwd())
        for path in os.listdir(temp):
            os.remove("{}/{}".format(temp, path))
        session.pop('usuario_logado', None)
    else:
        temp = "{}\\temp".format(os.getcwd())
        for path in os.listdir(temp):
            os.remove("{}\\{}".format(temp, path))
        session.pop('usuario_logado', None)

def string(x):
    return '' if x is None else ("'{}'".format(x) if type(x) is str else str(x))

def pswd_hash(pswd):
    return sha256(pswd.encode('utf-8')).hexdigest()

def validar_cpf(cpf):
    invalidos = ['00000000000', '11111111111',
                 '22222222222', '33333333333',
                 '44444444444', '55555555555',
                 '66666666666', '77777777777',
                 '88888888888', '99999999999']
    if type(cpf) is not str:
        if type(cpf) is int:
            return validar_cpf(str(cpf))
        else:
            return False
    elif len(cpf) != 11:
        return False
    elif cpf in invalidos:
        return False
    
    p = [11,10,9,8,7,6,5,4,3,2]
    s = ((sum([int(x)*y for x,y in zip(cpf[:-2],p[1:])])*10)%11)
    d = '0' if s > 9 else str(s)
    if d != cpf[-2]:
        return False
    s = ((sum([int(x)*y for x,y in zip(cpf[:-1],p)])*10)%11)
    d = '0' if s > 9 else str(s)
    if d != cpf[-1]:
        return False
    return True

def gerar_cpf():
    p = [11,10,9,8,7,6,5,4,3,2]
    cpf = ''.join([str(randint(0,9)) for _ in range(9)])
    s = ((sum([int(x)*y for x,y in zip(cpf, p[1:])])*10)%11)
    d = '0' if s > 9 else str(s)
    cpf += d
    s = ((sum([int(x)*y for x,y in zip(cpf, p)])*10)%11)
    d = '0' if s > 9 else str(s)
    cpf += d
    if validar_cpf(cpf):
        return cpf
    else:
        return gerar_cpf()
    
db = DataBase('teste')

class CPFInvalido(Exception):
    pass

class SenhaErrada(Exception):
    pass
            
class Usuario:

    _name_ = 'USUARIO'

    _must_ = ('nome', 'cpf', 'senha')

    _init_ = {'nome'  : 'CHAR(255) NOT NULL',
              'cpf'   : 'CHAR(11) PRIMARY KEY',
              'senha' : 'CHAR(64) NOT NULL'}      
    
    def __init__(self, db, **kwargs):
        self.db = db
        self.cpf = kwargs['cpf']
        if not validar_cpf(self.cpf):
            raise CPFInvalido

        self.db(self._create_table())
        
        if self.cpf not in sum(self.db("SELECT cpf FROM `{}`".format(self._name_)),tuple()):
            for key in self._init_:
                if key not in kwargs:
                    if key in self._must_:
                        raise KeyError('kwarg {} missing.'.format(key))
                    else:
                        kwargs[key] = None
                        
            kwargs['senha'] = pswd_hash(kwargs['senha'])
            self.db(self._insert_into(kwargs))
        else:
            cmd = "SELECT senha FROM `{}` WHERE cpf = {}".format(self._name_, string(self.cpf))
            check, = self.db(cmd)[0]
            if pswd_hash(kwargs['senha']) != check:
                raise SenhaErrada
            
    def __bool__(self):
        return True

    def __json__(self):
        return jsonpickle.encode(self)
        
    def __setitem__(self, k, v):
        """ Usuario[k] = v
        """
        args = (self._name_, k, string(v), string(self.cpf))
        self.db("UPDATE `{}` SET `{}` = {} WHERE `CPF` = {}".format(*args))

    def __getitem__(self, k):
        """ Usuario[k, ...]
        """
        if k is None:
            mono = False
            k = '*'
        elif type(k) is tuple:
            mono = False
            k = ", ".join(k)
        else:
            mono = True
        args = (k, self._name_, string(self.cpf))
        cmd = "SELECT {} FROM `{}` WHERE `CPF` = {}".format(*args);

        out, = self.db(cmd)
        if mono:
            return out[0]
        else:
            return out

    def _create_table(self):
        dic = self._init_
        r = ",\n".join(["{} {}".format(k, dic[k]) for k in dic])
        return "CREATE TABLE IF NOT EXISTS `{}` ({})".format(self._name_, r)

    def _insert_into(self, kwargs):
        keys = []
        vals = []
        for key in kwargs:
            keys.append(key)
            vals.append(string(kwargs[key]))
        k = ",\n".join(keys)
        v = ",\n".join(vals)
        return "INSERT INTO `{}` ({}) VALUES ({})".format(self._name_,k,v)
        

class Aluno(Usuario):

    _must_ = ('nome', 'cpf', 'senha')

    _name_ = 'ALUNO'

    _init_ = {'nome'           : 'CHAR(255) NOT NULL',
              'cpf'            : 'CHAR(11) PRIMARY KEY',
              'dre'            : 'CHAR(9) NOT NULL',
              'senha'          : 'CHAR(64) NOT NULL',
              'unidade'        : 'CHAR(255)',
              'curso'          : 'CHAR(255)',
              'nome_pai'       : 'CHAR(255)',
              'nome_mae'       : 'CHAR(255)',
              'naturalidade'   : 'CHAR(255)',
              'nacionalidade'  : 'CHAR(255)',
              'nascimento'     : 'DATE',
              'identidade'     : 'CHAR(255)',
              'orgao'          : 'CHAR(255)',
              'expedicao'      : 'DATE',
              'uf'             : 'CHAR(2)'
              }
    
    def __init__(self, db, **kwargs):
        Usuario.__init__(self, db, **kwargs)

kw1 = {'nome': 'Joāo Pedro Brandāo Rodrigues', 'cpf': '88562832200', 'dre':'116022848','senha': '123456',
     'unidade': 'Escola Politecnica', 'curso': 'Engenharia Civil', 'nome_pai': 'Jhonatan Jacobo',
     'nome_mae': 'Gina Weasley', 'naturalidade': 'Cidade Maravilhosa', 'nacionalidade': 'Brasil',
     'nascimento': '01/11/1996', 'identidade': '1821921', 'orgao': 'FIGADO', 'expedicao': '01/11/2006',
     'uf': 'RJ'}

kw2 = {'nome': 'Pedro Xavier', 'cpf': '12232331709', 'senha': '123456', 'dre':'116023847', 'unidade': 'Escola Politecnica',
       'curso': 'Engenharia de Computaçāo e Informaçāo', 'nome_pai': 'Pai do Pedro', 'nome_mae': 'Mae do Pedro',
       'naturalidade': 'Nova Friburgo', 'nacionalidade': 'Brasil', 'nascimento': '01/08/1998',
       'identidade': '1821921', 'orgao': 'INTESTINO', 'expedicao': '01/11/2006', 'uf': 'RJ'}

jampa = Aluno(db, **kw1)

pedro = Aluno(db, **kw2)


# FLASK Initializing
app = Flask(__name__)
app.secret_key = 'aula'

@app.route('/')
def login():
    dropsession(session)
    return render_template('login.html')

@app.route('/autenticar', methods=['POST', ])
def _call_0():
    cpf = request.form['usuariocpf']
    cpfs= sum(db("SELECT cpf FROM `ALUNO`"),tuple())
    if cpf in cpfs:
        senha = request.form['senha']
        try:
            aluno = Aluno(db, cpf=cpf, senha=senha)
            session['usuario_logado'] = aluno #aluno # cria uma sessao com o usuario preenchido no login
            return redirect('/home')
        except SenhaErrada:
            flash('Senha Incorreta!')
    else:
        flash('CPF não cadastrado!')
    dropsession(session)
    return redirect('/')

@app.route('/logout')
def _call_1():
    dropsession(session)
    return redirect('/')

@app.route('/home')
def _call_2():
    user = unjson(session['usuario_logado'])
    if user is None:
        dropsession(session)
        abort(503)
    else:
        pathash = "C{}{}".format(user['cpf'], dt.datetime.now().isoformat())
        
        link_carteirinha = 'http://{}:{}/carteirinha/{}'.format(HOST,PORT,pathash)
        link_logout = 'http://{}:{}/logout'.format(HOST,PORT)
    
        template = render_template('carteirinha.html', link=link_carteirinha , link2=link_logout)
        return template

@app.route('/carteirinha/<pathash>')
def _call_3(pathash):
    if session['usuario_logado'] is None:
        abort(503)
    else:
        #resgata o usuário
        user = unjson(session['usuario_logado'])

        #gera a imagem da carteirinha
        carteirinha(user, True)

    return send_from_directory("temp","carteirinha_{}.png".format(user['cpf']))


    
if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True ) # com debug true vai bastar salvar ao inves de ficar rodando diversas vezes    

print(os.name)