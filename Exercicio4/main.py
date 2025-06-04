# [EXIGÊNCIA DE CÓDIGO 1 de 8]
print("Bem vindo à loja de Livros do Felipe Eduardo Laurentino Ribeiro")

# [EXIGÊNCIA DE CÓDIGO 2 de 8]
lista_livros = []
id_global = 0

# [EXIGÊNCIA DE CÓDIGO 3 de 8]
def cadastrar_livro(id):
    print("-----------------------------------------------------------------")
    print("--------------------Menu de Cadastro-----------------------------")
    nome = input("Qual o nome do livro: ")
    autor = input("Qual o autor do livro: ")
    editora = input("Qual a editora do livro: ")

    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livros.append(livro)

    print("Livro cadastrado com sucesso!")
    print(f"ID: {id}")
    print(f"Nome: {nome}")
    print(f"Autor: {autor}")
    print(f"Editora: {editora}")

# [EXIGÊNCIA DE CÓDIGO 4 de 8]
def consultar_livro():
    while True:
        print("-----------------------------------------------------------------")
        print("--------------------Menu de Consulta-----------------------------")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu principal")
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            for livro in lista_livros:
                print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
        elif opcao == "2":
            id_consulta = int(input("Digite o ID do livro: "))
            encontrado = False
            for livro in lista_livros:
                if livro["id"] == id_consulta:
                    print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
                    encontrado = True
            if not encontrado:
                print("Livro com esse ID não encontrado.")
        elif opcao == "3":
            autor_consulta = input("Digite o nome do autor: ")
            encontrado = False
            for livro in lista_livros:
                if livro["autor"].lower() == autor_consulta.lower():
                    print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
                    encontrado = True
            if not encontrado:
                print("Nenhum livro encontrado para esse autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

# [EXIGÊNCIA DE CÓDIGO 5 de 8]
def remover_livro():
    while True:
        try:
            id_remover = int(input("Digite o ID do livro a ser removido: "))
            for livro in lista_livros:
                if livro["id"] == id_remover:
                    lista_livros.remove(livro)
                    print("Livro removido com sucesso.")
                    return
            print("Id inválido. Tente novamente.")
        except ValueError:
            print("Digite um número válido para o ID.")

# [EXIGÊNCIA DE CÓDIGO 6 de 8 e 7 de 8]
while True:
    print("-----------------------------------------------------------------")
    print("------------------------Menu Principal---------------------------")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")
    opcao_menu = input("Escolha a opção desejada: ")

    if opcao_menu == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_menu == "2":
        consultar_livro()
    elif opcao_menu == "3":
        remover_livro()
    elif opcao_menu == "4":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
