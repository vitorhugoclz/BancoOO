from Dominio.Cliente import Cliente
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015
'''

class Banco():
    class __Banco():
        
        '''
        classe privada para utilização do singleton
        '''
        def __init__(self):
            '''
            inicializa atributos do Banco
            '''
            self.__clientes = list()

        def adicionarCliente(self, primeiroNome: str, ultimoNome: str) -> None:
            '''
            adiciona cliente na lista de clientes do banco e recebe
            um nome e sobrenome como parametro
            '''
            cliente = Cliente(primeiroNome, ultimoNome)
            self.__clientes.append(cliente)

        def adicionarCliente2(self, cliente: Cliente) -> None:
            '''
            adiciona cliente na lista de clientes do banco e recebe
            um objeto do tipo cliente como parametro
            ''' 
            self.__clientes.append(cliente)

        def getCliente(self, indice: int) -> Cliente:
            '''
            retorna o cliente de um especifico indice
            '''
            if indice < len(self.__clientes):
                return self.__clientes[indice]
            return None

        def getClientePorNome(self, nomeCliente: str, sobrenomeCliente: str) -> Cliente:
            '''
            retorna o cliente que tenha o mesmo nome e sobrenome que os passados
            por parametro
            '''
            clienteNovo = Cliente(nomeCliente, sobrenomeCliente)
            for i in range(len(self.__clientes)):
                if self.__clientes[i] == clienteNovo:
                    return self.__clientes[i]
            return None

        def getNumeroClientes(self) -> int:
            '''
            retorna o numero de clientes do banco
            '''
            return len(self.__clientes)

    __banco = None
    def __new__(cls):
        '''
        metodo responsavel pelo controle da instanciação
        de objetos do tipo Banco
        '''
        if not Banco.__banco:
            Banco.__banco = Banco.__Banco()
        return Banco.__banco
