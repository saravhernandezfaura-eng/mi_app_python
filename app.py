import streamlit as st

st.title("Mis Aplicaciones Python")

pagina = st.selectbox("Selecciona una aplicación", [
    "Inicio",
    "Clasificador de números",
    "Calculadora de IMC",
    "Factorial",
    "Tabla de multiplicar"
])

if pagina == "Clasificador de números":
    exec(open("numeros.py").read())
elif pagina == "Calculadora de IMC":
    exec(open("imc.py").read())
elif pagina == "Factorial":
    exec(open("factorial.py").read())
elif pagina == "Tabla de multiplicar":
    exec(open("tabla_multiplicar.py").read())
else:
    st.write("👈 Selecciona una aplicación del menú para comenzar")
    

