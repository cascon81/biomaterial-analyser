# 🧪 Biomaterial Analyser

Este projeto fornece um sistema de **análise automática de imagens de biomateriais impressos em 3D**, utilizando redes neurais convolucionais (CNNs) com TensorFlow/Keras para prever métricas de qualidade.

## 📦 Conteúdo deste repositório

- ✅ **Modelos `.keras`** prontos para uso (opcional)
- 🧠 **Notebooks `.ipynb`** com todo o código necessário para rodar as análises
- 📸 **Imagens de referência** para testes com exemplos reais
- 🖨️ **Arquivos `.stl`** para impressão das geometrias de teste (opcional)

> ⚠️ Embora desenvolvido para biomateriais, o sistema também é compatível com filamentos como **ABS**, **PLA**, **PETG**, entre outros.

---

## 📊 Análises disponíveis

Cada métrica possui uma imagem de referência (`.png`) e, opcionalmente, um modelo (`.keras`) e uma geometria de teste (`.stl`).  
Esses arquivos estão organizados por métrica nas pastas abaixo:

| Métrica                   | Pasta com os Arquivos |
|---------------------------|------------------------|
| **Uniformidade do filamento** | [🔗 Acessar pasta](https://exemplo.com/uniformidade) |
| **Fusão entre filamentos**    | [🔗 Acessar pasta](https://exemplo.com/fusao)        |
| **Printabilidade geral**      | [🔗 Acessar pasta](https://exemplo.com/printabilidade) |

> 📁 Cada pasta contém:
> - Imagem de referência (`.png`)  
> - Modelo de predição (`.keras`) – **opcional**  
> - Geometria de teste (`.stl`) – **opcional**

> 💡 **Você só precisa do `.keras` se for rodar localmente. No Colab, ele é carregado automaticamente.**  
> Use o `.stl` apenas se quiser **testar a sua própria impressora 3D**.

---

## 🚀 Como testar os modelos no Google Colab

1. Abra o arquivo `.ipynb` correspondente neste repositório.
2. Clique em **“Abrir no Colab”** (botão exibido automaticamente no topo).
3. Execute as células – o modelo será carregado automaticamente.
4. Faça upload da **imagem de referência** ou de **sua própria imagem** para realizar a predição.

---

## 🧩 Teste sua impressora 3D (opcional)

Deseja avaliar a performance da sua impressora?

1. Escolha uma métrica e baixe o `.stl` correspondente.
2. Imprima a amostra com o material desejado.
3. Fotografe a peça em boa iluminação, em ângulo semelhante à imagem de referência.
4. Use o notebook para analisar a imagem.

> 📌 Os arquivos `.stl` foram projetados para realçar os aspectos específicos de cada métrica. Usá-los garante previsões mais alinhadas ao treinamento do modelo.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Abra uma issue com sugestões ou envie um pull request com melhorias, novos modelos ou métricas.

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
