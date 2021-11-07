lst_estados = []


class Cores: 
    azul = '\033[94m'
    verde = '\033[92m'
    amarelo = '\033[93m'
    rosa = '\033[95m'
    vermelho = '\033[91m'
    branco = '\033[0;37m'

cor = Cores()

class Estado:

    def __init__(self, nomedoestado, sigladoestado):
        self.__nome = nomedoestado
        self.__sigla = sigladoestado
        self.__qt_casos_estado =0
        self.__lst_cidades = []  
       
    def get_nome(self):
        return self.__nome

    def get_sigla(self):
        return self.__sigla
    
    def adiciona_cidade(self, cidade):
        self.__lst_cidades.append(cidade)

    def set_qnt_casos(self, casos):
        self.__qt_casos_estado = self.__qt_casos_estado + casos

    def get_qnt_casos(self):
        return self.__qt_casos_estado

    def get_cidades(self):
        return self.__lst_cidades

    def exibe_cidades(self):
        for cidade in self.__lst_cidades:
            print (f"{cor.verde}--------------------------------------------------------")
            print (f"{cor.azul}Cidade: ", cidade.get_nome(), f"{cor.amarelo}| ", f"{cor.rosa}Casos: -----> ", cidade.get_casos()) 
            print (f"{cor.verde}--------------------------------------------------------")
    
    def mostra_cidades(self):
        if len(self.__lst_cidades) > 0:
            print (f"{cor.amarelo}\nCidades cadastradas até o momento: ")
            for cidade in self.__lst_cidades:
                print (f"{cor.verde}{cidade.get_nome()}")                
            return False
        


    def valida_cidade(self, nome):
        for cidade in self.__lst_cidades:
            if cidade.get_nome() == nome:
                return True
        return False

    
    def remove_casos(self, casos):
        self.__qt_casos_estado =  self.__qt_casos_estado - casos

    def __str__(self):
        return f"{self.__nome}, {self.__sigla}, {self.__qt_casos_estado}"



class Cidade:

    def __init__(self, nome):
        self.__nome_cidade = nome
        self.__qnt_casos = 0
    
    def set_nome(self, nome):
        self.__nome_cidade = nome

    def get_nome(self):
        return self.__nome_cidade

    def set_casos(self, casos):
        self.__qnt_casos = self.__qnt_casos + casos
        

    def get_casos(self):
        return self.__qnt_casos

    def remove_casos(self, casos):
        self.__qnt_casos =  self.__qnt_casos - casos


##### VALIDAÇÕES #####


def validar_estado(nome):
    for estado in lst_estados:        
        if estado.get_nome() == nome:
            return True        
    return False


def valida_sigla(uf):   
    for estado in lst_estados:
        if estado.get_sigla() == uf:
            return True                 
    return False
    
##########################

def mostra_estados():
    if len(lst_estados)> 0:
        print(f"{cor.azul}\nEstados cadastrados até o momento:")
        for estado in lst_estados:    
            print(f"\n{cor.verde}{estado.get_nome()}"", " f" {estado.get_sigla()}")



##### CADASTROS #####

def cadastrar_estado():
    mostra_estados()  
    nome_estado = input(f"{cor.amarelo}\nInsira o nome do estado que deseja cadastrar: ").upper()
    sigla = input(f"{cor.amarelo}\nDigite a sigla do estado: ").upper() 
    if validar_estado(nome_estado) == False and valida_sigla(sigla) == False:            
        estado = Estado(nome_estado, sigla)                                                                                                               
        lst_estados.append(estado)                 
        print(f"{cor.verde}\nCadastro de estados concluído.")     
    else: 
        escolha =  input(f"{cor.vermelho}\nEstado já está na lista. Deseja adicionar outro? S para sim, N para não: ").upper()
        if escolha == 'S':
            cadastrar_estado() 
            
        else:
            print (f"{cor.verde}\nOk, encerramos.")
 
    



