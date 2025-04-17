# BioPrint Analyser

Este projeto fornece uma aplicação web interativa para classificar imagens de biomateriais utilizando modelos YOLO treinados. O classificador é acessível diretamente via **Streamlit** e **Vercel**, permitindo a análise de biomateriais impressos em 3D para testes como **uniformidade do filamento**, **fusão dos filamentos** e **printabilidade**.

---

## 🚀 Como usar online

1. **Acesse a aplicação online**:

Clique no link abaixo para acessar:

[**Acessar BioPrint Analyser**](https://biomaterial-classifier.streamlit.app/)

2. **Envie sua imagem**:

No site, você pode **fazer o upload de uma imagem** de biomaterial (em formatos JPG, PNG ou JPEG). O modelo realizará a classificação automaticamente, exibindo o resultado na tela.

---

## 🧠 Modelos Treinados

- **Filament Uniformity Test**: Uniformidade do filamento.
- **Filament Fusion Test**: Fusão dos filamentos.
- **Printability Test**: Avaliação da impressão do material.

Os modelos YOLO foram treinados com os seguintes biomateriais:

- Alginate
- Alginate + CaCl2
- GelMA
- Pluronic F-127

Esses modelos podem ser utilizados para materiais com comportamentos semelhantes, como acetato de celulose.
