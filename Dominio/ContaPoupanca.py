from Dominio.Conta import Conta
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015'''
class ContaPoupanca(Conta):
    def __init__(self, saldoInicial:float, taxaJuros:float) -> object:
        super().__init__(saldoInicial)
        self.__taxaJuros = taxaJuros
    def __str__(self):
        return f'Conta do Tipo Poupanca:\nSaldo: {self._saldo} \nTaxa de Juros: {self.__taxaJuros}%'
'''conta = ContaPoupanca(500.0, 8.0)
print(conta)'''