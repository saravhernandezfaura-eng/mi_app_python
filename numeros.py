import streamlit as st

st.title("Clasificador de números")

numero = st.number_input("Ingresa un número", step=0.1)

if st.button("Clasificar"):
    if numero > 0:
        st.success("El número es positivo")
    elif numero < 0:
        st.error("El número es negativo")
    else:
        st.warning("El número es cero")