from Dominio.Conta import Conta
from Dominio.ExcecaoChequeEspecial import ExcecaoChequeEspecial
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015
'''

class ContaCorrente(Conta):
    '''
    ContaCorrende herda de Conta
    '''
    
    def __init__(self, valorInicial: float, protecao=0.0):
        '''
        é chamado o metodo init da classe mae passando o valorInicial
        para que ele seja inicializado
        é iniciado os atributos da classe
        '''
        super().__init__(valorInicial)
        self.__chequeEspecial = protecao


    def getChequeEspecial(self) -> float:
        '''
        retorna o valor do atributo chequeEspecial
        '''
        return self.__chequeEspecial

    def sacar(self, valor:float) -> None:
        '''
        saca um determinado valor passado por paremtro
        da contaCorrente
        '''
        if self.__chequeEspecial == 0.0 and self._saldo < valor:
            raise ExcecaoChequeEspecial("Nao há saldo suficiente e conta sem cheque especial", valor - self._saldo)
        if self.__chequeEspecial + self._saldo < valor:
            raise ExcecaoChequeEspecial("Saldo Insuficiente no Cheque Especial", valor - self._saldo)
        if self._saldo > valor:
            self._saldo -= valor
        else:
            self.__chequeEspecial -= valor - self._saldo
            self._saldo = 0.0

    def __str__(self):
        '''
        sobreescreve o metodo __str__ que funciona como o metodo toString do Java
        retorna uma String contendo as informações do objeto
        '''
        return f'Conta do Tipo Corrente:\nSaldo: {self._saldo}' + f'\nCheque Especial: {self.__chequeEspecial}'
