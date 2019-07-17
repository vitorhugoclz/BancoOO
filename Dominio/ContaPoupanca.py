from Dominio.Conta import Conta
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015
'''

class ContaPoupanca(Conta):
    '''
    ContaPoupanca herda de Conta
    '''
    
    def __init__(self, saldoInicial:float, taxaJuros:float) -> object:
        '''
        é chamado o método init da classe mãe passando o saldoInicial
        para que ele seja inicializado
        inicializa os atributos da classe
        '''
        super().__init__(saldoInicial)
        self.__taxaJuros = taxaJuros
        
    def __str__(self):
        '''
        sobreescreve o metodo __str__ que funciona como o metodo toString do Java
        retorna uma String contendo as informações do objeto
        '''
        return f'Conta do Tipo Poupanca:\nSaldo: {self._saldo} \nTaxa de Juros: {self.__taxaJuros}%'
'''conta = ContaPoupanca(500.0, 8.0)
print(conta)'''
