from Dominio.Cliente import Cliente

class Banco():
    __banco = None
    def __init__(self):
        self.__clientes = list()
    @staticmethod
    def getBanco():
        if not Banco.__banco:
            Banco.__banco = Banco()
        return Banco.__banco
    def adicionarCliente(self, primeiroNome:str, ultimoNome:str) -> None:
        cliente = Cliente(primeiroNome, ultimoNome)
        self.__clientes.append(cliente)

    def getCliente(self, indice:int) -> Cliente:
        return self.__clientes[indice]

    def getNumeroClientes(self) -> int:
        return len(self.__clientes)