
import sys

class AnalisadorSintatico:

    def __init__ (self, token, string, tabela):

        self.token = []
        self.string = []
        self.tabelaDeSimbolos = tabela
        self.carga = ''

        for i in range(len(token)):

            for j in range(len(token[i])):
                self.token.append(token[i][j])
                self.string.append(string[i][j])

    def erro(self, funcao, elemento):
        print ("ERRO SINTATICO NA FUNÇÃO ", funcao, ": ESPERAVA O TOKEN ", elemento)
        sys.exit()

    def remove(self):
        self.token.pop(0)
        self.string.pop(0)
    
    def analisar(self):

        def program():

            if (self.token[0] == 'program'):
                self.remove()

                if (self.token[0] == 'ident'):
                    self.tabelaDeSimbolos.addTabela('ident', self.string[0], '', 'program', 'escopo_global', '')
                    self.remove()
                    corpo()

                    if (self.token[0] == '.'):
                        self.remove()

                    else:
                        self.erro('program', '.')
                
                else:
                    self.erro('program', 'ident')

            else:
                self.erro('program', 'program')

        def corpo():

            dc()

            if (self.token[0] == 'begin'):
                self.remove()
                comandos()

                if (self.token[0] == 'end'):
                    self.remove()

                else:
                    self.erro('corpo', 'end')

            else:
                self.erro('corpo', 'begin')
        
        def dc():

            if (self.token[0] == 'var'):
                dc_v()
                mais_dc()

            elif (self.token[0] == 'procedure'):
                dc_p()
                mais_dc()
            
            else:
                return ''

        def mais_dc():

            if (self.token[0] == ';'):
                self.remove()
                dc()
            
            else:
                return ''

        def dc_v():

            if (self.token[0] == 'var'):
                self.carga = self.token[0]
                self.remove()
                variaveis()

                if (self.token[0] == ':'):
                    self.remove()
                    tipo_var()

                else:
                    self.erro('dc_v', ':')
            
            else:
                self.erro('dc_v', 'var')

        def tipo_var():

            if (self.token[0] == 'real' or self.token[0] == 'integer'):
                self.tabelaDeSimbolos.inserirTipo(self.token[0])
                self.tabelaDeSimbolos.addTabela(self.token[0], '', '', '', '', '')
                self.remove()

            else:
                self.erro('tipo_var', 'real ou integer')

        def variaveis():

            if (self.token[0] == 'ident'):
                escopo = self.tabelaDeSimbolos.buscarEscopo()
                self.tabelaDeSimbolos.addTabela('ident', self.string[0], '', self.carga, escopo, '')
                self.remove()
                mais_var()

            else:
                self.erro('variaveis', 'ident')

        def mais_var():

            if (self.token[0] == ','):
                self.remove()
                variaveis()

            else:
                return ''

        def dc_p():

            if (self.token[0] == 'procedure'):
                self.carga = 'var'
                self.remove()

                if (self.token[0] == 'ident'):
                    self.tabelaDeSimbolos.addTabela('ident', self.string[0], '', 'procedure', 'escopo_global', '')
                    self.remove()
                    parametros()
                    corpo_p()
                
                else:
                    self.erro('dc_p', 'ident')

            else:
                self.erro('dc_p', 'procedure')

        def parametros():

            if (self.token[0] == '('):
                self.remove()
                lista_par()

                if (self.token[0] == ')'):
                    self.remove()

                else:
                    self.erro('parametros', ')')

            else:
                return ''

        def lista_par():

            variaveis()

            if (self.token[0] == ':'):
                self.remove()
                tipo_var()
                mais_par()

            else:
                self.erro('lista_par', ':')

        def mais_par():

            if (self.token[0] == ';'):
                self.remove()
                lista_par()

            else:
                return ''

        def corpo_p():

            dc_loc()

            if (self.token[0] == 'begin'):
                self.remove()
                comandos()

                if (self.token[0] == 'end'):
                    self.tabelaDeSimbolos.addTabela('end', '', '', '', '', '')
                    self.remove()

                else:
                    self.erro('corpo_p', 'end')

            else:
                self.erro('corpo_p', 'begin')

        def dc_loc():

            if (self.token[0] == 'var'):
                dc_v()
                mais_dcloc()

            else:
                return ''

        def mais_dcloc():

            if (self.token[0] == ';'):
                self.remove()
                dc_loc()

            else:
                return ''

        def lista_arg():

            if (self.token[0] == '('):
                self.remove()
                argumentos()

                if (self.token[0] == ')'):
                    self.remove()

                else:
                    self.erro('lista_arg', ')')

            else:
                return ''

        def argumentos():

            if (self.token[0] == 'ident'):
                escopo = self.tabelaDeSimbolos.buscarEscopo()
                self.tabelaDeSimbolos.addTabela('ident', self.string[0], '', self.carga, escopo, '')
                self.remove()
                mais_ident()

            else:
                self.erro('argumentos', 'ident')

        def mais_ident():

            if (self.token[0] == ';'):
                self.remove()
                argumentos()

            else:
                return ''

        def pfalsa():

            if (self.token[0] == 'else'):
                self.remove()
                comandos()

            else:
                return ''

        def comandos():
            comando()
            mais_comandos()

        def mais_comandos():

            if (self.token[0] == ';'):
                self.remove()
                comandos()

            else:
                return ''   

        def comando():

            if (self.token[0] == 'read' or self.token[0] == 'write'):
                self.carga = self.token[0]
                self.remove()

                if (self.token[0] == '('):
                    self.remove()
                    variaveis()

                    if (self.token[0] == ')'):
                        self.remove()

                    else:
                        self.erro('comando', ')')

                else:
                    self.erro('comando', '(')

            elif (self.token[0] == 'while'):
                self.carga = self.token[0]
                self.remove()
                condicao()

                if (self.token[0] == 'do'):
                    self.remove()
                    comandos()

                    if (self.token[0] == '$'):
                        self.remove()

                    else:
                        self.erro('comando', '$')
                
                else:
                    self.erro('comando', 'do')

            elif (self.token[0] == 'if'):
                self.carga = self.token[0]
                self.remove()
                condicao()

                if (self.token[0] == 'then'):
                    self.remove()
                    comandos()
                    pfalsa()

                    if (self.token[0] == '$'):
                        self.remove()

                    else:
                        self.erro('comando', '$')
                
                else:
                    self.erro('comando', 'then')

            elif (self.token[0] == 'ident'):
                escopo = self.tabelaDeSimbolos.buscarEscopo()
                self.carga = 'atribuicao'
                self.tabelaDeSimbolos.addTabela('ident', self.string[0], '', self.carga, escopo, '')
                self.remove()
                restoIdent()

            else:
                self.erro('comando', 'read ou write ou while ou if ou ident')

        def restoIdent():

            if (self.token[0] == ':='):
                self.remove()
                expressao()

            else:
                lista_arg()

        def condicao():

            expressao()
            relacao()
            expressao()

        def relacao():

            if (self.token[0] == '=' or self.token[0] == '<>' or self.token[0] == '>=' or self.token[0] == '<=' or self.token[0] == '>' or self.token[0] == '<'):
                self.remove()

            else:
                self.erro('relacao', '= ou <> ou >= ou <= ou > ou <')

        def expressao():

            termo()
            outros_termos()

        def op_un():

            if (self.token[0] == '+' or self.token[0] == '-'):
                self.remove()

            else:
                return ''

        def outros_termos():

            if (self.token[0] == '+' or self.token[0] == '-'):
                op_ad()
                termo()
                outros_termos()

            else:
                return ''

        def op_ad():

            if (self.token[0] == '+' or self.token[0] == '-'):
                self.remove()

            else:
                self.erro('op_ad', '+ ou -')

        def termo():

            op_un()
            fator()
            mais_fatores()

        def mais_fatores():

            if (self.token[0] == '*' or self.token[0] == '/'):
                op_mul()
                fator()
                mais_fatores()

            else:
                return ''

        def op_mul():

            if (self.token[0] == '*' or self.token[0] == '/'):
                self.remove()

            else:
                self.erro('op_mul', '* ou /')

        def fator():

            if (self.token[0] == 'ident' or self.token[0] == 'numero_inteiro' or self.token[0] == 'numero_real'):
                escopo = self.tabelaDeSimbolos.buscarEscopo()

                if (self.token[0] == 'ident'):
                    self.tabelaDeSimbolos.addTabela('ident', self.string[0], '', self.carga, escopo, '')

                if (self.token[0] == 'numero_inteiro'):
                    self.tabelaDeSimbolos.addTabela('numero_inteiro', self.string[0], 'integer', '', escopo, self.string[0])

                if (self.token[0] == 'numero_real'):
                    self.tabelaDeSimbolos.addTabela('numero_real', self.string[0], 'real', '', escopo, self.string[0])

                self.remove()

            elif (self.token[0] == '('):
                self.remove()
                expressao()

                if (self.token[0] == ')'):
                    self.remove()

                else:
                    self.erro('fator', ')')

            else:
                self.erro('fator', 'ident ou numero_inteiro ou numero_real ou (')

        program()

        self.tabelaDeSimbolos.complementaTabela()





















