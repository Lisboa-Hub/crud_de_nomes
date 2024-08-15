import os

# lista
nomes = []

while True:
    print(f"{"="*20} LISTA DE OPÇÕES {"="*20}\n")

    print("1 - Cadastrar um novo nome à lista")
    print("2 - Pesquisar por um nome existente na lista")
    print("3 - Alterar um nome na lista")
    print("4 - Deletar um nome da lista")
    print("5 - Sair")

    print("\n")

    opcao = input("Informe a opção desejada: ")

    os.system("cls")

    match opcao:
        case "1":
            novo_nome = input("Informe o nome a ser inserido na lista: ")
            nomes.append(novo_nome)
            os.system("cls")
        case "2":
            nome_pesquisa = input("Informe o nome que deseja pesquisar: ")
            os.system("cls")
            if nome_pesquisa in nomes:
                print(f"{nome_pesquisa} encontrado no cadastro!")
            else:
                print("Nome não encontrado!")
        case "3":
            print(f"{"-"*20} LISTA DE NOMES {"-"*20}\n")
            for nome in nomes:
                print(nome)
            print("\n")
            nome_a_alterar = input("Informe o nome que deseja alterar: ")
            nomes[nomes.index(nome_a_alterar)] = input("Informe o novo nome: ")
            os.system("cls")
            print(f"{"-"*20} LISTA DE NOMES {"-"*20}\n")
            for nome in nomes:
                print(nome)
        case "4":
            nome_a_excluir = input("Informe o nome a ser excluído: ")
            if nome_a_excluir in nomes:
                nomes.remove(nome_a_excluir)
                print(f"{"-"*20} LISTA DE NOMES {"-"*20}\n")
                for nome in nomes:
                    print(nome)
            else:
                print(
                    f"{nome_a_excluir} não pode ser excluído pois não existe no sistema.")
        case "5":
            break
        case _:
            print("Opção inválida. Por favor, escolher uma opção existente!")
