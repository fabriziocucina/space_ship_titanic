import streamlit as st

def datos (nombre,edad,vip,cryo):
    data = f"tu {nombre}, tienes {edad}, eres {vip}, cama {cryo}"
    return data
        
pasajeros = []
data_pasajeros = []
st.title("Bienvenidos al Hyperespacio")

planets= ["Earth", "Moon","Mars"]
vip = ["SI","NO"]
sleep = ["SI","NO"]
st.sidebar.write("Lista de Pasajeros")
form = st.form("creacion_de_pasajero", clear_on_submit=True)
nombre = form.text_input("Nombre",placeholder="Escribe tu nombre")
edad = form.number_input("Edad",step=1,max_value=150,min_value=1)
vip = form.checkbox("Eres VIP")
cryo = form.checkbox("Tienes Cryo")
form_button = form.form_submit_button(label='Crear')
if form_button:
    data_pasajeros.append(nombre)
    data_pasajeros.append(edad)
    data_pasajeros.append(vip)
    data_pasajeros.append(cryo)
    pasajeros.append(data_pasajeros)
for index, pasajero in enumerate(pasajeros):
    st.sidebar.write(f"Datos del pasajero: {pasajeros[index][0]},{pasajeros[index][1]}{pasajeros[index][2]},{pasajeros[index][3]}")