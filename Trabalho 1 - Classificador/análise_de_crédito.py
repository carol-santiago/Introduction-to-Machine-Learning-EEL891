import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Carregar o conjunto de dados


def load_dataset():
    df_train = pd.read_csv(
        'Trabalho 1 - Classificador/Dataset/conjunto_de_treinamento.csv')
    return df_train

# Imprimir os nomes das colunas de treinamento


def print_column_names(df):
    columns = df.columns[:-1]  # Excluir a última coluna (variável-alvo)
    for column in columns:
        print(column)


# Carregar o conjunto de dados
df_train = load_dataset()

# Imprimir os nomes das colunas de treinamento
print_column_names(df_train)
