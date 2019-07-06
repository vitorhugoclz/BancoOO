/*
 * Esta classe cria um programa para testar as classes do projeto banco.
 * Ela cria um conjunto de clientes, com algumas contas,
 * e gera um relatoorio do saldo atual em conta.
 */

import banco.dominio.*;
import banco.relatorios.RelatorioClientes;

public class TestaBanco {

  public static void main(String[] args) {
    Banco     banco = Banco.getBanco();
    Cliente cliente;
    RelatorioClientes relatorio = new RelatorioClientes();

    // Cria os clientes e suas contas
    banco.adicionarCliente("Jane", "Simms");
    cliente = banco.getCliente(0);
    cliente.adicionarConta(new ContaPoupanca(500.00, 0.05));
    cliente.adicionarConta(new ContaCorrente(200.00, 400.00));

    banco.adicionarCliente("Owen", "Bryant");
    cliente = banco.getCliente(1);
    cliente.adicionarConta(new ContaCorrente(200.00));

    banco.adicionarCliente("Tim", "Soley");
    cliente = banco.getCliente(2);
    cliente.adicionarConta(new ContaPoupanca(1500.00, 0.05));
    cliente.adicionarConta(new ContaCorrente(200.00));

    banco.adicionarCliente("Maria", "Soley");
    cliente = banco.getCliente(3);
    // Maria e Tim possuem um conta corrente compartilhada
    cliente.adicionarConta(banco.getCliente(2).getConta(1));
    cliente.adicionarConta(new ContaPoupanca(150.00, 0.05));

    // gerar o relatorio
    relatorio.geraRelatorio();
  }
}
