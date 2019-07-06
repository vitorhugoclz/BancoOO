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
public class ContaPoupanca extends Conta{
    
    private double taxaJuros;
    
    public ContaPoupanca(double saldoInicial, double taxa) {
        super(saldoInicial);
        this.taxaJuros =  taxa;
    }
 
}
