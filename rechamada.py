import streamlit as st

st.set_page_config(page_title="Calculadora de Melhoria de FCR", layout="centered")

st.title("📞 Calculadora de Melhoria de FCR (First Call Resolution)")

# Entradas do usuário
total = st.number_input("Total de chamadas recebidas", value=10000, step=100)
rechamadas = st.number_input("Total de rechamadas", value=2000, step=100)
melhoria = st.slider("Redução estimada nas rechamadas (%)", 0, 100, 10)

# Cálculos
resolvidas = total - rechamadas
fcr_atual = (resolvidas / total) * 100
rechamadas_apos_melhoria = rechamadas * (1 - melhoria / 100)
fcr_melhorado = ((total - rechamadas_apos_melhoria) / total) * 100

# Exibição
st.subheader("📊 Resultados")
st.metric("FCR Atual (%)", f"{fcr_atual:.2f}")
st.metric("FCR com melhoria simulada (%)", f"{fcr_melhorado:.2f}")
