from flask import Flask, flash, redirect, render_template, request
from projeto_guia import create_app

app = create_app()

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/cadastro')
def cadastro():
  return render_template('cadastro.html')


@app.route('/guia')
def guia():
  return render_template('guia.html')


@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
  if request.method == 'POST':
    genero = request.form.getlist('genero')
    classificacao = request.form['classificacao']
    avaliacao = request.form['avaliacao']

    perfil = Perfil(genero=genero,
                    classificacao=classificacao,
                    avaliacao=avaliacao)
    db_session.add(perfil)
    db_session.commit()

    return "Perfil cadastrado com sucesso!"

  return render_template('perfil.html')


#@app.route('/perfil')
#def perfil():
# return render_template('perfil.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    # Handle form submission
    email = request.form['email']
    password = request.form['password']
    # Do something with the username and password, like validation or authentication
    # Redirect to a different page or perform some action

  return render_template('login.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
