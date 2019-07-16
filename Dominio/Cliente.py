from Dominio.Conta import Conta
from Dominio.ContaPoupanca import ContaPoupanca
from Dominio.ContaCorrente import ContaCorrente
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015'''
class Cliente:
    
    def __init__(self, nome:str, sobrenome:str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__contas = list()

    def getPrimeiroNome(self) -> str:
        return self.__nome

    def setNome(self, nome:str) -> None:
        self.__nome = nome

    def getUltimoNome(self) -> str:
        return self.__sobrenome

    def setSobrenome(self, sobrenome:str) -> None:
        self.__sobrenome = sobrenome

    def setConta(self, conta:Conta) -> None:
        self.__contas.append(conta)
        
    def getConta(self, indice:int)-> Conta:
        if indice < len(self.__contas):
            return self.__contas[indice]
        else:
            return None
        
    def getNumeroContas(self) -> int:
        return len(self.__contas)
    
    def __str__(self) -> str:
        textoNome = f'Nome: {self.__nome}, Sobrenome: {self.__sobrenome}\n'
        textoContas = 'Contas: \n'
        for i in range(len(self.__contas)):
            conta = self.__contas[i]
            texto = conta.__str__() + '\n'
            textoContas += texto
        return textoNome + textoContas

    def __eq__(self, cliente):
        return self.__nome == cliente.__nome and self.__sobrenome == cliente.__sobrenome
 
