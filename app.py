import streamlit as st
from PIL import Image
import os
import gdown
import tensorflow as tf
import numpy as np

from pathlib import Path

# Seleção do modelo
model_map = {
    "Uniformidade do filamento": ("uniformity_model.h5", "1RcS2LCAAKrUpp4An5tR5Z0VFSuYrJcdr"),  # Exemplo: mesmo modelo para todos
    "Fusão dos filamentos": ("fusion_model.h5", "1RcS2LCAAKrUpp4An5tR5Z0VFSuYrJcdr"),
    "Printabilidade geral": ("printability_model.h5", "1RcS2LCAAKrUpp4An5tR5Z0VFSuYrJcdr")
}

model_filename, drive_id = model_map[teste]
model_path = Path("models") / model_filename

# Baixar o modelo se necessário
if not model_path.exists():
    st.info(f"⬇️ Baixando modelo `{model_filename}` do Google Drive...")
    os.makedirs("models", exist_ok=True)
    url = f"https://drive.google.com/uc?id={drive_id}"
    gdown.download(url, str(model_path), quiet=False)

        # Pré-processar a imagem
        img_resized = image.resize((224, 224))  # ajuste para o input do seu modelo
        img_array = np.array(img_resized) / 255.0
        if img_array.shape[-1] == 4:  # remover canal alpha se necessário
            img_array = img_array[:, :, :3]
        img_batch = np.expand_dims(img_array, axis=0)

        # Carregar modelo
        model = tf.keras.models.load_model(model_path)

        with st.spinner("🔎 Processando imagem com o modelo..."):
            prediction = model.predict(img_batch)[0][0]  # ajusta conforme a saída do seu modelo

        # Mostrar resultado
        st.success("✅ Análise concluída!")
        st.markdown(f"**🔢 Resultado do teste:** `{round(float(prediction), 2)}`")