def cadastrar_cidade():
    mostra_estados()
    if len(lst_estados)> 0:        
        sigla = input(f"{cor.amarelo}\nDigite a sigla do estado para cadastrar a cidade:  ").upper()
        for estado in lst_estados:
            if valida_sigla(sigla) == True:
                if estado.get_sigla() == sigla:
                    estado.mostra_cidades() 
                    nome_cidade = input(f"{cor.amarelo}\nDigite o nome da cidade que deseja cadastrar: ").upper()
                    if estado.valida_cidade(nome_cidade) == False:
                        cidade = Cidade(nome_cidade)
                        estado.adiciona_cidade(cidade)
                        print(f"{cor.verde}\nCadastro de cidades concluído.")
                        
                    else:
                        escolha = input (f"{cor.vermelho}\nCidade ja cadastrada. Deseja cadastrar uma nova? S para Sim, N para não: ").upper()
                        if escolha == 'S':
                            cadastrar_cidade()
                        else:
                            print (f"{cor.verde}\nEncerramos.")

            else:
                escolher = input (f"{cor.vermelho}\nEstado não está na lista. Deseja adicionar? S para Sim, N para não: ").upper()
                if escolher == 'S':
                    cadastrar_estado()
                    cadastrar_cidade()
                    break 
                else:
                    print (f"{cor.verde}\nEncerramos.")
                    break
    else:
        print (f"{cor.vermelho}\nNão há estados cadastrados ainda")


#####################             

##### RELATÓRIOS #####

def relatorio_estados(): 
    if len(lst_estados) > 0:     
        for estado in lst_estados:
            print (f"\n{cor.amarelo}{estado.get_nome()}, ",  estado.get_sigla(), f"{cor.verde}------->", f"{cor.azul}Total de casos: ",estado.get_qnt_casos())
    else:
        print (f"{cor.vermelho}\nAinda não foram cadastrados estados.")
        
         

def relatorio_cidades():
    if len(lst_estados) > 0:
        mostra_estados()
        sigla = input(f"{cor.amarelo}\nDigite a sigla do estado para ver as cidades registradas: ").upper()
        if valida_sigla(sigla) == True:
            for estado in lst_estados: 
                if estado.get_sigla() == sigla:
                    if len(estado.get_cidades()) > 0:
                        estado.exibe_cidades()
                    else:
                        print (f"{cor.vermelho}\nO estado ainda não possui cidades cadastradas!")
                        
        else:
            print(f"{cor.vermelho}\nNenhum estado com esta sigla está na lista!")         
                    
    else:
        print (f"{cor.vermelho}\nNenhuma cidade foi cadastrada ainda!")


#####################    

