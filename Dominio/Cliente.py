from Dominio.Conta import Conta
from Dominio.ContaPoupanca import ContaPoupanca
from Dominio.ContaCorrente import ContaCorrente
class Cliente:
    def __init__(self, nome:str, sobrenome:str):
        self.__primeiroNome = nome
        self.__ultimoNome = sobrenome
        self.__contas = list()
    def adicionarConta(self, conta:Conta) -> None:
        self.__contas.append(conta)
    def getConta(self, indice:int)-> Conta:
        if indice < len(self.__contas):
            return self.__contas[indice]
        else:
            return None
    def getNumeroContas(self) -> int:
        return len(self.__contas)
    @property
    def primeiroNome(self) -> str:
        return self.__primeiroNome
    @property
    def sobreNome(self) -> str:
        return self.__ultimoNome
    def __str__(self) -> str:
        testo1 = f'Nome: {self.__primeiroNome}, Sobrenome: {self.__ultimoNome}\n'
        texto2 = 'Contas: \n'
        for i in range(len(self.__contas)):
            conta = self.__contas[i]
            texto = conta.__str__() + '\n'
            texto2 += texto
        return testo1 + texto2
