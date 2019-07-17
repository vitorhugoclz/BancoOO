from Dominio.ContaPoupanca import ContaPoupanca
from Dominio.ContaCorrente import ContaCorrente
from Dominio.Conta import Conta
from Dominio.Cliente import Cliente
from Dominio.Banco import Banco
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015
'''

class RelatorioClientes:
    '''
    utiliza o construtor default do python ja que não
    possui atributos para serem inicializados
    '''
    
    def geraRelatorio(self):
        '''
        chama o singleton Banco
        '''
        banco = Banco()

        '''
        gera os relatorios dos clientes do banco
        '''
        print('\t\t\tRelatorio de Clientes:\n')
        print('\t\t\t================')
        for i in range(banco.getNumeroClientes()):
            cliente = banco.getCliente(i)
            print(cliente)
