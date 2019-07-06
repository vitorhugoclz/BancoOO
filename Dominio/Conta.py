class Conta:
    def __init__(self, saldoInicial:float):
        self._saldo = saldoInicial
    @property
    def saldo(self) -> float:
        return self._saldo
    def depositar(self, valorDeposito:float) -> bool:
        self.saldo += valorDeposito
        return True
    def sacar(self, valorSaque:float) -> bool:
        if self._saldo - valorSaque < 0:
            return False
        self._saldo -= valorSaque
        return True
    def __str__(self):
        return f'Saldo: {self._saldo}'