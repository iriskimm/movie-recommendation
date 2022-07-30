import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb
import config

movie = Movie()
tmdb = TMDb()
tmdb.api_key = config.api_key

movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

st.set_page_config(layout='wide')
st.header('Iris\' Movie Recommendation')

movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like:', movie_list) # user's selection is stored in title

if st.button('Recommend'): 
    pass