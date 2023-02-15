# Movie Recommendation System
An NLP-based recommendation system. Built using Python and Scikit-learn and deployed using Streamlit. 

## Product Overview
<img src='resources/website_overview.png' width=80%>

## Data Mining
##### Datasets obtained from Kaggle: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
* Merged two datasets into one by matching movie_id
* Removed repeated or redundant columns
* Combined trivial columns into a new 'score' column with a weighted rating
* Extracted keywords from text and convert text string into a list of keywords

## Algorithms
* Computed cosine similarity score based on movie genre, actors, the director, and plot keywords to compute TF-IDF vectors

