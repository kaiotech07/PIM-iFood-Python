restaurantes = ["Burguer King", "McDonalds","PizzaHut"]
menu_bk = ["Combo Whopper - R$29,90", "Combo Duplo Cheddar - R$25,90", "Combo King Costela - R$35,90"]
menu_mc = ["Combo BigMac - R$29,90", "Combo BigTasty - R$35,90", "Combo Quarteirão - R$25,90"]
menu_ph = ["Pizza Grande - R$65,00", "Pizza Média - R$40,90", "Brotinho - R$24,90"]
pedidos = []
valores = []

def cancelar_pedido():
    while True:
        resposta = input("Deseja realmente cancelar o pedido? [S/N]: ").lower()
        print("========================================")

        if resposta != "n" and resposta != "s":
            print(">>>> Por favor responda com [S/N].")
            continue
        elif resposta == "n":
            print(">>>> Retornando ao menu")
            print("========================================")
            break
        else:
            print(">>>> Pedido cancelado.")
            print(">>>> Finalizando programa.")
            exit()

def pagamento():
    print("========== FORMA DE PAGAMENTO ==========")
    print("1 - Cartão Débito/Crédito")
    print("2 - PIX")
    print("3 - Voucher(Alimentação/Refeição)")
    print("4 - Dinheiro")
    print("========================================")
    resposta = input()

    if resposta == "1":
        forma_de_pagamento = "Cartão Débito/Crédito"
    elif resposta == "2":
        forma_de_pagamento = "PIX"
    elif resposta == "3":
        forma_de_pagamento = "Voucher(Alimentação/Refeição)"
    else:
        forma_de_pagamento = "Dinheiro"
    
    return forma_de_pagamento

def concluir_pedido():
    while True:

        if len(pedidos) <= 0:
            print("========================================")
            print(">>>> ERRO! O carrinho está vazio.")
            print(">>>> Retornando ao menu.")
            print("========================================")
            break
        else:
            resposta = input("Deseja realmente concluir o pedido? [S/N]: ").lower()
            print("========================================")

            if resposta != "n" and resposta != "s":
                print(">>>> Por favor responda com [S/N].")
                continue
            elif resposta == "n":
                print(">>>> Operação cancelada.")
                print(">>>> Retornando ao menu.")
                print("========================================")
                break
            else:
                forma_de_pagamento = pagamento()
                print("========== RELATÓRIO DO PEDIDO ==========")

                for index,pedido in enumerate(pedidos):
                    print(f"{pedido} - R${valores[index]}")

                print(f"Total: R${sum(valores):.2f}")
                print(f"Forma de pagamento: {forma_de_pagamento}")
                print("Status: Em preparação")
                print("========================================")
                print(">>>> Pedido realizado com sucesso")
                print(">>>> Finalizando programa")
                exit()

def ver_carrinho():
    print("=============== CARRINHO ===============")
    if len(pedidos) <= 0:
        print("Carrinho vazio.")
    else:
        for index,pedido in enumerate(pedidos):
            print(f"{pedido} - R${valores[index]}")

        print(f"Total: R${sum(valores):.2f}")
    print("========================================")

def montar_pedido (escolha_rest):
    if escolha_rest == "1":
        while True:
            print("========== MENU BURGUER KING ==========")

            for index,combos in enumerate(menu_bk):
                print(f"{index+1} - {combos}")

            print("========================================")

            escolha_lanche = input()

            print("========================================")

            if escolha_lanche not in ["1", "2", "3"]:
                print(">>>> Opção inválida")
                print("========================================")
                continue
            else:
                break

        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print(">>>> Quantidade inválida")
                print("========================================")
                return
        except:
            print("========================================")
            print(">>>> Digite um número válido")
            print("========================================")
            return

        if escolha_lanche == "1":
            pedidos.extend(["Combo Whopper"] * quantidade)
            valores.extend([29.90] * quantidade)
        elif escolha_lanche == "2":
            pedidos.extend(["Combo Cheddar Duplo"] * quantidade)
            valores.extend([25.90] * quantidade)
        else:
            pedidos.extend(["Combo King Costela"] * quantidade)
            valores.extend([35.90] * quantidade)

    elif escolha_rest == "2":
        while True:
            print("============ Menu McDonalds ============")

            for index,combos in enumerate(menu_mc):
                print(f"{index+1} - {combos}")
            
            print("========================================")

            escolha_lanche = input()

            print("========================================")
                
            if escolha_lanche not in ["1", "2", "3"]:
                print(">>>> Opção inválida")
                print("========================================")
                continue
            else:
                break

        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print(">>>> Quantidade inválida")
                print("========================================")
                return
        except:
            print("========================================")
            print(">>>> Digite um número válido")
            print("========================================")
            return

        if escolha_lanche == "1":
            pedidos.extend(["Combo BigMac"] * quantidade)
            valores.extend([29.90] * quantidade)
        elif escolha_lanche == "2":
            pedidos.extend(["Combo Cheddar BigTasty"] * quantidade)
            valores.extend([35.90] * quantidade)
        else:
            pedidos.extend(["Combo Quarteirão"] * quantidade)
            valores.extend([25.90] * quantidade)
    
    else:
        while True:
            print("============ MENU PIZZA HUT ============")

            for index,combos in enumerate(menu_ph):
                print(f"{index+1} - {combos}")
            
            print("========================================")

            escolha_lanche = input()

            print("========================================")
            
            if escolha_lanche not in ["1", "2", "3"]:
                print(">>>> Opção inválida")
                print("========================================")
                continue
            else:
                break

        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print(">>>> Quantidade inválida")
                print("========================================")
                return
        except:
            print("========================================")
            print(">>>> Digite um número válido")
            print("========================================")
            return

        if escolha_lanche == "1":
            pedidos.extend(["Pizza Grande"] * quantidade)
            valores.extend([65.00] * quantidade)

        elif escolha_lanche == "2":
            pedidos.extend(["Pizza Média"] * quantidade)
            valores.extend([40.90] * quantidade)
        else:
            pedidos.extend(["Brotinho"] * quantidade)
            valores.extend([24.90] * quantidade)
    
    print("========================================")
    print(">>>>> Itens adicionado ao carrinho")
    print(">>>>> Retornando ao menu")
    print("========================================")


def fazer_pedido():
    while True:
        print("============= RESTAURANTES =============")

        for index, rest in enumerate(restaurantes):
            print(f"{index+1} - {rest}")

        print("========================================")

        escolha_rest = input()
        
        print("========================================")

        if escolha_rest not in ["1", "2", "3"]:
            print(">>>> Opção inválida")
            print("========================================")
            continue
        else:
            break
    montar_pedido(escolha_rest)

def escolha_menu(escolha):
    if escolha == "1":
        fazer_pedido()
    elif escolha == "2":
        ver_carrinho()
    elif escolha == "3":
        concluir_pedido()
    elif escolha == "4":
        cancelar_pedido()
    else:
        print(">>>> Opção inválida")
        print("========================================")

def main():
    print("======= SISTEMA DE PEDIDOS IFOOD =======")
    print("1 - Fazer pedido")
    print("2 - Ver carrinho")
    print("3 - Concluir pedido")
    print("4 - Cancelar pedido")
    print("========================================")

    escolha = input()

    print("========================================")

    escolha_menu(escolha)

while True:
    main()