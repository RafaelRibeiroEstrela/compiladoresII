import nltk
import sys


#PRÉ TOKENIZAÇÃO DOS ELEMENTOS
def tokenizar(lista):
    tkn = nltk.WordPunctTokenizer()

    for i in range(len(lista)):
        lista[i] = tkn.tokenize(lista[i])

    return corrigirTokenizacao(lista)


#FUNÇÃO AUXILIAR PARA VERIFICAR SE É UM NUMERO NA PRÉ TOKENIZAÇÃO
def verificaNumero(indice, string):
    numeros = '0123456789'
    
    for i in string:
        
        if (i not in numeros):
            return False
    
    return True


#FUNÇÃO QUE CORRIGE A PRÉ TOKENIZAÇÃO
def corrigirTokenizacao(lista):
    cont = 0
    posicaoDeletar = []
    numerosReais = []

    for i in range(len(lista)):

        for j in range(len(lista[i])):

            if (')' in lista[i][j] and len(lista[i][j]) > 1):
                #print ("ANTES: ", lista[i][j])
                temp = lista[i][j][1:]
                lista[i][j] = lista[i][j][0]
                lista[i].insert(j+1, temp)
                #print ("DEPOIS: ", lista[i][j], ',', lista[i][j+1])
                cont += 1


            if ('$' in lista[i][j] and len(lista[i][j]) > 1):
                #print ("ANTES: ", lista[i][j])
                temp = lista[i][j][1:]
                lista[i][j] = lista[i][j][0]
                lista[i].insert(j+1, temp)
                #print ("DEPOIS: ", lista[i][j], ',', lista[i][j+1])
                cont += 1
        
            if (lista[i][j] == '.' and verificaNumero(i, lista[i][j-1]) == True and verificaNumero(i, lista[i][j+1]) == True):
                temp = lista[i][j-1] + lista[i][j] + lista[i][j+1]
                #print ("numero real: ", temp)
                numerosReais.append(temp)
                posicaoDeletar.append([i, j])
                cont += 1

    for k in range(len(posicaoDeletar)):
        i = posicaoDeletar[k][0]
        j = posicaoDeletar[k][1]
        lista[i][j-1] = numerosReais[k]
        del(lista[i][j:j+2])


    #REMOVE LINHA VAZIA
    l = []

    for i in lista:

        if (len(i) == 0):
            continue
        
        l.append(i)

    return verificaCorrecao(l)   


#FUNÇÃO QUE VERIFICA SE A CORREÇÃO FOI FEITA COM SUCESSO
def verificaCorrecao(lista):

    for i in range(len(lista)):
    
        for j in range(len(lista[i])):

            if (')' in lista[i][j] and len(lista[i][j]) > 1):
                print ("Erro ao verificar o simbolo", lista[i][j])
                sys.exit()

            if ('$' in lista[i][j] and len(lista[i][j]) > 1):
                print ("Erro ao verificar o simbolo", lista[i][j])
                sys.exit()

    return lista

#REMOVE LINHAS VÁZIAS GERADAS PELOS COMENTÁRIOS
def corrigeTokenString(token, string):
    tokenS = []
    stringS = []

    for i in range(len(token)):

        if (len(token[i]) == 0):
            continue

        tokenS.append(token[i])
        stringS.append(string[i])

    return tokenS, stringS

