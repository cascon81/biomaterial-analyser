# 🧪 Biomaterial Analyser

Este projeto fornece um sistema de **análise automática de imagens de biomateriais impressos em 3D**, utilizando redes neurais convolucionais (CNNs) com TensorFlow/Keras para prever métricas de qualidade.

## 📦 Conteúdo deste repositório

- ✅ **Modelos `.keras` e `.h5`** prontos para uso (opcional)
- 🧠 **Notebooks `.ipynb`** com todo o código necessário para rodar as análises
- 📸 **Imagens de referência** para testes com exemplos reais
- 🏷️ **Labels** para auxiliar no treinamento e validação dos modelos
- 🖨️ **Arquivos `.stl`** para impressão das geometrias de teste (opcional)

> ⚠️ Embora desenvolvido para biomateriais, o sistema também é compatível com filamentos como **ABS**, **PLA**, **PETG**, entre outros.

---

## 📊 Análises disponíveis

Cada métrica possui uma imagem de referência (`.png`) e, opcionalmente, um modelo (`.keras` ou `.h5`), labels e uma geometria de teste (`.stl`). Esses arquivos estão organizados por métrica nas pastas abaixo:

| Métrica                   | Pasta com os Arquivos |
|---------------------------|------------------------|
| **Uniformidade do filamento** | [🔗 Acessar pasta](https://exemplo.com/uniformidade) |
| **Fusão entre filamentos**    | [🔗 Acessar pasta](https://exemplo.com/fusao)        |
| **Printabilidade geral**      | [🔗 Acessar pasta](https://exemplo.com/printabilidade) |

> 📁 Cada pasta contém:
> - Imagem de referência (`.png`)  
> - Modelo de predição (`.keras` ou `.h5`) – **opcional**  
> - Geometria de teste (`.stl`) – **opcional**  
> - Labels (`.csv` ou `.json`) – **opcional**

> 💡 **Você só precisa do `.keras` ou `.h5` se for rodar localmente. No Colab, ele é carregado automaticamente.**  
> Use o `.stl` apenas se quiser **testar a sua própria impressora 3D**.

---

## 🚀 Como testar os modelos no Google Colab

1. Abra o arquivo `.ipynb` correspondente neste repositório.
2. Ao abrir o arquivo `.ipynb`, você verá um exemplo de execução que foi rodado por mim, com as imagens de teste incluídas no repositório.
3. Clique em **“Abrir no Colab”** (botão exibido automaticamente no topo).
4. Execute as células – o modelo será carregado automaticamente.
5. Você pode rodar a análise com uma imagem da pasta de imagens de referência ou **fazer upload da sua própria imagem** para realizar a predição.

---

## 🧩 Teste sua impressora 3D (opcional)

Deseja avaliar a performance da sua impressora?

1. Escolha uma métrica e baixe o `.stl` correspondente.
2. Imprima a amostra com o material desejado.
3. Fotografe a peça em boa iluminação, em ângulo semelhante à imagem de referência.
4. Use o notebook para analisar a imagem.

> 📌 Os arquivos `.stl` foram projetados para realçar os aspectos específicos de cada métrica. Usá-los garante previsões mais alinhadas ao treinamento do modelo.

---

## 🔁 Evolução do Modelo

O sistema foi desenvolvido para ser **modular e adaptável**. Com isso, você pode:

- **Rotular automaticamente novas imagens** de amostras, enviando pastas com imagens de materiais diferentes.
- **Treinar novamente os modelos** com imagens de **outros materiais ou configurações de impressão**.
- **Aprimorar a especialização** do modelo em um tipo de falha, material ou equipamento específico.
- **Criar novas métricas ou adaptações** para sua própria realidade.

> **Como funciona**: Se você enviar algumas imagens de materiais diferentes, o modelo irá rotulá-las automaticamente. Essas imagens rotuladas podem ser usadas para **criar um novo modelo especializado** ou para **refinar o modelo existente** para que ele se torne mais eficiente em reconhecer o material específico.

> Com mais exemplos e ajustes finos, o modelo pode se tornar um **verdadeiro especialista** em **avaliar impressões de seu processo ou material específico**.

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
