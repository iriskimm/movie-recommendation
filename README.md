# movie-recommendation
This project was developed with the goal of learning and practicing **Machine Learning** algorithms. I used **Scikit-Learn** to calculate cosine similarity score and to compute Term Frequency-Inverse Document Frequency(TF-IDF), and utilized **Streamlit** to create an interactive web dashboard that uses the ML model to display appropriate data. 

## Product Overview
<img src='resources/website_overview.png' width=80%>

## Data Cleaning
##### Datasets obtained from Kaggle: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
* Merged two datasets into one by matching movie_id
* Removed repeated or redundant columns
* Created a new 'score' column that contains weighted average for each movie
* Extracted keywords from text and convert text string into a list of keywords

## Algorithms
* Computed cosine similarity score based on movie genre, actors, the director, and plot keywords to compute TF-IDF vectors
