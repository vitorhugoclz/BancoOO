from Dominio.Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, valorInicial: float, protecao=0.0):
        super().__init__(valorInicial)
        self.__chequeEspecial = protecao
    @property
    def chequeEspecial(self) -> float:
        return self.__chequeEspecial
    def sacar(self, valor:float) -> bool:
        if self._saldo >= valor:
            self._saldo -= valor
        elif self._saldo + self.__chequeEspecial > valor:
            self.__chequeEspecial -= (self._saldo - valor)
            self._saldo = 0
        else:
            return False
        return True
    def __str__(self):
        return f'Conta do Tipo Corrente:\nSaldo: {self._saldo}' + f'\nCheque Especial: {self.__chequeEspecial}'
'''conta = ContaCorrente(25.0, 82.0)
print(conta)'''