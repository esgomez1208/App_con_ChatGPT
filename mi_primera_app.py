import streamlit as st

# Título y autor
st.title("Mi primera app")
st.write("Esta app fue elaborada por “Esteban Gómez Benítez”.")

# Pregunta al usuario por su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
