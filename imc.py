import streamlit as st

st.title("Calculadora de IMC")

peso = st.number_input("Ingresa tu peso en kilogramos", min_value=1.0)
altura = st.number_input("Ingresa tu altura en metros (ejemplo: 1.65)", min_value=0.1)

if st.button("Calcular IMC"):
    imc = peso / (altura ** 2)
    
    st.write(f"Tu IMC es: {imc:.2f}")
    
    if imc < 18.5:
        st.warning("Clasificación: Bajo peso")
    elif imc < 24.9:
        st.success("Clasificación: Peso normal")
    elif imc < 29.9:
        st.warning("Clasificación: Sobrepeso")
    else:
        st.error("Clasificación: Obesidad")
        