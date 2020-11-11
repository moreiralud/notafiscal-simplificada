
clientes=["Marcelo", "Joana D'arc", "Maria de Fátima"]
produtos= [1000.50, 120.10, 999.99]
imposto=[0.010, 0.0]
menuProdutos=\
("""
Por favor, digite a quantidade desejada:

*** Lista de itens disponíveis *** 

computador:
preco:1000.50

mouse:
preco:120.00

Monitor LCD:
preco:999.99

""")
nomeCliente= input("Digite o nome do cliente: ")

if (nomeCliente != clientes[0]) & (nomeCliente != clientes[1]) & (nomeCliente != clientes[2]):
    print("Cliente não encontrado!")
else:
    print("Clinte  encontrado! ")

    print(menuProdutos)

    quantProdutoComputador = float(input("Coloque a quantidade de computadores que você deseja: "))
    quantProdutoMouse = float(input("Coloque a quantidade de mouses que você deseja: "))
    quantProdutoMonitor = float(input("Coloque a quantidade de monitores que você deseja: "))

    valorImpostoComputador = produtos[0] * imposto[0]
    valorImpostoMouse = produtos[1] * imposto[0]
    valorImpostoMonitor = produtos[2] * imposto[0]


    valorFinalComputador = (valorImpostoComputador + produtos[0]) * quantProdutoComputador
    valorFinalMouse = (valorImpostoMouse + produtos[1]) * quantProdutoMouse
    valorFinalMonitor = valorImpostoMonitor + produtos[2] * quantProdutoMonitor

    valorTotal = (float(valorFinalComputador) * float(quantProdutoComputador) ) + \
                 (float(valorFinalMouse) * float(quantProdutoMouse)) +\
                 (float(valorFinalMonitor) * float(quantProdutoMonitor))

    print(
    """ ==============================
Nota fiscal
Cliente: {}
Itens comprados
Computador 1000,50  - Quantidade: {:.2f} – Valor do imposto: {:.2f} Valor Total: {:.2f}
Mouse 120,10 – Quantidade {:.2f} – Valor do imposto: {:.2f} – Valor Total: {:.2f}
Monitor LCD 999,99 - Quantidade: {:.2f} – Valor do imposto: {:.2f} Valor Total: {:.2f}

Total da Nota: {:.2f}
Volte Sempre!
=============================""".format(nomeCliente, quantProdutoComputador, valorImpostoComputador,
                                        valorFinalComputador, quantProdutoMouse, valorImpostoMouse, valorFinalMouse,
                                        quantProdutoMonitor, valorImpostoMonitor , valorFinalMonitor,
                                        valorTotal))
print("""Deseja continuar? 
                     Aperte 0
                     Deseja sair? 
                     Aperte 1:
                                           """)
continuar = int(input())

if continuar == 0:
    print(menuProdutos)
    quantProdutoComputador = float(input("Coloque a quantidade de computadores que você deseja: "))
    quantProdutoMouse = float(input("Coloque a quantidade de mouses que você deseja: "))
    quantProdutoMonitor = float(input("Coloque a quantidade de monitores que você deseja: "))

else:
    exit( )