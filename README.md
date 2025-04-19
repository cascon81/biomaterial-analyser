# 🧪 Biomaterial Analyser

Este projeto fornece um sistema de **análise automática de imagens de biomateriais impressos em 3D** utilizando **modelos de regressão treinados com TensorFlow/Keras**. O sistema é executado via **Google Colab**, com interface simples e intuitiva para carregar imagens e obter resultados.

---

## O que o sistema analisa?

Três tipos de análises estão disponíveis, cada uma com seu próprio modelo `.h5` e `.keras`:

- **Uniformidade do filamento**  
- **Fusão entre filamentos**  
- **Printabilidade geral**

Cada análise utiliza uma **geometria de amostra específica** com GCode dedicado, projetada para destacar as características visuais mais relevantes de cada métrica.


## 💻 Executar no Google Colab

Abra e execute diretamente no Colab com o link abaixo:

- [Uniformidade do filamento – Abrir no Colab](https://drive.google.com/...)  
- [Fusão entre filamentos – Abrir no Colab](https://drive.google.com/...)  
- [Printabilidade geral – Abrir no Colab]([https://drive.google.com/file/d/1RcS2LCAAKrUpp4An5tR5Z0VFSuYrJcdr/view?usp=drive_link](https://colab.research.google.com/drive/1fj3Lq4Kldte4dZBxzvhAABXbBwRNgMIu?usp=sharing))

Permite:
- Fazer o upload da imagem da amostra
- Executar a predição


## 📐 GCodes de Teste

Para garantir a análise correta, utilize as amostras de teste correspondentes a cada modelo:

- [Amostra de Uniformidade – GCODE](https://drive.google.com/...)  
- [Amostra de Fusão – GCODE](https://drive.google.com/...)  
- [Amostra de Printabilidade – GCODE](https://drive.google.com/...)

Essas geometrias foram projetadas para evidenciar visualmente as métricas que os modelos analisam.


## 🧠 Modelos Treinados (TensorFlow/Keras)

Os modelos foram treinados usando imagens rotuladas com valores contínuos (regressão).

- [Uniformidade do filamento – Download modelo `.h5`](https://drive.google.com/...)  
- [Fusão entre filamentos – Download modelo `.h5`](https://drive.google.com/...)  
- [Printabilidade geral – Download modelo `.h5`](https://drive.google.com/drive/folders/1cFIDD61-nRLunhnHf91oDYkNiv9yHJ5a?usp=sharing)


