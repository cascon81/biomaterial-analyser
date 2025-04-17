import streamlit as st
from PIL import Image
import torch
import os
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

        # Seleção do modelo
        model_map = {
            "Uniformidade do filamento": "uniformity_yolo.pt",
            "Fusão dos filamentos": "fusion_yolo.pt",
            "Printabilidade geral": "printability_yolo.pt"
        }
        model_path = Path("models") / model_map[teste]

        # Processar imagem
        with st.spinner("🔎 Processando imagem com o modelo..."):
            model = torch.hub.load("ultralytics/yolov5", "custom", path=str(model_path), force_reload=True)
            results = model(image_path)

            save_dir = f"runs/detect/{teste.replace(' ', '_').lower()}"
            results.save(save_dir=save_dir)

            resultado_path = os.path.join(save_dir, os.path.basename(image_path))

        # Exibir resultado
        st.success("✅ Análise concluída!")
        st.image(resultado_path, caption="Resultado da análise", use_column_width=True)

        # Simular valor e erro
        resultado_valor = round(float(torch.rand(1)), 2)
        erro = round(float(torch.rand(1) * 0.1), 2)
        st.markdown(f"**🔢 Resultado do teste:** `{resultado_valor}` ± `{erro}`")

        # Botão para baixar
        with open(resultado_path, "rb") as f:
            st.download_button("📅 Baixar imagem com resultado", f, file_name="resultado_analise.png", mime="image/png")

        # Limpar imagem temporária
        os.remove(image_path)
