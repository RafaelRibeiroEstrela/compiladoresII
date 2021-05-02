
import sys

class AnalisadorSemantico:

    def __init__(self, token, string, tabela):

        self.tabela = tabela
        self.token = token
        self.string = string
    
    def erroDeclaracao(self, cadeia, escopo):
        print ("ERRO SEMANTICO: A VARIAVEL", cadeia, "JÁ FOI USADA EM OUTRA DECLARAÇÃO NO ESCOPO", escopo)
        sys.exit()

    def erroAtribuicao(self, cadeia, escopo):
        print ("ERRO SEMANTICO: A VARIAVEL", cadeia, "ESTA SENDO ATRIBUIDA COM TIPO DEFERENTE NO ESCOPO", escopo)
        sys.exit()

    def erroDivisao(self, cadeia, escopo):
        print ("ERRO SEMANTICO: A VARIAVEL", cadeia, "ESTA SENDO DIVIDIDA COM TIPO DEFERENTE NO ESCOPO", escopo)
        sys.exit()


    def verificaDivisao(self):

        escopo = 'escopo_global'

        for i in range(len(self.token)):

            if (self.token[i][0] == 'procedure'):
                escopo = 'escopo_' + self.string[i][1]
                
            if (self.token[i][0] == 'end'):
                escopo = 'escopo_global'

            if ('/' in self.token[i]):

                for j in range(len(self.token[i])):

                    if (self.token[i][j] == '/'):

                        esq = self.string[i][j-1]
                        dire = self.string[i][j+1]

                condicao = self.tabela.verificaDivisao(esq, dire, escopo)

                if not condicao:
                    self.erroDivisao(esq, escopo)

    def verificaProcedure(self):

        procedure = ''

        for i in range(len(self.token)):

            if (self.token[i][0] == 'procedure'):

                if (self.string[i][1] == procedure):
                    self.erroDeclaracao(procedure, 'escopo_global')
                
                procedure = self.string[i][1]


    def verificaLinhaDeclaracao(self, listaCadeia, escopo):

        for i in range(len(listaCadeia)):

            for j in range(len(listaCadeia)):

                if (listaCadeia[i] == listaCadeia[j] and i != j):
                    self.erroDeclaracao(listaCadeia[i], escopo)
            
            erro = self.tabela.verificaDeclaracao(listaCadeia[i], escopo)

            if (erro == True):
                self.erroDeclaracao(listaCadeia[i], escopo)

   
    def verificaDeclaracao(self):

        escopo = 'escopo_global'
        listaCadeia = []

        for i in range(len(self.token)):

            if (self.token[i][0] == 'procedure'):
                escopo = 'escopo_' + self.string[i][1]

                for j in range(len(self.token[i])):

                    if (self.token[i][j] == 'ident'):
                        listaCadeia.append(self.string[i][j])

                self.verificaLinhaDeclaracao(listaCadeia, escopo)
                listaCadeia.clear()
                
            if (self.token[i][0] == 'end'):
                escopo = 'escopo_global'

            if (self.token[i][0] == 'var'):
                
                for j in range(len(self.token[i])):

                    if (self.token[i][j] == 'ident'):
                        listaCadeia.append(self.string[i][j])

                self.verificaLinhaDeclaracao(listaCadeia, escopo)
                listaCadeia.clear()

    
    def verificaLinhaAtribuicao(self, listaTipos, cadeia, escopo):

        tipo = listaTipos[0]

        if (tipo == 'integer'):

            for i in listaTipos:

                if (tipo != i):
                    self.erroAtribuicao(cadeia, escopo)

    def verificaAtribuicao(self):

        escopo = 'escopo_global'
        listaTipos = []

        for i in range(len(self.token)):

            if (self.token[i][0] == 'procedure'):
                escopo = 'escopo_' + self.string[i][1]
                
            if (self.token[i][0] == 'end'):
                escopo = 'escopo_global'

            if (':=' in self.token[i]):

                #print ("ENTROU NA FUNCAO")

                for j in range(len(self.token[i])):

                    if (self.token[i][j] == 'ident' or self.token[i][j] == 'numero_real' or self.token[i][j] == 'numero_inteiro'):

                        tipo = self.tabela.verificaAtribuicao(self.string[i][j], escopo, self.token[i][j])

                        if (tipo == False):
                            print ("ERRO: Elemento não encontrado na tabela de simbolos")
                            sys.exit()
                        
                        listaTipos.append(tipo)
                
                #print ("Cadeia: ", self.string[i][0])
                #print ("Escopo: ", escopo)
                #print ("ListaTipos: ", listaTipos)
                self.verificaLinhaAtribuicao(listaTipos, self.string[i][0], escopo)
                listaTipos.clear()

            

            
                
               




            

            

        





    def analisar(self):

        self.verificaProcedure()
        self.verificaDeclaracao()
        self.verificaAtribuicao()

        





                

    



                

                



                