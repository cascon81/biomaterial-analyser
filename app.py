import streamlit as st

# Configuração da página
st.set_page_config(page_title="Biomaterial Analyzer (Beta)", layout="centered")
st.title("🧪 Biomaterial Analyzer (Beta)")
st.markdown("Interface inicial para análise de biomateriais. Selecione uma análise e clique no botão para simular os resultados.")

# Seletor de tipo de análise
st.subheader("⚙️ Escolha a Análise")
analysis_type = st.radio(
    "Selecione o teste a ser executado:",
    options=[
        "Filament Uniformity Test",
        "Filament Fusion Test",
        "Printability"
    ]
)

# Botão para rodar análise
if st.button("🔍 Rodar Análise"):
    st.subheader("🔎 Resultado da Análise")

    if analysis_type == "Filament Uniformity Test":
        st.success("✅ Uniformidade: Alta. Filamentos com largura consistente ao longo da estrutura.")
    elif analysis_type == "Filament Fusion Test":
        st.success("✅ Fusão: Adequada. Boa aderência entre camadas detectada.")
    elif analysis_type == "Printability":
        st.success("✅ Printabilidade: Excelente. Estrutura bem definida, sem falhas visíveis.")
