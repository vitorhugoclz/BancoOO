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
public class Conta {

    protected double saldo;

    public Conta(double saldoInicial) {
        this.saldo = saldoInicial;
    }

    public double getSaldo() {
        return this.saldo;
    }

    public boolean depositar(double valorDeposito) {
        this.saldo = this.saldo + valorDeposito;
        return true;
    }

    public boolean sacar(double valorSaque) {

        if ((saldo - valorSaque) >= 0) {
            this.saldo = this.saldo - valorSaque;
            return true;
        }

        return false;
    }

}
