# Dataset Description

## Arquivos Fornecidos

- conjunto_de_treinamento.csv: dados históricos fornecidos para treinamento de modelos preditivos. Este arquivo contém 20.000 amostras de solicitações de crédito com id do solicitante, dados da solicitação e desfecho do contrato (dívida quitada ou inadimplência).
- conjunto_de_teste.csv: dados históricos que serão usados na competição para verificar e comparar o desempenho dos modelos preditivos construídos pelos competidores. Este arquivo contém 5.000 amostras de solicitações de crédito (diferentes das fornecidas no conjunto de treinamento) com o id do solicitante e os dados da solicitação, mas sem o desfecho do contrato, que é a variável-alvo a ser respondida pelo modelo preditivo.
- exemplo_arquivo_respostas.csv: exemplo de arquivo de respostas para envio (submission). Este arquivo deve conter o desfecho predito pelo modelo para cada uma das 5.000 amostras do conjunto de teste.
- dicionario_de_dados.xlsx: planilha Excel contendo a descrição de todos os campos existentes nos arquivos CSV acima.
