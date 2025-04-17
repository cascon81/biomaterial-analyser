# Classificador de Biomateriais com Streamlit e TensorFlow

Este projeto é uma aplicação web interativa desenvolvida com Streamlit, destinada à classificação automática de imagens de biomateriais utilizando um modelo de aprendizado profundo treinado com TensorFlow/Keras.

A aplicação permite o envio de imagens via navegador, processa essas imagens e exibe o resultado da previsão com base em um modelo `.h5` previamente treinado.

## Estrutura do Projeto

```
biomaterial-classifier/
│
├── app.py                  # Aplicação principal em Streamlit
├── modelo_biomaterial.h5   # Modelo treinado (arquivo gerado com TensorFlow/Keras)
├── requirements.txt        # Lista de dependências Python
└── README.md               # Este arquivo de instruções
```

## Pré-requisitos

- Python 3.8 ou superior
- streamlit, tensorflow, numpy, Pillow (instalados via requirements.txt)
- Um modelo Keras salvo no formato .h5 (ver detalhes abaixo)

## Instruções para uso local

1. Clone este repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/seu-usuario/biomaterial-classifier.git
   cd biomaterial-classifier
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Adicione o seu modelo `.h5` com o nome `modelo_biomaterial.h5` na mesma pasta do arquivo `app.py`.

4. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

## Instruções para uso na nuvem (Streamlit Cloud)

1. Crie um repositório no GitHub com os arquivos:
   - app.py
   - modelo_biomaterial.h5
   - requirements.txt
   - README.md

2. Acesse: https://streamlit.io/cloud

3. Conecte sua conta do GitHub e selecione o repositório.

4. Defina:
   - Arquivo principal: app.py
   - Branch principal: main

5. Clique em "Deploy" e aguarde a instalação e execução automática.

## Sobre o arquivo modelo_biomaterial.h5

Este arquivo é um modelo de deep learning treinado com TensorFlow/Keras. Ele deve:

- Aceitar como entrada uma imagem com shape (128, 128, 3)
- Estar salvo usando model.save('modelo_biomaterial.h5')
- Ter uma camada de saída compatível com seu problema:
  - Classificação binária: Dense(1, activation='sigmoid')
  - Classificação multi-classe: Dense(n_classes, activation='softmax')
