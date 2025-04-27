# Análise de Printabilidade de Biomateriais - Prova de Conceito

Este projeto tem como objetivo prever automaticamente o "printabilidade score" de amostras de biomateriais impressos em 3D a partir de imagens, utilizando redes neurais convolucionais (CNNs) com TensorFlow/Keras.

## Como usar

### 1. Acesse o Google Colab

Clique no link abaixo para abrir o notebook de análise:

> [🔗 Abrir no Google Colab](https://colab.research.google.com/drive/1fj3Lq4Kldte4dZBxzvhAABXbBwRNgMIu?usp=sharing)

### 2. Execute o notebook

Ao executar o notebook, ele realizará automaticamente as seguintes etapas:

- Carregará o modelo de previsão treinado diretamente do Google Colab.
- A imagem de exemplo será carregada automaticamente para o teste.
- O "printabilidade score" da imagem de exemplo será calculado e exibido.
- Ao final da execução, o modelo treinado será salvo como um arquivo `.keras` e a imagem de exemplo estará disponível no formato `.png`, ambos no Colab. Caso queira, você pode baixar esses arquivos para o seu computador.

### 3. 3. Acesso ao código completo para criação e treinamento do modelo no GitHub

O código utilizado para criar e treinar o modelo está disponível neste repositório GitHub, em formato de notebook .ipynb. Este notebook contém todas as etapas do processo, incluindo a criação da arquitetura da rede neural convolucional, o treinamento e a avaliação do modelo. Ao acessar o código, você poderá visualizar os resultados do treinamento, como gráficos de desempenho.

## Observação

Este é um projeto de prova de conceito, baseado em imagens de um artigo científico. Futuramente, amostras reais de biomateriais, como acetato de celulose, serão utilizadas para treinar um modelo mais especializado.

## Licença

MIT License.
