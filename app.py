import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os
import gdown

st.set_page_config(page_title="Analisador de Printabilidade", layout="centered")
st.title("🧪 Analisador de Printabilidade (.h5)")

# Verifica se o modelo já foi baixado, senão baixa do Google Drive
MODEL_PATH = "modelo_printabilidade.h5"
if not os.path.exists(MODEL_PATH):
    with st.spinner("⬇️ Baixando modelo de printabilidade..."):
        gdown.download(
            "https://drive.google.com/uc?id=1RcS2LCAAKrUpp4An5tR5Z0VFSuYrJcdr",
            MODEL_PATH,
            quiet=False,
        )

# Carrega o modelo
model = load_model(MODEL_PATH)

# Upload da imagem
uploaded_file = st.file_uploader("📷 Envie a imagem da amostra", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Imagem enviada", use_column_width=True)

    # Pré-processamento da imagem
    img_resized = image.resize((224, 224))  # ajuste conforme sua rede
    img_array = np.array(img_resized) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)

    # Predição
    if st.button("▶️ Analisar"):
        with st.spinner("🔎 Processando imagem..."):
            prediction = model.predict(img_batch)[0][0]
            st.success("✅ Análise concluída!")
            st.markdown(f"**Resultado da printabilidade:** `{prediction:.2f}`")
