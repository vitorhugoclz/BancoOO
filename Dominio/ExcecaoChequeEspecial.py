'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015'''
class ExcecaoChequeEspecial(Exception):
    def __init__(self, mensagem:str, deficit:float):
        self.__mensagem = mensagem
        self.__deficit = deficit

    def getDeficit(self) -> float:
        return self.__deficit

    def getMessage(self) -> str:
        return self.__mensagem

    def __str__(self):
        return self.__mensagem + f'Saldo: {self.__deficit}'