def atualizar_casos():
    if len(lst_estados) > 0:
        mostra_estados()    
        sigla = input(f"{cor.amarelo}\nDigite a sigla do estado que a cidade pertence: ").upper()
        if valida_sigla(sigla) == True:
            for estado in lst_estados:
                if estado.get_sigla() == sigla:
                    if estado.mostra_cidades() == False:
                        cidadenome = input(f"{cor.amarelo}\nDigite o nome da cidade para atualizar os casos: ").upper()             
                        if estado.valida_cidade(cidadenome) == True:
                            for cidade in estado.get_cidades():
                                if cidade.get_nome() == cidadenome:
                                    adrem = input(f"{cor.branco}\nVocê deseja adicionar ou remover casos desta cidade? {cor.verde}1 para ADICIONAR casos " f"{cor.branco}||" f" {cor.vermelho}2 para REMOVER casos: ")
                                    if adrem == '1':
                                        try:
                                            casos = int(input(f"{cor.amarelo}\nInforme a quantidade de novos casos que há na cidade: "))
                                            if casos > 0:                                                            
                                                cidade.set_casos(casos)
                                                estado.set_qnt_casos (casos)
                                                print(f"{cor.verde}\nConcluído.")
                                            else:
                                                escolha = input(f"{cor.vermelho}\nVocê não pode digitar casos negativos! Deseja adicionar novamente? S para Sim, N para Não: ").upper()
                                                if escolha == 'S':
                                                    atualizar_casos()
                                                else:
                                                    print (f"{cor.verde}\nEncerramos.")
                                        except:
                                            esc = input (f"{cor.vermelho}\nDigite apenas números inteiros! Deseja tentar novamente? S para Sim, N para Não: ").upper()
                                            if esc == 'S':
                                                atualizar_casos()
                                            else:
                                                print (f"{cor.verde}\nOk, encerramos.")
                                    elif adrem == '2':
                                        if cidade.get_casos() > 0:    
                                            try:
                                                casos1 = int(input(f"{cor.amarelo}\nInforme a quantidade de casos a serem removidos: "))                                            
                                                if casos1 > 0:
                                                    if cidade.get_casos() - casos1 > 0:  
                                                        cidade.remove_casos(casos1)
                                                        estado.remove_casos (casos1)
                                                        print(f"{cor.verde}\nConcluído.")
                                                    else:
                                                        print (f"{cor.vermelho}\nOs casos não podem ficar negativos! Tente novamente")
                                                        atualizar_casos()
                                                    
                                                else:
                                                    escolha = input(f"{cor.vermelho}\nVocê não pode digitar casos negativos! Deseja adicionar novamente? S para Sim, N para Não: ").upper()
                                                    if escolha == 'S':
                                                        atualizar_casos()
                                                    else:
                                                        print (f"{cor.verde}\nEncerramos.")
                                            except:
                                                esc = input (f"{cor.vermelho}\nDigite apenas números inteiros! Deseja tentar novamente? S para Sim, N para Não: ").upper()
                                                if esc == 'S':
                                                    atualizar_casos()
                                                else:
                                                    print (f"{cor.verde}\nOk, encerramos.")
                                                    
                                        else:
                                            print(f"{cor.vermelho}\nAinda não foram digitados casos na cidade!Não há o que remover. Adicione primeiro.")
                                            
                                    else:
                                        print(f"{cor.vermelho}\nDigite algo válido!")
                                        atualizar_casos()

                                                                                                                        
                        else:
                            esc = input (f"{cor.vermelho}\nA cidade digitada não está na lista! Deseja adicionar essa cidade? S para Sim, N para Não: ").upper()
                            if esc == 'S':
                                cadastrar_cidade()
                            else:
                                print(f"{cor.verde}\nOk, encerramos.")
                    else:
                        print(f"{cor.vermelho}Ainda não existem cidades cadastradas no momento.")

        else:
            print (f"{cor.vermelho}\nNenhum estado com esta sigla está na lista!")
    else:
        print(f"{cor.vermelho}\nAinda não foram cadastrados estados nem cidades!")

#####################  


def menu_principal():
    print( f"""\n\n {cor.rosa}                    Bem - vindo ao menu!   
                    ----------------------------------
                    0. Encerrar programa
                    1. Cadastrar Estados
                    2. Cadastrar Cidades 
                    3. Mostrar relatório de estados
                    4. Mostrar relatório de cidades                   
                    5. Atualizar casos de cidades
                    ----------------------------------
                    """)

def escolhas():
    
    escolha = input (f"{cor.rosa}Digite a opção que deseja: """)
    if escolha == '1':
        cadastrar_estado()
    elif escolha == '2':
        cadastrar_cidade()
    elif escolha == '3':
        relatorio_estados()
    elif escolha =='4':
        relatorio_cidades()
    elif escolha =='5':
        atualizar_casos()
    elif escolha =='0':
        print(f"{cor.verde}\nVocê escolheu encerrar.") 
        return False      
    else:
        print (f"{cor.vermelho}\nEscolha uma opção válida!")


while True:
    menu_principal()
    if escolhas() == False:
        break

