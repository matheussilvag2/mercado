#coding: utf-8

from estoque import cadastrar
from estoque import vender
from estoque import imprimir

class economizaTec:
    def menuPrincipal(self):
        cadastro = cadastrar()
        venda = vender()
        balanco = imprimir()
        self.lista = []
        while True:
            print "==== Bem vindo(a) ao EconomizaTec====\n"
            print "Cadastrar um Produto: 1"
            print "Vender um Produto: 2"
            print "Imprimir Balanço: 3"
            print "Sair: 4"
            op = raw_input("\nOpcao: ")

            if op == "1":
                '''Cadastro dos produtos'''
                self.lista = cadastro.cadastrarProduto(self.lista)
            elif op == "2":
                '''Vender os produtos'''
                self.lista = venda.venderProduto(self.lista)
            elif op == "3":
                '''Imprimir Balanço'''
                self.lista = balanco.imprimirBalanco(self.lista)
            elif op == "4":
                print "\nObrigado!\nVolte Sempre!"
                break
            else:
                print "\nOpcao Invalida!!!\n"

mercado = economizaTec()
mercado.menuPrincipal()