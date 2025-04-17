import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Biomaterial Analyzer",
    layout="wide",
)

# ===== Título =====
st.title("🧪 Biomaterial Analyzer")
st.markdown("""
Este sistema utiliza **modelos treinados com YOLO** para analisar imagens de biomateriais impressos em 3D.  
Você pode escolher entre diferentes tipos de análise e receber uma avaliação automática do material analisado.

📌 **Os modelos foram treinados com os seguintes materiais**:
- Alginate
- Alginate + CaCl₂
- GelMA
- Nivea
- Pluronic F-127

⚠️ Portanto, os resultados são mais confiáveis com esses materiais ou com materiais com **comportamento semelhante**, como **acetato de celulose**.
""")

st.divider()

# ===== Análise rápida =====
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("🔍 Selecione o tipo de análise")

    analysis_type = st.radio(
        "Tipo de teste:",
        options=[
            "Filament Uniformity Test",
            "Filament Fusion Test",
            "Printability"
        ],
        index=0,
        horizontal=True,
    )

    if st.button("▶️ Rodar Análise"):
        st.success(f"✅ {analysis_type} finalizado com sucesso.")
        st.markdown("🔄 *Integração com o modelo YOLO em breve.*")

with col2:
    st.subheader("📁 Upload (em breve)")
    st.info("A função de upload será ativada na próxima versão. Aguarde!")

st.divider()

# ===== Detalhes técnicos =====
with st.expander("ℹ️ Mais informações sobre os testes"):
    st.markdown("""
### 📌 Descrição dos testes:

#### 🧵 Filament Uniformity Test
Avalia se os filamentos impressos possuem **largura uniforme**, indicando consistência do fluxo e precisão da extrusão.

#### 🔗 Filament Fusion Test
Detecta a **aderência entre camadas**, verificando se a fusão entre filamentos consecutivos está adequada para manter a integridade estrutural.

#### 🖨️ Printability
Verifica se o material apresenta **defeitos visuais ou estruturais** que comprometam a qualidade da impressão, como buracos, deslocamentos ou falhas na camada base.

---

### 🎯 Sobre os modelos
Cada tipo de teste utiliza um modelo **YOLO treinado especificamente** para aquela tarefa.  
Os modelos foram treinados com imagens rotuladas de biomateriais típicos usados em bioimpressão 3D.

### 🧪 Materiais usados no treinamento:
- **Alginate**
- **Alginate + CaCl₂**
- **GelMA**
- **Nivea (como controle de textura/padrão)**
- **Pluronic F-127**

Estes materiais cobrem uma variedade de **comportamentos reológicos e padrões de impressão** observados em biofabricação.
""")

