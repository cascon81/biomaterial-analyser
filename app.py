import streamlit as st
from PIL import Image
import torch
import os
from pathlib import Path

# Título bonito
st.set_page_config(page_title="Analisador de Bioimpressibilidade", layout="centered")
st.title("🔬 Analisador de Bioimpressibilidade")
st.markdown("""
Envie uma imagem de uma impressão e selecione os critérios que deseja analisar.
O sistema usa modelos treinados com YOLOv5 para realizar a detecção de padrões.
""")

# Upload de imagem
uploaded_file = st.file_uploader("📤 Envie sua imagem", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Imagem Original", use_column_width=True)
    image_path = f"temp_image.{uploaded_file.name.split('.')[-1]}"
    image.save(image_path)

    # Seleção de modelos
    st.markdown("### Selecione os aspectos que deseja analisar:")
    use_uniformity = st.checkbox("🧵 Uniformidade do filamento")
    use_fusion = st.checkbox("🔗 Fusão dos filamentos")
    use_printability = st.checkbox("🖨️ Printabilidade geral")

    run_button = st.button("🔍 Rodar análise")

    if run_button:
        models_dir = Path("models")
        results_dict = {}

        with st.spinner("⏳ Analisando..."):
            if use_uniformity:
                model_path = models_dir / "uniformity_yolo.pt"
                model = torch.hub.load("ultralytics/yolov5", "custom", path=str(model_path), force_reload=True)
                results = model(image_path)
                results.save(save_dir="runs/detect/uniformity")
                results_dict["Uniformidade"] = "runs/detect/uniformity/" + os.path.basename(image_path)

            if use_fusion:
                model_path = models_dir / "fusion_yolo.pt"
                model = torch.hub.load("ultralytics/yolov5", "custom", path=str(model_path), force_reload=True)
                results = model(image_path)
                results.save(save_dir="runs/detect/fusion")
                results_dict["Fusão"] = "runs/detect/fusion/" + os.path.basename(image_path)

            if use_printability:
                model_path = models_dir / "printability_yolo.pt"
                model = torch.hub.load("ultralytics/yolov5", "custom", path=str(model_path), force_reload=True)
                results = model(image_path)
                results.save(save_dir="runs/detect/printability")
                results_dict["Printabilidade"] = "runs/detect/printability/" + os.path.basename(image_path)

        st.success("✅ Análise concluída!")
        st.markdown("---")

        for nome, resultado in results_dict.items():
            st.markdown(f"### Resultado - {nome}")
            st.image(resultado, caption=f"{nome} - Resultado", use_column_width=True)

        # Limpeza (opcional)
        os.remove(image_path)
else:
    st.info("👆 Envie uma imagem acima para começar.")