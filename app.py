import streamlit as st
from PIL import Image
import torch

# Função para carregar o modelo YOLO (substitua com o código de carregamento adequado)
@st.cache_resource
def load_model(model_name):
    # Carrega o modelo YOLO treinado correspondente ao teste selecionado
    model_path = f"models/{model_name}.pt"
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    return model

# Função para realizar a análise da imagem (substitua com a lógica de inferência do modelo)
def analyze_image(model, image):
    # Realiza a análise no modelo e retorna os resultados
    results = model(image)
    return results

# Título e descrição da aplicação
st.title("Classificador de Biomateriais")
st.write("""
Esta aplicação web permite a análise de biomateriais impressos em 3D. Utilizamos modelos YOLO treinados para classificar imagens de biomateriais com base em diferentes testes:
- **Uniformidade do Filamento**
- **Fusão dos Filamentos**
- **Printabilidade**
""")

# Exibição de informações sobre os biomateriais
with st.expander("Sobre os Biomateriais e os Testes"):
    st.write("""
    Os modelos YOLO foram treinados com os seguintes biomateriais:
    - **Alginate**
    - **Alginate + CaCl2**
    - **GelMA**
    - **Pluronic F-127**

    Esses modelos podem ser usados para materiais com comportamentos semelhantes, como acetato de celulose.
    """)

# Carregar a imagem
st.header("Faça o Upload de uma Imagem")
uploaded_file = st.file_uploader("Escolha uma imagem de biomaterial", type=["jpg", "png", "jpeg"])

# Seleção do tipo de análise
analysis_option = st.selectbox("Escolha o tipo de análise", ["Filament Uniformity Test", "Filament Fusion Test", "Printability Test"])

# Botão para iniciar a análise
if uploaded_file is not None:
    # Exibe a imagem carregada
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem carregada", use_column_width=True)
    
    # Carregar o modelo adequado com base na análise selecionada
    if analysis_option == "Filament Uniformity Test":
        model = load_model("uniformity_yolo")
    elif analysis_option == "Filament Fusion Test":
        model = load_model("fusion_yolo")
    else:
        model = load_model("printability_yolo")
    
    # Processamento da imagem e exibição dos resultados
    if st.button("Analisar Imagem"):
        st.write("Processando a imagem...")
        results = analyze_image(model, image)
        st.write("Resultados da análise:")
        st.write(results.pandas().xywh)  # Exibe os resultados da detecção em formato pandas
        st.image(results.render()[0], caption="Resultado da análise", use_column_width=True)
