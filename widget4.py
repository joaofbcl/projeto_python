import PySimpleGUI as sg

# Abre uma janela para o usuário selecionar um arquivo
path = sg.popup_get_file('Selecione um ficheiro')

# Imprime o caminho do arquivo selecionado
print(path)
