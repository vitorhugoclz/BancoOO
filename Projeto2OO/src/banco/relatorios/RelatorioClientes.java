package banco.relatorios;



import java.text.NumberFormat;
import java.util.*;
import banco.dominio.*;
import banco.dominio.Cliente;



public class RelatorioClientes {

  public void geraRelatorio() {
    NumberFormat formatoMonetario = NumberFormat.getCurrencyInstance(new Locale("pt", "BR"));

   
   Banco banco = Banco.getBanco();
   Cliente cliente;

    System.out.println("\t\t\tRelat�rio de Clientes");
    System.out.println("\t\t\t================");

    for ( int indiceCliente = 0; indiceCliente < banco.getNumeroDeClientes(); indiceCliente++ ) {
      cliente = banco.getCliente(indiceCliente);

      System.out.println();
      System.out.println("Cliente: "
			 + cliente.getUltimoNome() + ", "
			 + cliente.getPrimeiroNome());

      for ( int indiceConta = 0; indiceConta < cliente.getNumeroDeContas(); indiceConta++ ) {
	Conta conta = cliente.getConta(indiceConta);
	String  tipoConta = "";

	// Determina o tipo de conta
	if ( conta instanceof ContaPoupanca ) {
	  tipoConta = "Conta Poupanca";
	} else if ( conta instanceof ContaCorrente ) {
	  tipoConta = "Conta Corrente";
	} else {
	  tipoConta = "Tipo desconhecido de conta";
	}

	// Exibe os saldos da conta
	System.out.println("    " + tipoConta + ": Saldo atual de "
			 + formatoMonetario.format(conta.getSaldo()));
      }
    }
  }

}


