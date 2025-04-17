# biomaterial-analyser

Este projeto fornece uma aplicação web interativa para classificar imagens de biomateriais utilizando modelos YOLO treinados. O classificador é acessível diretamente via **Streamlit** e **Vercel**, permitindo a análise de biomateriais impressos em 3D para testes como **uniformidade do filamento**, **fusão dos filamentos** e **printabilidade**.

---

## 🚀 Como usar online

1. **Acesse a aplicação online**:

Clique no link abaixo para acessar:

[**Acessar biomaterial-analyser**](https://biomaterial-classifier.streamlit.app/)

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

---

📐 Cada teste requer uma **amostra física com formato específico**, projetada para evidenciar as características visuais que o modelo deve analisar. Por isso, **cada teste deve ser feito com uma peça diferente**, impressa com base em um design otimizado para aquele tipo de avaliação. Abaixo estão os modelos utilizados em cada teste, com links para baixar o arquivo STL ou GCODE correspondente:

- [Amostra de Uniformidade](https://drive.google.com/your-uniformity-link) – formato com linhas paralelas para avaliar variações no diâmetro.
- [Amostra de Fusão](https://drive.google.com/your-fusion-link) – estrutura em grelha para detectar falhas de fusão entre extrusões.
- [Amostra de Printabilidade](https://drive.google.com/your-printability-link) – padrão com curvas e ângulos variados para testar a capacidade de impressão precisa.

Você pode baixar e imprimir essas amostras com sua bioimpressora antes de realizar a análise com a aplicação.


