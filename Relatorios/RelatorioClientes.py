from Dominio.ContaPoupanca import ContaPoupanca
from Dominio.ContaCorrente import ContaCorrente
from Dominio.Conta import Conta
from Dominio.Banco import Banco
class RelatorioClientes:
    def geraRelatorio(self):
        banco = Banco.getBanco()
        print('\t\t\tRelatorio de Clientes:\n')
        print('\t\t\t================')
        for i in range(banco.getNumeroClientes()):
            cliente = banco.getCliente(i)
            print(cliente)