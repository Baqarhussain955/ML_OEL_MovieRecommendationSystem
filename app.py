import pandas as pd
import streamlit as st
import pickle
import requests
from streamlit_option_menu import option_menu


# Function to fetch movie posters from TMDB API
def fetch_posters(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8f9e9efb3b81787d12456765463e238e")
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"


# Function to get movie recommendations
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_images = []
    for i in movies_list:
        j = i[0]
        recommended_movies.append(movies.iloc[j].title)
        recommended_movie_images.append(fetch_posters(movies.iloc[j].id))

    return recommended_movies, recommended_movie_images


# Load movie data and similarity matrix
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

# Set Streamlit page configuration
st.set_page_config(page_title="Movie Recommender System", layout="wide")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu", ["Home", "Recommendations"],
        icons=['house', 'film'], menu_icon="cast", default_index=0)

# Home Page
if selected == "Home":
    st.title("Welcome to the Movie Recommender System")
    st.write("Explore a wide range of movies and get personalized recommendations based on your preferences.")

# Recommendations Page
if selected == "Recommendations":
    st.title("Get Movie Recommendations")
    st.write("Select a movie from the dropdown below to get recommendations:")

    selected_movie = st.selectbox("Choose a movie", movies["title"].values)
    st.write(f"You selected: {selected_movie}")

    if st.button("Recommend"):
        recommendations, posters = recommend(selected_movie)
        col1, col2, col3,col4 , col5 = st.columns(5)
        with col1:
            st.text(recommendations[0])
            st.image(posters[0])
        with col2:
            st.text(recommendations[1])
            st.image(posters[1])
        with col3:
            st.text(recommendations[2])
            st.image(posters[2])
        with col4:
            st.text(recommendations[3])
            st.image(posters[3])
        with col5:
            st.text(recommendations[4])
            st.image(posters[4])

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #ffcccc;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .css-1d391kg {
        background-color: #ffffff;
        color: #333;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    .css-1v0mbdj {
        background-color: #ffffff;
        color: #333;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    .css-1cpxqw2 {
        color: #333;
        font-size: 18px;
        font-weight: bold;
    }
    .css-1hpcjlh {
        color: #555;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# import pandas as pd
# import streamlit as st
# import pickle
# import requests
# def fetch_posters(movie_id):
#     response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8f9e9efb3b81787d12456765463e238e".format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
# def recommend(movie):
#     movie_index = movies[movies["title"] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
#     recommended_movies=[]
#     recommended_movie_images=[]
#     for i in movies_list:
#         j=i[0]
#         recommended_movies.append(movies.iloc[j].title)
#         recommended_movie_images.append(fetch_posters(movies.iloc[j].id))
#     return recommended_movies, recommended_movie_images
# movies_dict=pickle.load(open("movies_dict.pkl","rb"))
# movies=pd.DataFrame(movies_dict)
# similarity=pickle.load(open("similarity.pkl","rb"))
# st.title("Movie Recommender System")
# selected_name_first = st.selectbox(
#     "How would you like to be contacted?",
#     movies["title"].values)
# st.write("You selected:", selected_name_first)
# if st.button("Recommend"):
#     recommendations,posters=recommend(selected_name_first)
#     col1, col2, col3,col4 , col5 = st.columns(5)
#     with col1:
#         st.text(recommendations[0])
#         st.image(posters[0])
#     with col2:
#         st.text(recommendations[1])
#         st.image(posters[1])
#     with col3:
#         st.text(recommendations[2])
#         st.image(posters[2])
#     with col4:
#         st.text(recommendations[3])
#         st.image(posters[3])
#     with col5:
#         st.text(recommendations[4])
#         st.image(posters[4])