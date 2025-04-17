import streamlit as st
from PIL import Image
import torch
import os
from pathlib import Path

st.set_page_config(page_title="Analisador de Bioimpressibilidade", layout="centered")
st.title("🧪 Analisador de Amostras Impressas")

st.markdown("""
Envie a imagem da **amostra** e selecione o **teste específico** que deseja realizar:

⚠️ Cada teste possui um padrão distinto, portanto **cada amostra deve ser única** e correspondente ao teste escolhido.
""")

uploaded_file = st.file_uploader("📤 Enviar imagem da amostra", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem da amostra", use_column_width=True)
    image_path = f"temp_image.{uploaded_file.name.split('.')[-1]}"
    image.save(image_path)

    teste = st.selectbox("🔍 Escolha o teste a realizar", [
        "Uniformidade do filamento",
        "Fusão dos filamentos",
        "Printabilidade geral"
    ])

    if st.button("▶️ Analisar"):
        st.spinner("Processando...")

        model_map = {
            "Uniformidade do filamento": "uniformity_yolo.pt",
            "Fusão dos filamentos": "fusion_yolo.pt",
            "Printabilidade geral": "printability_yolo.pt"
        }

        model_path = Path("models") / model_map[teste]
        model = torch.hub.load("ultralytics/yolov5", "custom", path=str(model_path), force_reload=True)
        results = model(image_path)

        save_dir = f"runs/detect/{teste.replace(' ', '_').lower()}"
        results.save(save_dir=save_dir)

        st.success("✅ Análise concluída!")
        st.image(os.path.join(save_dir, os.path.basename(image_path)), caption="Resultado", use_column_width=True)

        os.remove(image_path)
else:
    st.info("👆 Envie uma imagem acima para iniciar.")
