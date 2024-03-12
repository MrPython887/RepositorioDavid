import csv
import matplotlib.pyplot as plt
#função leitura
def ler_ficheiro(nome_arquivo):
    dados =[]
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            dados.append(linha)
    return dados

def ordenar_bubblesort(dados):
    n = len(dados)
    for i in range(n):
        for k in range(n - i - 1):
            if int(dados[k][1]) > int(dados[k + 1][1]):
                dados[k], dados[k + 1] = dados[k + 1], dados[k]
    return dados
def grafico_barras(produtos, vendas):
    plt.bar(produtos, vendas)
    plt.xlabel('total de vendas')
    plt.title('produtos e vendas')
    plt.ticks(rotation=90)
    plt.show()


dados_csv = ler_ficheiro("AtividadePedagogica4_10793_02.csv")

dados_ordenados_bubblesort = ordenar_bubblesort("AtividadePedagogica4_10793_02.csv")

produtos_bubblesort = [linha[0] for linha in dados_ordenados_bubblesort]
vendas_bubblesort = [int(linha[1]) for linha in dados_ordenados_bubblesort]

grafico_barras(produtos_bubblesort, vendas_bubblesort)