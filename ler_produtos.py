# FICHEIRO CSV
import csv

with open('Produtos.csv', 'r', encoding='cp1252') as ficheiro:
    ficheiro_csv = csv.reader(ficheiro, delimiter=';')
    for linha in ficheiro_csv:
        print(linha)
