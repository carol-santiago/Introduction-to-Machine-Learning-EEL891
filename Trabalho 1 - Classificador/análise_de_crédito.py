# %%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from pandas.plotting import scatter_matrix
import seaborn as sns

# Carregar o conjunto de dados


def load_dataset():
    df_train = pd.read_csv(
        './Dataset/conjunto_de_treinamento.csv')
    return df_train


df_train = load_dataset()
df_train.drop(columns=['id_solicitante'], inplace=True)


# %%
# TESTES
df_train.drop(columns=['id_solicitante'], inplace=True)
# for i in range(len(df_train.columns)):
#     print(df_train.columns[i], i)

# %%
# Criar um gráfico de barras para visualizar a distribuição dos dados


def grafico_barras(column):
    if pd.api.types.is_numeric_dtype(df_train[column]):
        grafico = df_train[column].plot.hist(bins=20, edgecolor='black')
        grafico.set(
            title='Histograma de ' + column,
            xlabel=column,
            ylabel='Frequência')
    else:
        grafico = plt.figure()
        plt.text(0.5, 0.5, 'Non-numeric data', ha='center', va='center')
        plt.axis('off')
        plt.title('Histograma de ' + column)
    plt.show()
    return grafico


for i in range(len(df_train.columns)):
    grafico_barras(df_train.columns[i])
    plt.show()

# %%


def scatter_matrix_all(df):
    atributo = df.iloc[:, :-1]
    mapa_cores = ['red', 'green', 'aqua']
    cores_amostras = [mapa_cores[i] for i in df.iloc[:, -1]]
    pd.plotting.scatter_matrix(
        atributo[atributo.columns[:11]],
        figsize=(13, 13),
        c=cores_amostras,
        marker='o',
        s=50,
        alpha=0.5,
        diagonal='hist')
    plt.show()


scatter_matrix_all(df_train)

# %%
# Criar uma matriz de correlação para visualizar a relação entre as variáveis


def matriz_de_correlacao(df):
    atributo = df.iloc[:, :-1]
    correlation_matrix = atributo[atributo.columns[20:30]].corr()
    if correlation_matrix.empty:
        print('Não há correlação entre as variáveis')
    print(correlation_matrix)
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlação')
    plt.show()


matriz_de_correlacao(df_train)

# %%
# Criar um gráfico de dispersão para visualizar a relação entre duas variáveis


def grafico_de_dispersao(df, variavel1, variavel2):
    plt.scatter(df[variavel1], df[variavel2])
    plt.xlabel(variavel1)
    plt.ylabel(variavel2)
    plt.title(f'Gráfico de Dispersão: {variavel1} vs {variavel2}')
    plt.show()


# grafico_de_dispersao(df_train, df_train.columns[0], df_train.columns[1])

i = 2
for j in range(len(df_train.columns)):
    grafico_de_dispersao(
        df_train, df_train.columns[i], df_train.columns[j])
    plt.show()

# %%
