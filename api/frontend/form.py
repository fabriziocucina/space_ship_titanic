import streamlit as st

st.title("Bienvenidos al Hyperespacio")

planets= ["Earth", "Moon","Mars"]
vip = ["SI","NO"]

player_planet = st.selectbox("Escoje vuestro planeta de origen",planets)
player_planet = st.selectbox("Escoje vuestro planeta de destino",planets)


st.text_input("Nombre",placeholder="Escribe tu nombre")
st.text_input("Edad",placeholder="Escribe tu edad")
st.radio("¿Eres VIP?",vip)
st.radio("¿Quieres viajar congelado? (Cryo Sleep)",vip)
