import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.title("Classificador de Biomateriais")

uploaded_file = st.file_uploader("Envie uma imagem", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file).resize((128, 128))
    st.image(image, caption="Imagem carregada", use_column_width=True)

    model = tf.keras.models.load_model("modelo_biomaterial.h5")
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    st.write(f"Resultado da predição: {prediction}")
