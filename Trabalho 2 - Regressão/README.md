# Instruções

- Baixe os arquivos de dados do projeto, disponíveis na aba "Data", onde você encontrará também a descrição dos arquivos e o significado de todos os campos neles contidos.
- Implemente o pré-processamento adequado (tratamento de atributos categóricos, utilização de fatores de escala, etc.).
- Visualize, analise e selecione os atributos com maior potencial preditivo.
- Escolha os modelos preditivos de sua preferência e construa um script Python para testá-los.
- Verifique o desempenho dos modelos preditivos escolhidos por meio de validação cruzada, ou outra técnica de validação de sua preferência, usando o conjunto de treinamento fornecido.
- Ajuste os hiperparâmetros e o conjunto de variáveis utilizadas pelo modelo preditivo, de modo a reduzir o erro obtido na validação cruzada.
- Quando estiver satisfeito com o ajuste, treine o seu modelo preditivo usando o conjunto de treinamento completo, obtenha a previsão do modelo para o conjunto de teste fornecido e submeta ao Kaggle (que detém o gabarito oculto do conjunto de teste), para verificar o desempenho real do seu modelo preditivo.
- Revise e repita os passos anteriores quantas vezes achar necessário, até ficar satisfeito com o resultado.
- Escreva um relatório descrevendo todos os passos do seu trabalho (pré-processamento dos dados, seleção dos atributos, modelos preditivos experimentados e seus respectivos ajustes de hiperparâmetros, técnicas de validação utilizadas, resultados intermediários alcançados, etc.).
- Envie um e-mail para o professor (heraldo@poli.ufrj.br) contendo:
  - o seu id no Kaggle
  - o código-fonte utilizado (para possibilitar a reprodução dos resultados relatados)
  - o seu relatório (o relatório poderá ser entregue em um arquivo separado no formato PDF, ou integrado no próprio código-fonte, caso seja utilizado Jupyter Notebook ou Google Colab).

# Dataset Description

Trata-se de um conjunto de dados contendo informações a respeito de 6683 imóveis residenciais de uma cidade brasileira, coletados de ofertas de venda publicadas em site especializado. São fornecidos um conjunto de treinamento, um conjunto de teste e um exemplo de arquivo de submissão de resposta, todos em formato CSV.

No conjunto de treinamento, composto por 4683 imóveis, são fornecidas 20 características de cada imóvel, acompanhadas do preço de venda. No conjunto de teste, composto pelos 2000 imóveis restantes, são fornecidas somente as características do imóvel, cabendo ao competidor estimar o preço de venda.

## Arquivos Fornecidos

- conjunto_de_treinamento.csv: dados para treinamento (características dos imóveis e respectivos preços)
- conjunto_de_teste.csv: dados para teste (somente as características dos imóveis)
- exemplo_arquivo_respostas.csv: exemplo de arquivo para submissão das respostas (preços estimados para o conjunto de teste)

## Descrição dos Campos

- Id: identificação única do imóvel
- tipo: tipo de imóvel (apartamento, casa, loft ou quitinete)
- bairro: nome do bairro onde o imóvel se localiza
- tipo_vendedor: tipo de vendedor (imobiliária ou pessoa física)
- quartos: número de quartos
- suites: número de suítes
- vagas: número de vagas de garagem
- area_util: área útil, em metros quadrados
- area_extra: área extra, em metros quadrados
- diferenciais: descrição textual das duas principais características que diferenciam o imóvel
- churrasqueira: o anúncio menciona churrasqueira (1 = menciona ; 0 = não menciona)
- estacionamento: o anúncio menciona estacionamento para visitantes (1 = menciona ; 0 = não menciona)
- piscina: o anúncio menciona piscina (1 = menciona ; 0 = não menciona)
- playground: o anúncio menciona playground (1 = menciona ; 0 = não menciona)
- quadra: o anúncio menciona quadra esportiva ou campo de futebol (1 = menciona ; 0 = não menciona)
- s_festas: o anúncio menciona salão de festas (1 = menciona ; 0 = não menciona)
- s_jogos: o anúncio menciona salão de jogos (1 = menciona ; 0 = não menciona)
- s_ginastica: o anúncio menciona sala de ginástica (1 = menciona ; 0 = não menciona)
- sauna: o anúncio menciona sauna (1 = menciona ; 0 = não menciona)
- vista_mar: o anúncio menciona vista para o mar (1 = menciona ; 0 = não menciona)
- preco: preço de venda (valor a ser estimado, informado apenas no conjunto de treinamento)

Obs: Os 10 campos seguintes ao campo "diferenciais" se referem à existência ou não de determinadas palavras ou expressões na descrição textual contida nesse campo.
