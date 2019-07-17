from Dominio.Banco import Banco
from Dominio.Cliente import Cliente
from Dominio.Conta import Conta
from Dominio.ContaCorrente import ContaCorrente
from Dominio.ContaPoupanca import ContaPoupanca
from Relatorios.RelatorioClientes import RelatorioClientes
from Dominio.ExcecaoChequeEspecial import ExcecaoChequeEspecial
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luiza Fernandes: 2018.1.08.015
'''

'''Nota de Observação:
    a implementação do singleton em python não necessita da utilizacao
    de um metodo getBanco(), entao podemos usar Banco() diretamente
'''

banco = Banco()
relatorio = RelatorioClientes()

# Cria dois clientes e suas contas
banco.adicionarCliente('Jane', 'Simms');
cliente = banco.getCliente(0);
cliente.setConta(ContaPoupanca(500.00, 0.05))
cliente.setConta(ContaCorrente(200.00, 500.00))

banco.adicionarCliente("Owen", "Bryant")
cliente = banco.getCliente(1)
cliente.setConta(ContaCorrente(200.00))

#testa a conta de Jane Sims (com cheque especial
cliente = banco.getCliente(0);
conta = cliente.getConta(1);
print(f"Cliente [" + cliente.getUltimoNome()
		       + ", " + cliente.getPrimeiroNome() + "]"
		       + f" Tem um saldo em conta corrente de {conta.getSaldo()}"
			 + " Com cheque especial de  R$ 500.00.")
try:
    print("Conta Corrente [Jane Simms] : Saque de R$ 150,00")
    conta.sacar(150.00)
    print("Conta Corrente [Jane Simms] : depósito de R$ 22,50")
    conta.depositar(22.50)
    print("Conta Corrente [Jane Simms] : Saque de R$ 147,62")
    conta.sacar(147.62)
    print("Conta Corrente [Jane Simms] : Saque de R$ 470,00")
    conta.sacar(470.00)
except ExcecaoChequeEspecial as e1:
    print("Exceção: " + e1.getMessage() + f" Déficit: {e1.getDeficit()}")
finally:
    print("Cliente [" + cliente.getUltimoNome() + ", " + cliente.getPrimeiroNome() + "]"
          + f" Tem um saldo em conta corrente de {conta.getSaldo()}")
#  Testa a conta corrente de Owen Bryant (sem cheque especial)

cliente = banco.getCliente(1)
conta = cliente.getConta(0)
print("Cliente [" + cliente.getUltimoNome()
		       + ", " + cliente.getPrimeiroNome() + "]"
		       + f" tem um saldo de {conta.getSaldo()}")
try:
    print("Conta Corrente [Owen Bryant] : Saque de R$ 100,00")
    conta.sacar(100.00)
    print("Conta Corrente [Owen Bryant] : depósito de R$ 25,00")
    conta.depositar(25.00)
    print("Conta Corrente [Owen Bryant] : Saque de R$ 175,00")
    conta.sacar(175.00)
except ExcecaoChequeEspecial as e1:
    print("Exceção: " + e1.getMessage()
			 + f"   Déficit: {e1.getDeficit()}")
finally:
    print("Cliente [" + cliente.getUltimoNome()
			 + ", " + cliente.getPrimeiroNome() + "]"
			 + f" Tem um saldo dem conta corrente de {conta.getSaldo()}")

print("teste de singleton")
banco2 = Banco()

#gerar o relatorio
#relatorio.geraRelatorio()
