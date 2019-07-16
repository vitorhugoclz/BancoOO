from Dominio.Banco import Banco
from Dominio.Cliente import Cliente
from Dominio.Conta import Conta
from Dominio.ContaCorrente import ContaCorrente
from Dominio.ContaPoupanca import ContaPoupanca
from Relatorios.RelatorioClientes import RelatorioClientes
from Dominio.ExcecaoChequeEspecial import ExcecaoChequeEspecial
'''Trabalho feito por:
    Vitor Hugo da Costa Luz: 2018.1.08.023
    Maria Luzia Fernandes: 2018.1.08.015'''

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

#remova as aspas triplhas para testar as exececoes de saque
'''try:
    cliente = banco.getCliente(0)
    conta = cliente.getConta(0)
    conta.sacar(800.0)
except ExcecaoChequeEspecial as exc:
    print(exc)'''

'''print('\n\n\n\n');
print('Teste\n');
print(banco.getClientePorNome("Jane", "Simms"))'''
