/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package banco.dominio;

import banco.*;

/**
 *
 * @author Otávio
 */
public class Cliente {

    private String primeiroNome;
    private String ultimoNome;

    private Conta contas[];
    private int numeroDeContas;

    private ContaCorrente contaCorrente;
    private ContaPoupanca contaPoupanca;

    public Cliente(String primeiroNome, String ultimoNome) {
        this.primeiroNome = primeiroNome;
        this.ultimoNome = ultimoNome;
        contas = new Conta[10];
    }

    public void adicionarConta(Conta conta) {
        this.contas[numeroDeContas++] = conta;
    }

    public Conta getConta(int indice) {
        return this.contas[indice];
    }

    public int getNumeroDeContas() {
        return numeroDeContas;
    }

    public String getPrimeiroNome() {
        return this.primeiroNome;
    }

    public String getUltimoNome() {
        return this.ultimoNome;
    }

    public ContaCorrente getContaCorrente() {
        return contaCorrente;
    }

    public void setContaCorrente(ContaCorrente contaCorrenta) {
        this.contaCorrente = contaCorrenta;
    }

    public ContaPoupanca getContaPoupanca() {
        return contaPoupanca;
    }

    public void setContaPoupanca(ContaPoupanca contaPoupanca) {
        this.contaPoupanca = contaPoupanca;
    }

}
