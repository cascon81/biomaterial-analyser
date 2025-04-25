# 🧪 Biomaterial Analyser

Este projeto fornece um sistema de análise automática de imagens de biomateriais impressos em 3D, utilizando redes neurais convolucionais (CNNs) com TensorFlow/Keras para prever métricas de qualidade.  

Inclui neste repositório:

- ✅ **Modelos `.keras`** treinados e prontos para uso
- 🧠 **Notebooks `.ipynb`** com todo o código necessário para rodar os modelos  
  *(basta abrir no GitHub e clicar em "Abrir no Colab")*
- 📸 **Imagens de referência** das amostras já impressas, para você testar os modelos com exemplos reais
- 🖨️ **Arquivos `.stl`** para impressão das amostras de teste

> ⚠️ Embora desenvolvido para biomateriais, o sistema também funciona com outros filamentos como **ABS**, **PLA**, **PETG**, entre outros.

---

## 📊 Análises disponíveis

Cada métrica tem um modelo, uma imagem de referência e uma geometria `.stl` dedicada para testes:

| Métrica                    | Modelo (.keras)        | Imagem de amostra (.jpg)    | Geometria de teste (.stl)      |
|---------------------------|------------------------|------------------------------|--------------------------------|
| **Uniformidade do filamento** | [modelo_uniformidade.keras]() | [sample_uniformidade.jpg]()     | [uniformidade_teste.stl]()      |
| **Fusão entre filamentos**   | [modelo_fusao.keras]()        | [sample_fusao.jpg]()            | [fusao_teste.stl]()             |
| **Printabilidade geral**     | [modelo_printabilidade.keras]() | [sample_printabilidade.jpg]()   | [printabilidade_teste.stl]()    |

---

## 🚀 Como testar o modelo

1. Abra o arquivo `.ipynb` correspondente no GitHub.
2. Clique em **"Abrir no Colab"** (aparece automaticamente no topo da visualização do notebook).
3. Execute as células do notebook – o modelo será carregado automaticamente.
4. Faça upload da **imagem de amostra** incluída no repositório para simular a predição.

> Você também pode usar **suas próprias imagens** de peças impressas seguindo as orientações abaixo.

---

## 🧩 Teste sua impressora 3D

Quer avaliar a qualidade da sua impressora 3D?

1. Escolha uma das métricas e baixe o `.stl` correspondente.
2. Imprima a amostra com seu material (biomaterial, PLA, ABS, etc.).
3. Fotografe a amostra em boa iluminação, de forma similar à imagem de referência.
4. Use o notebook para analisar sua imagem com o modelo treinado.

> 📌 Os `.stl` foram projetados para destacar visualmente os aspectos mais relevantes de cada métrica. Usá-los é essencial para garantir previsões coerentes com o treinamento dos modelos.

---
