import streamlit as st

st.set_page_config(
    page_title="Organização das sugestões",
    page_icon="📟",
)

# Cria duas colunas lado a lado
col1, col2 = st.columns([1, 4])  # Ajuste os números para controlar a largura relativa

# Coluna da imagem
with col1:
    st.image("pages/nps.webp.jpg", width=100)  # Substitua pelo caminho da sua imagem

# Coluna do título
with col2:
    st.title("Calculadora de NPS")

# Inputs
col1, col2, col3 = st.columns(3)
with col1:
    promotores = st.number_input("Promotores", min_value=0, value=0)
with col2:
    neutros = st.number_input("Neutros", min_value=0, value=0)
with col3:
    detratores = st.number_input("Detratores", min_value=0, value=0)

total_respostas = promotores + neutros + detratores

if total_respostas == 0:
    st.warning("Insira pelo menos uma resposta para calcular o NPS.")
else:
    # Cálculo de porcentagens
    pct_promotores = promotores / total_respostas
    pct_detratores = detratores / total_respostas
    nps = (pct_promotores - pct_detratores) * 100

    # Formatação de sinais
    sinal_prom = "+" if pct_promotores > 0 else ""
    sinal_detr = "-" if pct_detratores > 0 else ""

    # Exibição
    st.markdown("### Resultados:")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success(f"Promotores: {sinal_prom}{pct_promotores:.1%}")
    with col2:
        st.info(f"Neutros: {neutros / total_respostas:.1%}")
    with col3:
        st.error(f"Detratores: {sinal_detr}{pct_detratores:.1%}")

    # Exibe o NPS final
    st.markdown("---")
    cor = "🟢" if nps > 0 else "🔴" if nps < 0 else "⚪"
    st.metric(label="**NPS Atual**", value=f"{nps:.1f}", delta=f"{nps:.1f}", delta_color="normal")
    st.markdown(f"{cor} NPS")

   
st.caption("Desenvolvido por Joenice Almeida")
st.caption("10/07/2025")


