import streamlit as st

st.title("Tabla de Multiplicar")

numero = st.number_input("Ingresa un número", min_value=1, step=1)

if st.button("Generar tabla"):
    st.write(f"### Tabla del {numero}")
    
    i = 1
    while i <= 10:
        resultado = numero * i
        st.write(f"{numero} x {i} = {resultado}")
        i += 1