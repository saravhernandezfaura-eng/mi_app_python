import streamlit as st

st.title("Calculadora de Factorial")

numero = st.number_input("Ingresa un número", min_value=0, step=1)

if st.button("Calcular Factorial"):
    resultado = 1
    operacion = ""
    
    if numero == 0:
        st.write("El factorial de 0 es: 1")
    else:
        for i in range(numero, 0, -1):
            resultado *= i
            if operacion == "":
                operacion = str(i)
            else:
                operacion += f" x {i}"
        
        st.write(f"{numero}! = {operacion} = {resultado}")