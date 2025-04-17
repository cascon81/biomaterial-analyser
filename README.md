# Classificador de Biomateriais com Streamlit e TensorFlow

Este projeto oferece uma aplicação web interativa desenvolvida com **Streamlit**, que permite a **classificação de imagens de biomateriais** utilizando um modelo treinado com **TensorFlow/Keras**. A ferramenta pode ser acessada diretamente na web, sem necessidade de instalação local.

---

## 🌐 Como usar online (Streamlit Cloud)

Siga estas etapas para usar a aplicação diretamente na web:

### 1. Acesse a aplicação online:

Clique no link abaixo para acessar a aplicação hospedada no **Streamlit Cloud**:

[**Acessar Classificador de Biomateriais**]([https://share.streamlit.io/seu-usuario/biomaterial-classifier/main/app.py](https://biomaterial-classifier.streamlit.app/))

### 2. Envie sua imagem:

No site, você pode **fazer o upload de uma imagem** de biomaterial (em formatos JPG, PNG ou JPEG). O modelo realizará a classificação automaticamente, exibindo o resultado na tela.

---

## 🍴 Como testar o modelo sozinho

Se você quiser testar o modelo em seu próprio Streamlit, ou fazer ajustes, você pode **fazer um fork** do repositório. O fork permite que você tenha sua própria cópia do projeto e possa modificá-lo para suas necessidades. Para isso, siga os passos:

### 1. Clique em **Fork** no canto superior direito da página do repositório.
### 2. Clone o repositório para sua máquina e rode a aplicação localmente, ou faça o deploy no **Streamlit Cloud**.

Isso permitirá que você utilize o modelo de classificação em suas próprias imagens e, se necessário, substitua o modelo `.h5` por outro treinado para diferentes tipos de biomateriais.

---

## 🤖 Sobre o modelo `.h5`

O modelo que acompanha o projeto foi treinado com **TensorFlow/Keras** para classificar imagens de biomateriais. O modelo `.h5` espera imagens com o formato **128x128 pixels** e 3 canais (RGB). O modelo foi treinado para **classificação binária** (por exemplo, "biomaterial A" vs "biomaterial B"), mas pode ser facilmente adaptado para outras tarefas de classificação.

### Adaptando para outros materiais

Caso você queira usar o modelo para classificar outros tipos de biomateriais, basta treinar um novo modelo com imagens do material desejado e salvar o modelo treinado no formato `.h5`. Substitua o arquivo `modelo_biomaterial.h5` pelo novo modelo e faça o upload das imagens correspondentes. O código da aplicação vai utilizar o novo modelo para a classificação automaticamente.

---

## 💡 Como treinar seu próprio modelo `.h5`

Se você deseja treinar um modelo para outro tipo de material, siga estas etapas:

1. Treine um modelo de classificação de imagens com **TensorFlow/Keras**.
2. Salve o modelo treinado com:
   ```python
   model.save("modelo_biomaterial.h5")
