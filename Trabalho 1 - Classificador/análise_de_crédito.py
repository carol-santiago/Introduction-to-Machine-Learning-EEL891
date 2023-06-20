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
df_train.drop(columns=['id_solicitante'], inplace=True)
print(df_train.head())  # Verify the DataFrame after dropping the column

# Imprimir os nomes das colunas de treinamento
# print_column_names(df_train)

# Save DataFrame to an Excel file with a new sheet
with pd.ExcelWriter('Trabalho 1 - Classificador/Dataset/df_treinamento.xlsx', engine='openpyxl') as writer:
    df_train.to_excel(
        writer, sheet_name='conjunto de treinamento', index=False)

    # Access the workbook and sheet
    workbook = writer.book  # Access the workbook
    worksheet = workbook['conjunto de treinamento']  # Access the sheet

    # Apply formatting to the sheet
    column_widths = [15, 20, 25]  # Specify the desired column widths
    for i, width in enumerate(column_widths):
        worksheet.column_dimensions[worksheet.cell(
            row=1, column=i+1).column_letter].width = width

    # Save the Excel file
    writer.save()
