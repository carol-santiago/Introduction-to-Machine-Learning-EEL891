# Instruções

1. Baixe os arquivos de dados do projeto, disponíveis na aba "Data", onde você encontrará também a descrição dos arquivos e o significado de todos os campos neles contidos.
2. Implemente o pré-processamento adequado (tratamento de atributos categóricos, utilização de fatores de escala, etc.).
3. Visualize, analise e selecione os atributos com maior potencial preditivo.
4. Escolha os modelos preditivos de sua preferência e construa um script Python para testá-los.
5. Verifique o desempenho dos modelos preditivos escolhidos por meio de validação cruzada, ou outra técnica de validação de sua preferência, usando o conjunto de treinamento fornecido.
6. Ajuste os hiperparâmetros e o conjunto de variáveis utilizadas pelo modelo preditivo, de modo a reduzir o erro obtido na validação cruzada.
7. Quando estiver satisfeito com o ajuste, treine o seu modelo preditivo usando o conjunto de treinamento completo, obtenha a previsão do modelo para o conjunto de teste fornecido e submeta ao Kaggle (que detém o gabarito oculto do conjunto de teste), para verificar o desempenho real do seu modelo preditivo.
8. Revise e repita os passos anteriores quantas vezes achar necessário, até ficar satisfeito com o resultado.

Escreva um relatório descrevendo todos os passos do seu trabalho (pré-processamento dos dados, seleção dos atributos, modelos preditivos experimentados e seus respectivos ajustes de hiperparâmetros, técnicas de validação utilizadas, resultados intermediários alcançados, etc.).

Envie um e-mail para o professor (heraldo@poli.ufrj.br) contendo:

- O seu id no Kaggle
- O código-fonte utilizado (para possibilitar a reprodução dos resultados relatados)
- O seu relatório (o relatório poderá ser entregue em um arquivo separado no formato PDF, ou integrado no próprio código-fonte, caso seja utilizado Jupyter Notebook, Kaggle Notebook ou Google Colab).

# Dataset Description

## Arquivos Fornecidos

- conjunto_de_treinamento.csv: dados históricos fornecidos para treinamento de modelos preditivos. Este arquivo contém 20.000 amostras de solicitações de crédito com id do solicitante, dados da solicitação e desfecho do contrato (dívida quitada ou inadimplência).
- conjunto_de_teste.csv: dados históricos que serão usados na competição para verificar e comparar o desempenho dos modelos preditivos construídos pelos competidores. Este arquivo contém 5.000 amostras de solicitações de crédito (diferentes das fornecidas no conjunto de treinamento) com o id do solicitante e os dados da solicitação, mas sem o desfecho do contrato, que é a variável-alvo a ser respondida pelo modelo preditivo.
- exemplo_arquivo_respostas.csv: exemplo de arquivo de respostas para envio (submission). Este arquivo deve conter o desfecho predito pelo modelo para cada uma das 5.000 amostras do conjunto de teste.
- dicionario_de_dados.xlsx: planilha Excel contendo a descrição de todos os campos existentes nos arquivos CSV acima.
