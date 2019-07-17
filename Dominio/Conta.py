from Dominio.ExcecaoChequeEspecial import ExcecaoChequeEspecial
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015
'''

class Conta:
    def __init__(self, saldoInicial:float):
        '''
        inicializa os atributos da classe Conta
        '''
        self._saldo = saldoInicial

    def getSaldo(self) -> float:
        '''
        retorna o valor do atributo saldo
        '''
        return self._saldo

    def depositar(self, valorDeposito:float) -> bool:
        '''
        deposita uma quantidade passada por parametro
        na conta
        '''
        self._saldo += valorDeposito
        return True

    def sacar(self, valorSaque:float) -> None:
        '''
        saca uma determinada quantidade passada por
        parametro da conta
        '''
        if self._saldo < valorSaque:
            raise ExcecaoChequeEspecial("Saldo Insuficiente", valorSaque)
        self._saldo -= valorSaque

    def __str__(self):
        '''
        sobreescrita do metodo __str__ que funciona como o
        metodo toString do Java
        retorna uma string contendo as informações da Conta
        '''
        return f'Saldo: {self._saldo}'
