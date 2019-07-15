from Dominio.ExcecaoChequeEspecial import ExcecaoChequeEspecial


class Conta:
    def __init__(self, saldoInicial:float):
        self._saldo = saldoInicial

    def getSaldo(self) -> float:
        return self._saldo
    def depositar(self, valorDeposito:float) -> bool:
        self.saldo += valorDeposito
        return True
    def sacar(self, valorSaque:float) -> None:
        if self._saldo < valorSaque:
            raise ExcecaoChequeEspecial("Saldo Insuficiente", self._saldo - valorSaque)
        self._saldo -= valorSaque

    def __str__(self):
        return f'Saldo: {self._saldo}'