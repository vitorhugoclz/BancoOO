/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package banco.dominio;



/**
 *
 * @author Otávio
 */
public class Banco {
    
    
    private static Banco banco = null;

    private Cliente clientes[];
    private int numeroDeClientes;

    private Banco() {
        this.clientes =  new Cliente[10];
    }

    public static Banco getBanco() {
        if(banco == null){
            banco = new Banco();
        }
        return banco;
    }
    
    
    

    public void adicionarCliente(String primeiroNome, String ultimoNome) {
        this.clientes[numeroDeClientes++] =  new Cliente(primeiroNome, ultimoNome);
    }

    public Cliente getCliente(int indice) {
        return this.clientes[indice];
    }
    
    
    public int getNumeroDeClientes(){
        return this.numeroDeClientes;
    }

}
