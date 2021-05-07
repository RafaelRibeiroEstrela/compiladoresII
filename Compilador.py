
from AbrirArquivo import carregarArquivo
from AnalisadorLexico import AnalisadorLexico
from AnalisadorSintatico import AnalisadorSintatico
from AnalisadorSemantico import AnalisadorSemantico
from TabelaDeSimbolos import TabelaDeSimbolos
from GrafoSintatico import grafoSintatico

def main():

    arquivo = carregarArquivo()
    token, string = AnalisadorLexico().analisar(arquivo)
    tabelaDeSimbolos = TabelaDeSimbolos()

    #VERIFICAR A POSSIBILIDADE DE COLOCAR O TIPO E VALOR NOS TOKEN DE ATRIBUIÇÃO
    AnalisadorSintatico(token, string, tabelaDeSimbolos).analisar()
    AnalisadorSemantico(token, string, tabelaDeSimbolos).analisar()
    print ("CODIGO COMPILADO SEM ERROS")
    #tabelaDeSimbolos.mostrarTabela()
    #grafoSintatico()



main()



