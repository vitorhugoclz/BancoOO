from Dominio.Conta import Conta
from Dominio.ExcecaoChequeEspecial import ExcecaoChequeEspecial
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015'''
class ContaCorrente(Conta):
    def __init__(self, valorInicial: float, protecao=0.0):
        super().__init__(valorInicial)
        self.__chequeEspecial = protecao


    def getChequeEspecial(self) -> float:
        return self.__chequeEspecial

    def sacar(self, valor:float) -> None:
        if self.__chequeEspecial == 0.0 and self._saldo < valor:
            raise ExcecaoChequeEspecial("Não há Cheque Especial", self._saldo - valor)
        if self.__chequeEspecial + self._saldo < valor:
            raise ExcecaoChequeEspecial("Saldo Insuficiente no Cheque Especial",
                                        self.__chequeEspecial + self._saldo - valor)
        if self._saldo > valor:
            self._saldo -= valor
        else:
            self.__chequeEspecial -= valor - self._saldo
            self._saldo -= valor

    def __str__(self):
        return f'Conta do Tipo Corrente:\nSaldo: {self._saldo}' + f'\nCheque Especial: {self.__chequeEspecial}'
