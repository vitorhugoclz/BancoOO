from Dominio.Conta import Conta
from Dominio.ContaPoupanca import ContaPoupanca
from Dominio.ContaCorrente import ContaCorrente
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015
'''

class Cliente:
    
    def __init__(self, nome:str, sobrenome:str):
        '''
        inicialização dos atributos da classe cliente
        '''
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__contas = list()

    def getPrimeiroNome(self) -> str:
        '''
        retorna o atributo nome
        '''
        return self.__nome

    def setNome(self, nome:str) -> None:
        '''
        seta o atributo nome
        '''
        self.__nome = nome

    def getUltimoNome(self) -> str:
        '''
        retorna o atributo sobrenome
        '''
        return self.__sobrenome

    def setSobrenome(self, sobrenome:str) -> None:
        '''
        seta o atributo sobrenome
        '''
        self.__sobrenome = sobrenome

    def setConta(self, conta:Conta) -> None:
        '''
        adiciona uma conta na lista de contas do cliente
        '''
        self.__contas.append(conta)
        
    def getConta(self, indice:int)-> Conta:
        '''
        retorna a conta na posição do indíce passado
        por parametro
        '''
        if indice < len(self.__contas):
            return self.__contas[indice]
        else:
            return None
        
    def getNumeroContas(self) -> int:
        '''
        retorna a quantidade de contas que o cliente
        possui
        '''
        return len(self.__contas)
    
    def __str__(self) -> str:
        '''
        sobreescrita do metodo __str__ que tem a mesma
        funcionalidade do metodo toString do Java
        ele vai retornar uma string contendo todas as informações
        do objeto
        '''
        textoNome = f'Nome: {self.__nome}, Sobrenome: {self.__sobrenome}\n'
        textoContas = 'Contas: \n'
        for i in range(len(self.__contas)):
            conta = self.__contas[i]
            texto = conta.__str__() + '\n'
            textoContas += texto
        return textoNome + textoContas

    def __eq__(self, cliente):
        '''
        sobreescrita do metodo __eq__ que funciona como o método equals do java
        quando é comparado dois objetos do tipo cliente por " == " esse método
        é chamado por de baixo dos panos
        '''
        return self.__nome == cliente.__nome and self.__sobrenome == cliente.__sobrenome
 
