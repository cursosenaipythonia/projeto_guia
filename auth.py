from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/')
def login():
  return "<p> Entrar </p>"


@auth.route('/logout')
def logout():
  return "<p> Sair </p>"

@auth.route('/sign-up')
def sign-up():
  return "<p> Cadastro</p>"
