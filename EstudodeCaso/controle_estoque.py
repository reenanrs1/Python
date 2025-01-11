# Sistema de Controle de Estoque de Loja de eletrônicos

# Dicionário para armazenar os produtos
estoque = {}

#Função para mostrar o menu
def mostrar_menu():
    print("\n=== Sistema de Controle de Estoque ===")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Excluir Produto")
    print("4. Visualizar Estoque")
    print("5. Sair do Sistema")

#Função para adicionar produto
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    if nome in estoque:
        print("Produto já existe no estoque!")
    else:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        estoque[nome] = {"preco": preco, "quantidade": quantidade}
        print(f"Produto '{nome}' adicionado com sucesso!")

#Função para atualizar produto
def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    if nome in estoque:
        preco = float(input("Digite o novo preço do produto: "))
        quantidade = int(input("Digite a nova quantidade em estoque: "))
        estoque[nome]["preco"] = preco
        estoque[nome]["quantidade"] = quantidade
        print(f"Produto '{nome}' atualizado com sucesso!")
    else:
        print("Produto não encontrado no estoque!")

#Função para excluir produto
def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ")
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' excluído com sucesso!")
    else:
        print("Produto não encontrado no estoque!")

#Função para visualizar estoque
def visualizar_estoque():
    if not estoque:
        print("O estoque está vazio!")
    else:
        print("\n=== Estoque Atual ===")
        for nome, detalhes in estoque.items():
            print(f"Produto: {nome}, Preço: R${detalhes['preco']:.2f}, Quantidade: {detalhes['quantidade']}")

#Função principal
def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()