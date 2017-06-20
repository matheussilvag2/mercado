#coding: utf-8
from produto import produto

total = 0.0

class cadastrar:
    def cadastrarProduto(self,listaproduto):

        while True:
            print "====Cadastros de Produtos====\n"
            nomeProduto = raw_input("Digite o nome do produto: ")
            precoProduto = float(raw_input("Digite o preço unitário do produto: "))
            if precoProduto <= 0:
                print "numero negativo é invalido"
                continue
            tipoProduto = raw_input("Digite o tipo do produto: ")
            estoqueProduto = int(raw_input("Digite a quantidade no estoque: "))

            existe = False
            if len(listaproduto) == 0:
                produ = produto(nomeProduto, precoProduto, tipoProduto, estoqueProduto)
                listaproduto.append(produ)
                print "\n%i %s(s) cadastrado(s) com sucesso.\n" % (estoqueProduto, nomeProduto)
            else:
                for i in range(len(listaproduto)):
                    if listaproduto[i].getNome() == nomeProduto:
                        existe = True
                        print "Produto ja cadastrado"

                if existe == False:
                    produ = produto(nomeProduto, precoProduto, tipoProduto, estoqueProduto)
                    listaproduto.append(produ)
                    print "\n%d %s cadastrado(s) com sucesso.\n" % (estoqueProduto, nomeProduto)

            op1 = raw_input("Deseja cadastrar outro produto? ")

            if op1.upper() == "SIM":
                continue
            elif op1.upper() == "NAO":
                break
            else:
                print "Invalido!"
        return listaproduto




class vender:
    def venderProduto(self,listaproduto1):
        global total
        global restante
        while True:
            print "====Venda de Produtos====\n"
            nomeProduto = raw_input("Digite o nome do produto: ")
            existe = False
            for i in range(len(listaproduto1)):
                if listaproduto1[i].getNome() == nomeProduto:
                    existe = True
                    print "%s(%s): R$%.2f" % (listaproduto1[i].getNome(), listaproduto1[i].getTipo(), listaproduto1[i].getPreco())
                    quantidade = int(raw_input("digite a quantidade que deseja vender: "))
                    if quantidade <= 0:
                        print("numero negativo é invalido")
                        continue
                    if listaproduto1[i].getEstoque() >= quantidade:
                        listaproduto1[i].setEstoque(listaproduto1[i].getEstoque() - quantidade)
                        r = listaproduto1[i].getPreco() * quantidade
                        total += r
                        print("total arrecadado: R$%.2f" % (r))
                    else:
                        print "Não é possível vender pois não há %s suficiente" % (nomeProduto)

            if existe == False:
                print "%s nao cadastrado no sistema" % (nomeProduto)
                break

            op = raw_input("Deseja vender outro Produto? ")
            if op.upper() == "SIM":
                continue
            elif op.upper() == "NAO":
                break
            else:
                print "Invalido"


        return listaproduto1




class imprimir:
    def imprimirBalanco(self,listaproduto2):
        total_arrecadado = 0.0
        print "==== Impressao de Balanco ====\n"
        print "Produtos cadastrados: \n"
        for i in range(len(listaproduto2)):
            print "%d) %s(%s): R$%.2f" % (i + 1, listaproduto2[i].getNome(), listaproduto2[i].getTipo(), listaproduto2[i].getPreco())
            print"\tRestante: %d" % (listaproduto2[i].getEstoque())
            total_arrecadado += listaproduto2[i].getPreco() * listaproduto2[i].getEstoque()
        print "Total arrecadado em vendas: R$%.2f\n" % (total)
        print "Total que pode ser arrecadado : R$ %.2f" % (total_arrecadado)

        return listaproduto2