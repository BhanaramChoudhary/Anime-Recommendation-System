import streamlit as st
import pickle
import pandas as pd

def recommend(anime):
    index = animes[animes['animename'] == anime].index[0]
    distances = similarity[index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_animes = []
    for i in anime_list:
        anime_id = i[0]


        recommend_animes.append(animes.iloc[i[0]].animename)
    return recommend_animes




animes_dict = pickle.load(open('anime_dict.pkl','rb'))
animes = pd.DataFrame(animes_dict)

similarity = pickle.load(open('sim.pkl','rb'))
st.title('Anime Recommender System')

selected_anime_name = st.selectbox (
'Looking for anime?',
animes['animename'].values)


if st.button('Recommend'):
    recommendations = recommend(selected_anime_name)
    for i in recommendations:
        st.write(i)



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp{{
             background-image: url("https://external-preview.redd.it/gOSvKrZoOVD1rzDsWLQcIfb-YsBwF_F3tDkbun2uoYA.jpg?blur=40&format=pjpg&auto=webp&s=2db87ad9c6d0c55cac27a8e28ad25b92c656d857");
             background-attachment: fixed;
             background-size: cover;
             color:black;

            }}

         </style>
         """,
         unsafe_allow_html=True)


add_bg_from_url()
