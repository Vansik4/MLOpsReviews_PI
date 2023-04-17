from fastapi import FastAPI, Query, Path, UploadFile, File
import uvicorn
import pandas as pd
from typing import Optional
from typing import List
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI()

df = pd.read_csv('./plataformas_ratings.csv', sep=",")

@app.get('/')
def welcome():
    """
    Endpoint para dar la bienvenida a la API.
    """
    return {"message": "Bienvenido a la API de mi proyecto."}

@app.get('/get_max_duration/{year}/{platform}/{duration}')
def get_max_duration(year: int, platform: str, duration: str):
    df3 = df[(df['release_year'] == year) & (df['Plataforma'] == platform)]
    column = 'duration_int' if duration == 'min' else 'duration_type'
    titulo = df3.loc[df3[column].idxmax(), 'title']
    return titulo

@app.get('/get_score_count/{platform}')
def get_score_count(platform: str, scored: float, year: int):
    df_movies = df[(df['Plataforma'] == platform) & (df["type"] == "movie")]    
    movies = df_movies[(df_movies["release_year"] == year) & (df_movies["score_mean"] >= scored)]
    movies = movies.drop_duplicates(subset=['title'])
    return len(movies)


@app.get('/get_count_platform/{platform}')
def get_count_platform(platform: str) -> int:
    if platform == 'amazon':
        platforms = df[(df['Plataforma'] == 'amazon') & (df["type"] == "movie")]
    elif platform == 'netflix':
        platforms = df[(df['Plataforma'] == 'netflix') & (df["type"] == "movie")]
    elif platform == 'hulu':
        platforms = df[(df['Plataforma'] == 'hulu') & (df["type"] == "movie")]
    elif platform == 'disney':
        platforms = df[(df['Plataforma'] == 'disney') & (df["type"] == "movie")]
    else:
        return 'Plataforma no válida'
    unique_movies = platforms['id'].nunique()
    return unique_movies

@app.get('/get_actor/{platform}')
def get_actor(platform: str, year: int) -> str:
    df_actor = df[df['Plataforma'] == platform]
    df_year = df_actor[df_actor["release_year"] == year]
    try:
        actors = df_year["cast"].str.split(", ")
        actors_exploded = actors.explode()
        if actors_exploded.empty:
            raise AttributeError
        return actors_exploded.value_counts().index[0]
    except AttributeError:
        return "No actor available"
    

@app.get('/prod_per_country/{platform}')
def prod_per_country(tipo: str, pais: str, anio: int):
    df_plataform = df[(df["type"] == tipo) & (df["country"] == pais) & (df["release_year"] == anio)]    
    df_movie_count = df_plataform[df_plataform["type"] == "movie"]["title"].nunique()
    df_serie_count = df_plataform[df_plataform["type"] == "tv show"]["title"].nunique()
    output_dict = {"pais": pais, "anio": anio, "pelicula": df_movie_count, "serie": df_serie_count}
    return output_dict

@app.get('/get_contents/{rating}')
def get_contents(rating: str) -> int:    
    return len(df[df["rating_x"] == rating]["id"].unique())

df = df[["title", "score_mean"]]
vectorizer = CountVectorizer()
title_matrix = vectorizer.fit_transform(df["title"])
cosine_sim = cosine_similarity(title_matrix)

@app.get("/get_recommendations/{title}")
def get_recommendation(title: str, n: int = 5):
    # Obtener el índice de la película dada
    idx = df[df["title"] == title].index[0]
    # Obtener los puntajes de similitud para la película dada
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Ordenar las películas por puntaje de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Obtener los índices de las películas recomendadas
    movie_indices = [i[0] for i in sim_scores[1:n+1]]
    # Obtener las películas recomendadas
    top_recommendations = df.iloc[movie_indices]["title"].values.tolist()
    return {"title": title, "recommendations": top_recommendations}

