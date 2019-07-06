from Dominio.Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, saldoInicial:float, taxaJuros:float) -> object:
        super().__init__(saldoInicial)
        self.__taxaJuros = taxaJuros
    def __str__(self):
        return f'Conta do Tipo Poupanca:\nSaldo: {self.saldo} \nTaxa de Juros: {self.__taxaJuros}%'
'''conta = ContaPoupanca(500.0, 8.0)
print(conta)'''