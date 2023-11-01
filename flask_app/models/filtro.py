from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Carregar o arquivo movies.csv em um DataFrame
df = pd.read_csv('movies.csv')


@app.route('/')
def formulario():
  return render_template('interesse.html')


@app.route('/filtrar', methods=['POST'])
def filtrar():
  generos = request.form.getlist('genero')
  ano = int(request.form['ano'])
  avaliacao = int(request.form['avaliacao'])

  # Aplicar os filtros
  resultado = df[(df['Genero'].isin(generos)) & (df['Ano'] == ano) &
                 (df['Avaliacao'] == avaliacao)]

  # Agora você pode fazer o que quiser com o DataFrame "resultado", como exibi-lo na página ou salvá-lo em um novo arquivo.

  return render_template('guia.html', resultado=resultado)
