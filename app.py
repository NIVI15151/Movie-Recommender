import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list_titles = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set page configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Customize theme and layout
st.markdown(
    """
    <style>
        body {
            color: #1E1E1E;
            background-color: #F5F5F5;
        }
        .streamlit-container {
            max-width: 1200px;
        }
        .sidebar .sidebar-content {
            background-color: #333;
            color: #FFF;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main content
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Movie to select?',
    movies_list_titles
)

if st.button('Recommend'):
    movie_index = movies_list[movies_list['title'] == selected_movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies_list.iloc[i[0]].title)

    st.subheader(f"Recommended movies for {selected_movie_name}:")
    for movie in recommended_movies:
        st.write(movie)
