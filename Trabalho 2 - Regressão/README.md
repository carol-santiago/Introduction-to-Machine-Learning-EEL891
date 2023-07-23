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
