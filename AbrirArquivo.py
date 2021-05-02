from tkinter import Tk
from tkinter.filedialog import askopenfilename

#FUNÇÃO QUER CARREGA O DIRETÓRIO DO ARQUIVO TEXTO
def carregarArquivo():

    Tk().withdraw()
    diretorio = askopenfilename(title = "SELECIONE O ARQUIVO A SER LIDO")
    return lerArquivo(diretorio)

#FUNÇÃO QUE FAZ A LEITURA DO ARQUIVO TEXTO
def lerArquivo(diretorio):

    arquivo = open(diretorio, 'r')
    linhas = arquivo.readlines()
    return linhas







