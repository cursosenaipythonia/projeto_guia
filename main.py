from website import create_app, views
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

login_manager = LoginManager(app)

# Sobrescreva a mensagem padrão
login_manager.login_message = "Faça o login para acessar esta página."
login_manager.login_message_category = "error"

"""
@app.route('/', methods=['GET', 'POST'])
def login():
  # Lógica para processar o login
  user = current_user()  # Substitua por sua lógica de autenticação
  if user:
    login_user(user)
    flash(login_manager.login_message, login_manager.login_message_category)
    return redirect(url_for('/login'))
  else:
    flash("Credenciais inválidas.", "error")
    return redirect(url_for('/login'))
"""

app = create_app()

# Rota padrão, será acessada quando a aplicação for iniciada


@app.route('/')
def home():
    user = {'is_authenticated': False}  # Definindo um usuário fictício como não autenticado
    return render_template('index.html', user=user)  # Substitua 'index.html' pelo seu modelo desejado



# Rota para lidar com o erro 404
@app.errorhandler(404)
def not_found_error(error):
  return render_template('404.html', user=current_user), 404


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
