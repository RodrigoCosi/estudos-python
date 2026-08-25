from conexao import conectar
from services.produto_service import ( 
    listar_produtos,
    cadastrar_produto,
    atualizar_produto,
    excluir_produto,
    buscar_produto
)

while True:
    print("\n ---CONTROLE DE ESTOQUE---")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Excluir produto")
    print("5 - Buscar produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ").strip()
        descricao = input("Descrição: ").strip()

        if not nome:
            print("Erro: O nome do produto não pode estar vazio.")
            continue

        try:
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
        except ValueError:
            print("Erro: Quantidade e preço devem ser números válidos.")
            continue

        if quantidade < 0:
            print("Erro: A quantidade não pode ser negativa.")
            continue

        if preco <= 0:
            print("Erro: O preço deve ser maior que zero.")
            continue

        cadastrar_produto(nome, descricao, quantidade, preco)
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
       produtos = listar_produtos()
       print("\n---PRODUTOS---")

       for produto in produtos:
           print(
            f"ID: {produto[0]} | "
            f"Nome: {produto[1]} | "
            f"Quantidade: {produto[3]} | "
            f"Preço: R$ {produto[4]}"
           )

    elif opcao == "3":
        try:
            id_produto = int(input("Digite o ID do produto que deseja atualizar: "))

            if id_produto <= 0:
                print("Erro: O ID do produto deve ser maior que zero.")
                continue

            nome= input("Digite o novo nome do produto: ").strip()
            descricao = input("Digite a nova descrição do produto: ").strip()

            if not nome:
                print("Erro: O nome do produto não pode estar vazio.")
                continue

            quantidade = int(input("Digite a nova quantidade do produto: "))
            preco = float(input("Digite o novo preço do produto: "))

            if quantidade < 0:
                print("Erro: A quantidade não pode ser negativa.")
                continue

            if atualizar_produto(id_produto, nome, descricao, quantidade, preco):
                print("Produto atualizado com sucesso!")
            else:
                print("Erro: Produto não encontrado ou nenhum campo foi alterado.")

        except ValueError:
            print("Erro: O ID do produto, quantidade e preço devem ser números válidos.")
            continue

        atualizar_produto(id_produto, nome, descricao, quantidade, preco)

        print("Produto atualizado com sucesso!")

    elif opcao == "4":
        try:
            id_produto = int(input("Digite o ID do produto que deseja excluir: "))
        except ValueError:
            print("Erro: O ID do produto deve ser um número válido.")
            continue

        if excluir_produto(id_produto):
                    print("Produto excluído com sucesso!")
        else:
            print("Erro: Produto não encontrado.")

    elif opcao == "5":
        nome = input("Digite o nome do produto que deseja buscar: ").strip()

        if not nome:
            print("Erro: O nome do produto não pode estar vazio.")
            continue

        produtos = buscar_produto(nome)

        if produtos:
            print("\n---PRODUTOS ENCONTRADOS---")
            for produto in produtos:
                print(
                    f"ID: {produto[0]} | "
                    f"Nome: {produto[1]} | "
                    f"Quantidade: {produto[3]} | "
                    f"Preço: R$ {produto[4]}"
                )
        else:
            print("Nenhum produto encontrado com esse nome.")


    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")