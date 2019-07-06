package banco.dominio;


import banco.dominio.Conta;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Otávio
 */
public class ContaCorrente extends Conta {

    private double chequeEspecial;

    public ContaCorrente(double saldoInicial) {
        super(saldoInicial);
    }

    public ContaCorrente(double saldoInicial, double protecao) {
        super(saldoInicial);
        this.chequeEspecial = protecao;
    }

    public double getChequeEspecial() {
        return this.chequeEspecial;
    }

    @Override
    public boolean sacar(double valorSaque) {
        if ((this.saldo - valorSaque) >= 0) {
            this.saldo = this.saldo - valorSaque;
            return true;
        } else {
            if (this.chequeEspecial > 0) {
                double diferenca = -1 * (this.saldo - valorSaque);

                if (diferenca < this.chequeEspecial) {
                    this.saldo = saldo - valorSaque;
                    this.chequeEspecial = this.chequeEspecial - diferenca;
                    return true;
                }
                return false;
            }
        }
        return false;
    }
}


