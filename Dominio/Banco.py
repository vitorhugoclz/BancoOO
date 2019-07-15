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

    def adicionarCliente2(self, cliente:Cliente) -> None:
        self.__clientes.append(cliente)

    def getCliente(self, indice:int) -> Cliente:
        if indice < len(self.__clientes):            
            return self.__clientes[indice]
        return None
    
    def getClientePorNome(self, nomeCliente:str, sobrenomeCliente:str) -> Cliente:
        clienteNovo = Cliente(nomeCliente, sobrenomeCliente)
        for i in range(len(self.__clientes)):
            if self.__clientes[i] == clienteNovo:
                return self.__clientes[i]
        return None

    def getNumeroClientes(self) -> int:
        return len(self.__clientes)
