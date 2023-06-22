# Comandos Úteis do Pandas para Análise de Dados

Aqui estão alguns comandos úteis do Pandas para análise de dados, que podem ser úteis para o seu trabalho atual. Lembre-se de importar o Pandas antes de utilizar os comandos.

## Leitura e Escrita de Dados

### Leitura de Dados

- `pd.read_csv('nome_do_arquivo.csv')`: Lê um arquivo CSV e retorna um DataFrame.
- `pd.read_excel('nome_do_arquivo.xlsx', sheet_name='nome_da_planilha')`: Lê um arquivo Excel e retorna um DataFrame.

### Escrita de Dados

- `df.to_csv('nome_do_arquivo.csv', index=False)`: Salva um DataFrame em um arquivo CSV.
- `df.to_excel('nome_do_arquivo.xlsx', sheet_name='nome_da_planilha', index=False)`: Salva um DataFrame em um arquivo Excel.

## Manipulação de DataFrame

### Visualização dos Dados

- `df.head()`: Retorna as primeiras linhas do DataFrame.
- `df.tail()`: Retorna as últimas linhas do DataFrame.
- `df.shape`: Retorna o número de linhas e colunas do DataFrame.
- `df.columns`: Retorna os nomes das colunas do DataFrame.
- `df.info()`: Retorna informações sobre o DataFrame, como tipo de dados e quantidade de valores não nulos.

### Seleção de Colunas

- `df['nome_da_coluna']`: Acessa uma coluna específica do DataFrame.
- `df[['coluna1', 'coluna2']]`: Acessa múltiplas colunas do DataFrame.

### Seleção de Linhas

- `df.loc[indice]`: Acessa uma linha específica do DataFrame pelo índice.
- `df.iloc[indice]`: Acessa uma linha específica do DataFrame pelo número da linha.

### Filtragem de Dados

- `df[df['coluna'] > valor]`: Filtra o DataFrame com base em uma condição.
- `df.query('condição')`: Filtra o DataFrame usando uma expressão booleana.

### Ordenação de Dados

- `df.sort_values('coluna')`: Ordena o DataFrame com base em uma coluna específica.

### Criação de Novas Colunas

- `df['nova_coluna'] = valor`: Cria uma nova coluna no DataFrame com um valor fixo.
- `df['nova_coluna'] = df['coluna1'] + df['coluna2']`: Cria uma nova coluna no DataFrame com base em cálculos entre colunas existentes.

### Remoção de Colunas

- `df.drop('coluna', axis=1, inplace=True)`: Remove uma coluna do DataFrame.

### Estatísticas Descritivas

#### Resumo Estatístico

- `df.describe()`: Retorna estatísticas descritivas do DataFrame, como média, desvio padrão, mínimo, máximo, etc.

### Agregação de Dados

- `df.groupby('coluna').mean()`: Calcula a média dos valores agrupados por uma coluna.

### Tratamento de Valores Ausentes

#### Verificação de Valores Ausentes

- `df.isnull()`: Retorna uma matriz booleana indicando quais valores são nulos.
- `df.isnull().sum()`: Retorna o número de valores nulos em cada coluna.

#### Preenchimento de Valores Ausentes

- `df.fillna(valor)`: Preenche os valores ausentes com um valor específico.
- `df.dropna()`: Remove as linhas que contêm valores nulos.

## Visualização de Dados

### Gráficos Básicos

- `df['coluna'].plot(kind='tipo_de_gráfico')`: Gera um gráfico básico para uma coluna específica.

### Gráficos Avançados

- `import matplotlib.pyplot as plt`: Importa a biblioteca Matplotlib para criar gráficos mais avançados.
- `df.plot(x='coluna1', y='coluna2', kind='tipo_de_gráfico')`: Gera um gráfico com base em duas colunas do DataFrame.

Lembre-se de consultar a [documentação oficial do Pandas](https://pandas.pydata.org/docs/) para obter mais informações sobre cada comando e explorar outras funcionalidades.
