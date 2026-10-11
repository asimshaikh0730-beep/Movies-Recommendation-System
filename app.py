import pickle
import joblib
import streamlit as st

st.title("Movies REcommendation System")

with open("movies.pickle", "rb") as m:
    data = pickle.load(m)

similarity = joblib.load("simlarity.joblib")

movies = data["title"].values

def recommend(name_movie):
    movie_index = data[data["title"] == name_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]
    return [data.iloc[i[0]].title for i in movies_list]

name_movie = st.selectbox("Enter the Movies Name", movies)

if st.button("Recommend"):
    st.write("The Recommendation Movies are :")
    for title in recommend(name_movie):
        st.write(title)