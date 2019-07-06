from Dominio.Banco import Banco
from Dominio.Cliente import Cliente
from Dominio.Conta import Conta
from Dominio.ContaCorrente import ContaCorrente
from Dominio.ContaPoupanca import ContaPoupanca
from Relatorios.RelatorioClientes import RelatorioClientes

banco = Banco.getBanco()
relatorio = RelatorioClientes()

# Cria os clientes e suas contas
banco.adicionarCliente("Jane", "Simms");
cliente = banco.getCliente(0);
cliente.adicionarConta(ContaPoupanca(500.00, 0.05))
cliente.adicionarConta(ContaCorrente(200.00, 400.00))

banco.adicionarCliente("Owen", "Bryant")
cliente = banco.getCliente(1)
cliente.adicionarConta(ContaCorrente(200.00))

banco.adicionarCliente("Tim", "Soley")
cliente = banco.getCliente(2)
cliente.adicionarConta(ContaPoupanca(1500.00, 0.05))
cliente.adicionarConta(ContaCorrente(200.00))
banco.adicionarCliente("Maria", "Soley");
cliente = banco.getCliente(3);
cliente.adicionarConta(banco.getCliente(2).getConta(1))
cliente.adicionarConta(ContaPoupanca(150.00, 0.05))
#gerar o relatorio
relatorio.geraRelatorio()
