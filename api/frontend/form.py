import streamlit as st
from api.frontend import crear

st.title("Bienvenidos al Hyperespacio")

planets= ["Earth", "Moon","Mars"]

player_planet = st.selectbox("Escoje vuestro planeta de origen",planets)

st.write(player_planet)

st.text_input("Nombre",placeholder="Escribe tu nombre",)


# Using object notation
st.sidebar.button("Crear_Personaje",on_click=crear.crear())