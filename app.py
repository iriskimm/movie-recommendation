import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb
import config

movie = Movie()
tmdb = TMDb()
tmdb.api_key = config.api_key
# tmdb.language = 'ko-KR' # show movie titles & images in korean

movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

def get_recommendations(title): 
    idx = movies[movies['title'] == title].index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    images = []
    titles = []
    for i in movie_indices: 
        id = movies['id'].iloc[i]
        details = movie.details(id)
        try: 
            images.append('https://image.tmdb.org/t/p/w500' + details['poster_path'])
        except:
            images.append('no_image.jpg')
        titles.append(details['title'])

    return images, titles

st.set_page_config(layout='wide')
st.header('Iris\' Movie Recommendation')

movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like:', movie_list) # user's selection is stored in title

if st.button('Recommend'): 
    with st.spinner('Please wait...'):
        images, titles = get_recommendations(title)

        idx = 0
        for i in range(0, 2): 
            cols = st.columns(5)
            for col in cols: 
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1
