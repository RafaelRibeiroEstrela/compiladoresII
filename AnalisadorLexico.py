
from AnalisadorLexicoUtil import tokenizar
from AnalisadorLexicoUtil import corrigeTokenString
import sys


class AnalisadorLexico:

    def __init__(self):

        self.palavraReservada = ['integer', 'real', 'if', 'else', 'do', 'while', 'write', 'read', 'then', 'begin', 'end', 'var', 'procedure', 'program']
        self.simbolos = ['(', ')', '*', '/', '+', '-', '>=', '<=', '>', '<', '<>', '=', ':=', '$', ';', ':', ',', '.']
        self.abreComentario = ['/*', '{']
        self.fechaComentario = ['*/', '}']

        self.token = []
        self.string = []

        print ("\n ANALISANDO LEXICAMENTE... \n")

    #PRINTA ERRO SINTATICO ENCONTRADO
    def erro(self, indice, palavra):
        print ("ERRO LEXICO NA LINHA ", indice + 1, ": O ELEMENTO ", palavra, "NÃO É CONHECIDO")
        sys.exit()

    #FUNÇÃO AUXILIAR DO ANALISADOR PARA VERIFICAR QUE TIPO DE TOKEN É O ELEMENTO
    def verificaPalavra(self, palavra, indice):

        numeros = ['0','1','2','3','4','5','6','7','8','9']
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']

        cont = 0

        if (palavra[0] in numeros):

            for i in palavra:

                if (i not in numeros and i != '.'):
                    self.erro(indice, palavra)

                if (i == '.'):
                    cont += 1

            if (cont == 0):
                self.token[indice].append('numero_inteiro')
                self.string[indice].append(palavra)
                
            
            elif (cont == 1):
                self.token[indice].append('numero_real')
                self.string[indice].append(palavra)
                
            
            else:
                self.erro(indice, palavra)

        elif (palavra[0] in alfabeto):
            self.token[indice].append('ident')
            self.string[indice].append(palavra)

        else:
            return False

    #FUNÇÃO DE FAZER A ANÁLISE LÉXICA DO ARQUIVO TEXTO
    def analisar(self, arquivo):

        lista = tokenizar(arquivo)

        comentario = False

        for i in range(len(lista)):
            self.token.append([])
            self.string.append([])

            for j in range(len(lista[i])):

                if (lista[i][j] in self.abreComentario):
                    comentario = True
                    continue

                if (lista[i][j] in self.fechaComentario):
                    comentario = False
                    continue

                if (comentario == True):
                    continue

                if (lista[i][j] in self.palavraReservada):
                    self.token[i].append(lista[i][j])
                    self.string[i].append(lista[i][j])

                elif (lista[i][j] in self.simbolos):
                    self.token[i].append(lista[i][j])
                    self.string[i].append(lista[i][j])

                else:
                    condicao = self.verificaPalavra(lista[i][j], i)

                    if (condicao == False):
                        self.erro(i, lista[i][j])

        self.token, self.string = corrigeTokenString(self.token, self.string)
        
        #print ("LISTA DE TOKENS")
        #for linha in self.token:
            #print (linha)

        print ('\n')

        return self.token, self.string

            


                

                


                








        

    



        





















        