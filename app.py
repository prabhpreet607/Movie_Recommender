import pickle
import streamlit as st
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=43cdedacf09820e42af3f8c27841c659&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies=pickle.load(open("movie_recommende.pkl","rb"))
movie=movies["title"].values

similarity=pickle.load(open("cosine_similarity.pkl","rb"))
def recommender(new_movie):
    index=movies[movies["title"]==new_movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended=[]
    recommended_poster=[]
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))
    return recommended, recommended_poster

st.header("MOVIE RECOMMENDER")
selected_movie_name=st.selectbox(" Type or select a movie from the dropdown",movie)
if st.button("Recommend"):
    recommend,poster=recommender(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend[0])
        st.image(poster[0])

    with col2:
        st.text(recommend[1])
        st.image(poster[1])

    with col3:
        st.text(recommend[2])
        st.image(poster[2])

    with col4:
        st.text(recommend[3])
        st.image(poster[3])

    with col5:
        st.text(recommend[4])
        st.image(poster[4])