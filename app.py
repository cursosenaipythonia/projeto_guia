from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/cadastro')
def cadastro():
  return render_template('cadastro.html')


@app.route('/login')
def login():
  return render_template('login.html')


@app.route('/guia')
def guia():
  return render_template('guia.html')


@app.route('/perfil')
def perfil():
  return render_template('perfil.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
