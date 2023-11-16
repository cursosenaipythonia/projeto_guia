from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy.util.langhelpers import has_compiled_ext
from .models import Note
from . import db
import pickle
import json
#import pandas as pd
import requests
import logging

views = Blueprint('views', __name__)
#app = Blueprint('app', __name__)

#app = Flask(__name__)

# Configuração do logging
logging.basicConfig(level=logging.DEBUG)
"""
#Rota inicial 
@views.route('/')
def inicio():
    user = {'is_authenticated': False}  # Definindo um usuário fictício como não autenticado
    return render_template('index.html')
  

@views.route('/')
def inicio():
# Verifica se o usuário está autenticado de acordo com a lógica do Flask-Login
    return render_template('index.html')
"""

"""
# Carregue a lista de filmes uma vez ao iniciar o aplicativo
with open('models/filmes_dataframe.pkl', 'rb') as file:
    filmesData = pickle.load(file)

with open('models/filmes_df.pkl', 'rb') as file:
    filmesFilter = pickle.load(file)

# Carregar o modelo em um novo código
with open('models/modelo.pkl', 'rb') as file:
    similarity = pickle.load(file)
"""
# Não saberei explicar em detalhes, mas, em resumo, usa uma API que busca a logo dos filmes
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao fazer requisição à API: {e}")
        return None

def recommend(movie):
    logging.debug("Entrou na função recommend.")
    index = filmesData[filmesData['title'] == movie].index
    if len(index) > 0:
        index = index[0]
        distances = sorted(enumerate(similarity[index]),
                        reverse=True,
                        key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[0:10]:
        # buscar o cartaz do filme 
            movie_id = filmesData.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(filmesData.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters
    else:
        return None, None

@views.route("/home", methods=["GET", "POST"])
@login_required
def index():
    logging.debug("Entrou na rota index.")

    generos = ['Action', 'Romance', 'Fantasy']
    nota_minima = 5
    ano_lancamento = 2017
    user_authenticated = current_user.is_authenticated  # Adicione esta linha
    
    if request.method == "POST":
        if "genres" in request.form:
            generos = request.form.getlist("genres")
        else:
            generos = ['Action', 'Romance', 'Fantasy']
        if "ratings" in request.form:
            nota_minima = int(request.form["ratings"])
        else:
            nota_minima = 5
        if "year" in request.form:
            ano_lancamento = int(request.form["year"])
        else:
            ano_lancamento = 2017

    if generos or nota_minima or ano_lancamento:
        filmes_selecionados = filmesFilter[
            (filmesFilter['genres'].apply(lambda x: all(genero in x for genero in generos))) if generos else True
            & (filmesFilter['vote_average'] >= nota_minima) if nota_minima else True
            & (filmesFilter['release_date'].apply(lambda x: int(x[:4]) <= ano_lancamento)) if ano_lancamento else True]

        print("Filmes selecionados:", filmes_selecionados)  # Adicione esta linha

    if not filmes_selecionados.empty:
        nome_do_filme = filmes_selecionados['title'].values[0]
    else:
        nome_do_filme = "Nenhum filme foi selecionado"
    
    selected_movie = nome_do_filme
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Passa os dados para o template
    movie_list = filmesData['title'].values
    # Verifica se o usuário está autenticado antes de passá-lo para o template
    user_authenticated = current_user.is_authenticated
    return render_template("home.html",
                        movie_list=movie_list,
                        selected_movie=selected_movie,
                        recommended_movie_names=recommended_movie_names,
                        recommended_movie_posters=recommended_movie_posters,
                        generos=generos,
                        ano_lancamento=ano_lancamento,
                        nota_minima=nota_minima,user_authenticated=user_authenticated,
                           user=current_user)  # Adicione esta linha)


# Adicionar Notas na Guia.
@views.route('/index', methods=['GET', 'POST'])
@login_required
def home():
    logging.debug("Entrou na rota home.")
    if request.method == 'POST':
        note = request.form.get('note')  # Obtém a nota do HTML
        logging.debug(f"Note to be added: {note}")
        
        if len(note) < 5:
            logging.warning("Nota muito curta.")
            flash('Nota muito curta!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)  # fornece o esquema para a nota
            db.session.add(new_note)  # adiciona a nota ao banco de dados
            db.session.commit()
            logging.debug("Nota adicionada com sucesso.")
            flash('Nota adicionada!', category='success')

    return render_template("home.html", user=current_user)


# Deletar notas da guia.
# Deletar notas da guia.
@views.route('/delete-note', methods=['POST'])
def delete_note():
    logging.debug("Entrou na rota delete-note.")
    try:
        note = json.loads(request.data)  # esta função espera um JSON do arquivo INDEX.js
        noteId = note['noteId']
        logging.debug(f"Tentando deletar nota com ID: {noteId}")
        note = Note.query.get(noteId)
        
        if note:
            if note.user_id == current_user.id:
                db.session.delete(note)
                db.session.commit()
                logging.debug("Nota deletada com sucesso.")
                flash('Nota deletada com sucesso!', category='success')
                return jsonify({"status": "success"})
            else:
                logging.warning("Usuário não autorizado a excluir esta nota.")
                return jsonify({"status": "unauthorized"})
        else:
            logging.warning("Nota não encontrada.")
            return jsonify({"status": "not_found"})
    except Exception as e:
        logging.error(f"Erro ao deletar nota: {e}")
        return jsonify({"status": "error"})