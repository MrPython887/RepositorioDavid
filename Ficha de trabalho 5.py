import csv
import matplotlib.pyplot as plt
#função leitura
def ler_ficheiro(nome_arquivo):
    dados =[]
    with open(nome_arquivo, newline="") as arquivo_csv:
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
def grafico_barras()
