import streamlit as st
from PIL import Image
import os
import gdown
import tensorflow as tf
import numpy as np
from pathlib import Path

# Configuração da página
st.set_page_config(page_title="Analisador de Bioimpressibilidade", layout="centered")
st.title("🧪 Analisador de Amostras Impressas")

# Instruções
st.markdown("""
### Escolha o tipo de teste que deseja realizar:
""")

# Menu de seleção
teste = st.selectbox("🔬 Selecione o teste desejado", [
    "Uniformidade do filamento",
    "Fusão dos filamentos",
    "Printabilidade geral"
])

# Upload da imagem
uploaded_file = st.file_uploader("📄 Enviar imagem da amostra", type=["png", "jpg", "jpeg"])

# Botão de gerar
gerar = st.button("▶️ Gerar resultado")

# Ação ao clicar no botão
if gerar:
    if not uploaded_file:
        st.warning("⚠️ Por favor, envie uma imagem para análise.")
    else:
        # Exibir imagem enviada
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem enviada", use_column_width=True)

        # Salvar temporariamente
        image_ext = uploaded_file.name.split('.')[-1]
        image_path = f"temp_image.{image_ext}"
        image.save(image_path)

        # Seleção do modelo e ID do Google Drive
        model_map = {
            "Uniformidade do filamento": ("uniformity_model.h5", "1RcS2LCAAKrUpp4An5tR5Z0VFSuYrJcdr"),
            "Fusão dos filamentos": ("fusion_model.h5", "1RcS2LCAAKrUpp4An5tR5Z0VFSuYrJcdr"),
            "Printabilidade geral": ("printability_model.h5", "1RcS2LCAAKrUpp4An5tR5Z0VFSuYrJcdr")
        }

        model_filename, drive_id = model_map[teste]
        model_path = Path("models") / model_filename

        # Baixar o modelo, se necessário
        if not model_path.exists():
            st.info(f"⬇️ Baixando modelo `{model_filename}` do Google Drive...")
            os.makedirs("models", exist_ok=True)
            url = f"https://drive.google.com/uc?id={drive_id}"
            gdown.download(url, str(model_path), quiet=False)

        # Pré-processar a imagem
        img_resized = image.resize((128, 128))
        img_array = np.array(img_resized) / 255.0
        if img_array.shape[-1] == 4:  # remover canal alpha, se existir
            img_array = img_array[:, :, :3]
        img_batch = np.expand_dims(img_array, axis=0)

        # Carregar modelo e prever
        with st.spinner("🔎 Processando imagem com o modelo..."):
            model = tf.keras.models.load_model(model_path)
            prediction = model.predict(img_batch)[0][0]

        # Mostrar resultado
        st.success("✅ Análise concluída!")
        st.markdown(f"**🔢 Resultado do teste:** `{round(float(prediction), 2)}`")

        # Botão para baixar imagem original
        with open(image_path, "rb") as f:
            st.download_button("📅 Baixar imagem enviada", f, file_name="amostra.png", mime="image/png")

        # Limpar imagem temporária
        os.remove(image_path)
