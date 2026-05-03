import os
os.system("cls")

def main():
    produtos = []
    vendas = []

    while True:
        print("\n=== SISTEMA DE LOJA SIMPLES ===")
        print("1. Cadastrar Produto"             )
        print("2. Realizar Venda"                )
        print("3. Gerar Relatório"               )
        print("4. Salvar Relatório em Arquivo"   )
        print("5. Sair"                          )
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto(produtos)
        elif opcao == '2':
            realizar_venda(produtos, vendas)
        elif opcao == '3':
            gerar_relatorio(vendas)
        elif opcao == '4':
            salvar_relatorio(vendas)
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def cadastrar_produto(lista_produtos):
    try:
        nome = input("Nome do produto: ").strip()
        if not nome or any(p['nome'].lower() == nome.lower() for p in lista_produtos):
            print("Erro: Nome inválido ou produto já cadastrado.")
            return

        preco = float(input("Preço: R$ "))
        if preco <= 0:
            print("Erro: O preço deve ser maior que zero.")
            return

        estoque = int(input("Estoque inicial: "))
        if estoque < 0:
            print("Erro: O estoque não pode ser negativo.")
            return

        novo_produto = {"nome": nome, "preco": preco, "estoque": estoque}
        lista_produtos.append(novo_produto)
        print(f"Produto '{nome}' cadastrado com sucesso!")
        
    except ValueError:
        print("Erro: Entrada inválida. Digite números para preço e estoque.")


def calcular_venda(produto, quantidade):
    valor_bruto = produto['preco'] * quantidade
    desconto = valor_bruto * 0.05 if quantidade > 10 else 0.0
    valor_final = valor_bruto - desconto
    
    return {
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final
    }

def realizar_venda(produtos, vendas):
    if not produtos:
        print("Não há produtos cadastrados.")
        return

    nome_cliente = input("Nome do cliente: ").strip()
    if not nome_cliente:
        print("Erro: Nome do cliente é obrigatório.")
        return

    print("\n--- Produtos Disponíveis ---")
    for i, p in enumerate(produtos):
        print(f"{i}. {p['nome']} - R$ {p['preco']:.2f} (Estoque: {p['estoque']})")

    try:
        indice = int(input("Selecione o índice do produto: "))
        selecionado = produtos[indice]
        
        qtd = int(input(f"Quantidade desejada de {selecionado['nome']}: "))
        
        if 0 < qtd <= selecionado['estoque']:
            resultado = calcular_venda(selecionado, qtd)
            
            selecionado['estoque'] -= qtd
            
            venda_registro = {
                "cliente": nome_cliente,
                "produto": selecionado['nome'],
                "quantidade": qtd,
                **resultado
            }
            vendas.append(venda_registro)
            print("Venda realizada com sucesso!")
        else:
            print("Erro: Estoque insuficiente ou quantidade inválida.")
            
    except (ValueError, IndexError):
        print("Erro: Seleção ou quantidade inválida.")


def gerar_relatorio(vendas):
    if not vendas:
        print("Nenhuma venda realizada ainda.")
        return

    print("\n=== RELATÓRIO DE VENDAS ===")
    total_arrecadado = 0
    for v in vendas:
        print(f"Cliente: {v['cliente']} | Produto: {v['produto']}")
        print(f"Qtd: {v['quantidade']} | Bruto: R$ {v['valor_bruto']:.2f}")
        print(f"Desconto: R$ {v['desconto']:.2f} | Final: R$ {v['valor_final']:.2f}")
        print("-" * 30)
        total_arrecadado += v['valor_final']
    
    print(f"TOTAL ARRECADADO PELA LOJA: R$ {total_arrecadado:.2f}")

def salvar_relatorio(vendas):
    if not vendas:
        print("Não há vendas para salvar.")
        return
    
    try:
        nome_arquivo = "relatorio_vendas.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("=== RELATÓRIO DE VENDAS ===\n")
            total = 0
            for v in vendas:
                f.write(f"Cliente: {v['cliente']}\n")
                f.write(f"Produto: {v['produto']} - Qtd: {v['quantidade']}\n")
                f.write(f"Valor Final: R$ {v['valor_final']:.2f}\n")
                f.write("-" * 20 + "\n")
                total += v['valor_final']
            f.write(f"Total Geral: R$ {total:.2f}")
        print(f"Relatório salvo com sucesso em: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


if __name__ == "__main__":
    main()
