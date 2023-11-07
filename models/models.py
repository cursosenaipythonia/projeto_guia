from . import db
from flask_login import UserMixin

# Resto do código


class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
  __tablename__ = "usuario"
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.String(80), nullable=False)
  genres = db.Column(db.String(200))
  adult = db.Column(db.Boolean)
  ratings = db.Column(db.String(100))
  notes = db.relationship('Note')


"""
class PreferencesForm(FlaskForm):
  genres = SelectMultipleField('Gênero de filmes', choices=[('acao', 'Ação'), ('aventura', 'Aventura'), ('comedia', 'Comédia'), ('drama', 'Drama'), ('ficcao', 'Ficção Científica'), ('terror', 'Terror'), ('romance', 'Romance'), ('animacao', 'Animação'), ('documentario', 'Documentário'), ('outro', 'Outro')])
  adult = SelectField('Classificação adulta', choices=[('adulta', 'Sim'), ('criancas', 'Não')])
  ratings = SelectMultipleField('Nível de avaliações', choices=[('acima_de_5', 'Acima de 5'), ('abaixo_de_5', 'Abaixo de 5'), ('todas', 'Todas')])
  submit = SubmitField('Salvar Perfil')
  
  """
"""
def __init__(self, id, user_id, genres, adult, ratings):
  self.id = id
  self.user_id = user_id
  self.genres = genres
  self.adult = ratings


def __repr__(self):
  return "<UserPreferences {}>".format(self.user_id)
"""
