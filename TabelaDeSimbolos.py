
import sys

class TabelaDeSimbolos:

    def __init__(self):

        self.tabela = {"token":[], "cadeia":[], "tipo":[], "categoria":[], "escopo":[], "valor":[]}


    def addTabela(self, token, cadeia, tipo, categoria, escopo, valor):

        self.tabela["token"].append(token)
        self.tabela["cadeia"].append(cadeia)
        self.tabela["tipo"].append(tipo)
        self.tabela["categoria"].append(categoria)
        self.tabela["escopo"].append(escopo)
        self.tabela["valor"].append(valor)

    
    def complementaTabela(self):

        cadeia = ''
        escopo = ''
        tipo = ''

        for i in range(len(self.tabela["cadeia"])):

            if (self.tabela["token"][i] == 'ident' and self.tabela["categoria"][i] == 'var'):
                cadeia = self.tabela["cadeia"][i]
                escopo = self.tabela["escopo"][i]
                tipo = self.tabela["tipo"][i]

            for j in range(len(self.tabela["cadeia"])):

                if (self.tabela["cadeia"][j] == cadeia and self.tabela["escopo"][j] == escopo and self.tabela["categoria"][j] == 'atribuicao' and i != j):
                    self.tabela["tipo"][j] = tipo


    def buscarEscopo(self):

        #self.mostrarTabela()

        for i in range(len(self.tabela["token"]) - 1, -1, -1):

            if (self.tabela["token"][i] == 'end'):
                return 'escopo_global'
            
            elif (self.tabela["categoria"][i] == 'procedure'):
                return 'escopo_' + self.tabela["cadeia"][i]

            elif (self.tabela["categoria"][i] == 'program'):
                return 'escopo_global'

    def inserirTipo(self, tipo):

        for i in range(len(self.tabela["token"]) - 1, 0, -1):

            if (self.tabela["token"][i] == 'real' or self.tabela["token"][i] == 'integer'):
                break

            if (self.tabela["categoria"][i] == 'var'):
                self.tabela["tipo"][i] = tipo

    
    def verificaDeclaracao(self, cadeia, escopo):

        cont = 0

        for i in range(len(self.tabela["cadeia"])):

            if (self.tabela["cadeia"][i] == cadeia and self.tabela["escopo"][i] == escopo and self.tabela["categoria"][i] == 'var'):
                cont += 1

        if (cont > 1):
            return True
        
        return False

    def verificaDivisao(self, esq, dire, escopo):

        tipo1 = tipo2 = ''

        for i in range(len(self.tabela["cadeia"])):

            if (self.tabela["cadeia"][i] == esq and self.tabela["escopo"][i] == escopo and self.tabela["categoria"][i] == 'atribuicao'):
                tipo1 = self.tabela["tipo"][i]
            
            if (self.tabela["cadeia"][i] == dire and self.tabela["escopo"][i] == escopo and self.tabela["categoria"][i] == 'atribuicao'):
                tipo2 = self.tabela["tipo"][i]
        
        if (tipo1 != tipo2):
            return False
        
        return True

        


    
    def verificaAtribuicao(self, cadeia, escopo, token):

        if (token == 'ident'):

            for i in range(len(self.tabela["cadeia"])):

                if (self.tabela["cadeia"][i] == cadeia and self.tabela["escopo"][i] == escopo and self.tabela["categoria"][i] == 'atribuicao'):
                    return self.tabela["tipo"][i]

        else:

            for i in range(len(self.tabela["cadeia"])):

                if (self.tabela["cadeia"][i] == cadeia and self.tabela["escopo"][i] == escopo):
                    return self.tabela["tipo"][i]
            
        return False

    
    def verificaExistenciaIdent(self, cadeia, escopo, token):

        for i in range(len(self.tabela["cadeia"])):

            if (self.tabela["cadeia"][i] == cadeia and self.tabela["escopo"][i] == escopo and self.tabela["token"][i] == token):
                return True
            
            return False





        



    '''
    def retornaElementos(self, i):

        print ("ENTROU NA OUTRA FUNÇÃO")

        if (self.tabela["token"][i] == 'ident' and self.tabela["categoria"][i] == 'var' and self.tabela["tipo"][i] == 'real' or self.tabela["tipo"][i] == 'integer'):
            print ("ENTROU NO IF")
            cadeia = self.tabela["cadeia"][i]
            categoria = self.tabela["categoria"][i]
            escopo = self.tabela["escopo"][i]
        
            return cadeia, categoria, escopo
        
        return '', '', ''

    def verificaDeclaracao(self):

        #print ("ENTROU NA FUNÇÃO")

        for i in range(len(self.tabela["cadeia"])):
            cadeia1, categoria1, escopo1 = self.retornaElementos(i)

            if (cadeia1 == '' and categoria1 == '' and escopo1 == ''):
                continue

            for j in range(len(self.tabela["cadeia"])):

                if (j != i):
                    cadeia2, categoria2, escopo2 = self.retornaElementos(j)

                    if (cadeia2 == '' and categoria2 == '' and escopo2 == ''):
                        continue

                    if (cadeia1 == cadeia2 and categoria1 == categoria2 and escopo1 == escopo2):
                        #print ("CONDICAO 1: ", self.tabela["cadeia"][i], self.tabela["categoria"][i], self.tabela["escopo"][i])
                        #print ("CONDICAO 2: ", self.tabela["cadeia"][j], self.tabela["categoria"][j], self.tabela["escopo"][j])
                        #print (i, j)
                        return cadeia1, escopo1
        
        return '', ''
        '''

    def mostrarTabela(self):

        print ("TABELA DE SIMBOLOS")

        for i in range(len(self.tabela["token"])):

            print ("token: ", self.tabela["token"][i], " - cadeia: ", self.tabela["cadeia"][i], " - tipo: ", self.tabela["tipo"][i], " - categoria: ", self.tabela["categoria"][i], " - escopo: ", self.tabela["escopo"][i], " - valor: ", self.tabela["valor"][i])

