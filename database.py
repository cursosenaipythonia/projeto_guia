from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
"""
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from registro.database import metadata, db_session

perfil_table = Table('perfil', metadata,
    Column('id', Integer, primary_key=True),
    Column('genero', String),
    Column('classificacao', String),
    Column('avaliacao', String)
)

class Perfil(object):
  def __init__(self, genero, classificacao, avaliacao):
      self.genero = genero
      self.classificacao = classificacao
      self.avaliacao = avaliacao

mapper(Perfil, perfil_table)"""
"""

Peço desculpas novamente pelo erro. Parece que há um problema na forma como a extensão db está sendo registrada no Flask-Migrate.

Tente substituir a linha:

Python

Copy

Insert
str(current_app.extensions['migrate'].db.engine.url).replace('%', '%%')
por:

Python

Copy

Insert
str(current_app.extensions['migrate'].db.get_engine().url).replace('%', '%%')
Isso deve ajudar a corrigir o erro KeyError: None ao executar o comando flask db migrate.

Após fazer essa alteração, tente executar novamente o comando flask db migrate -m "Migração inicial" e veja se o erro persiste. Se ainda enfrentar problemas, por favor, forneça mais informações sobre a estrutura do seu projeto e as importações no arquivo env.py dentro da pasta flask_app/migrations, para que eu possa entender melhor o contexto e fornecer uma solução adequada.

"""
