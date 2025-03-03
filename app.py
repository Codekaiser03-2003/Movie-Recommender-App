import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np

# Directly assign the API key (Not recommended for production)
api_key = "39eea467429598301cc1e1c82fbc0987"

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data.get('poster_path', '')

movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity1 = pickle.load(open('similarity1.pkl','rb'))
similarity2 = pickle.load(open('similarity2.pkl','rb'))
similarity = np.concatenate([similarity1, similarity2], axis=0)

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

if st.button('Show Recommendation'):
    recommended_movie_names, posters = recommend(selected_movie)
    for name, poster in zip(recommended_movie_names, posters):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(poster, width=150)
        with col2:
            st.write(name)
