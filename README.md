# 🧪 Biomaterial Analyser

Este projeto fornece um sistema de análise automática de imagens de biomateriais impressos em 3D, utilizando redes neurais convolucionais (CNNs) para regressão com TensorFlow/Keras. Os modelos `.keras`, notebooks `.ipynb` e arquivos de geometria `.stl` estão todos incluídos neste repositório.

> ℹ️ **Observação:** Embora o foco seja em biomateriais, os modelos também funcionam para outros materiais comuns de impressão 3D, como **ABS**, **PLA**, **PETG**, entre outros.

---

## 📊 Análises disponíveis

Cada métrica possui:
- Um modelo `.keras` treinado com imagens reais
- Um notebook `.ipynb` para execução no Google Colab
- Um arquivo `.stl` com geometria específica de teste
- Uma imagem de amostra para referência

| Métrica                     | Notebook (.ipynb)             | Modelo + Imagem (.keras)                        | Geometria de Teste (.stl)         |
|----------------------------|-------------------------------|-------------------------------------------------|------------------------------------|
| **Uniformidade do filamento** | `uniformidade_filamento.ipynb` | `modelo_uniformidade.keras` + `sample_uniformidade.jpg` | `uniformidade_teste.stl` |
| **Fusão entre filamentos**   | `fusao_filamentos.ipynb`        | `modelo_fusao.keras` + `sample_fusao.jpg`         | `fusao_teste.stl`         |
| **Printabilidade geral**     | `printabilidade_geral.ipynb`     | `modelo_printabilidade.keras` + `sample_printabilidade.jpg` | `printabilidade_teste.stl` |

---

## 🚀 Como usar

1. Abra o notebook correspondente no Google Colab.
2. Faça upload da imagem da amostra impressa (semelhante à imagem exemplo).
3. Execute o modelo para obter o resultado da análise.

> ⚠️ **Atenção:** utilize a geometria `.stl` correspondente a cada análise para garantir resultados confiáveis.

---

## 🧩 Teste sua impressora 3D

Quer verificar a performance da sua impressora 3D?

- Baixe o arquivo `.stl` da análise desejada
- Imprima a amostra com seu material preferido
- Fotografe de forma semelhante à imagem de exemplo
- Submeta a imagem no notebook correspondente

Compare os resultados com o desempenho ideal esperado!

---
