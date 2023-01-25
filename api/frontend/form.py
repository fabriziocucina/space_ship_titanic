import streamlit as st

def datos (nombre,edad,vip,cryo):
    data = f"tu {nombre}, tienes {edad}, eres {vip}, cama {cryo}"
    return data
        

st.title("Bienvenidos al Hyperespacio")

planets= ["Earth", "Moon","Mars"]
vip = ["SI","NO"]
sleep = ["SI","NO"]

form = st.form("creacion_de_pasajero", clear_on_submit=True)
nombre = form.text_input("Nombre",placeholder="Escribe tu nombre")
edad = form.number_input("Edad",step=1,max_value=150,min_value=1)
vip = form.checkbox("Eres VIP")
cryo = form.checkbox("Tienes Cryo")
form_button = form.form_submit_button(label='Crear')
if form_button:
    st.write(f"{nombre},{edad},{vip},{cryo}")

