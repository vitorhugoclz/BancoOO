'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015
'''

class ExcecaoChequeEspecial(Exception):
    '''
    ExcecaoChequeEspecial herda de Exception
    '''
    
    def __init__(self, mensagem:str, deficit:float):
        '''
        inicializa os atributos da classe
        '''
        self.__mensagem = mensagem
        self.__deficit = deficit

    def getDeficit(self) -> float:
        '''
        retorna o atributo deficit
        '''
        return self.__deficit

    def getMessage(self) -> str:
        '''
        retorna o atributo mensagem
        '''
        return self.__mensagem

    def __str__(self):
        '''
        sobreescreve o metodo __str__ que funciona como um toString do Java
        retorna uma String contendo as informações do objeto
        '''
        return self.__mensagem + f'Saldo: {self.__deficit}'
