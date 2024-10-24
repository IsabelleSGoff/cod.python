#22102024
#Colégio Irene Branco - Téc. em Sistemas
#Professor: Orlando Gomes
#Autor: Isabelle S. Goffredo

def calcular_icms(valor_total):

    return valor_total * 0.12

def calcular_parcelas(valor_total, num_parcelas):

    return valor_total / num_parcelas

def main():
    produtos = []
    num_itens = int(input("Digite a quantidade de itens a serem cadastrados: "))

    for i in range(num_itens):
        print(f"\nCadastro do produto {i + 1}:")
        codigo = input("Código do produto: ")
        descricao = input("Descrição do produto: ")
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário: "))

        produtos.append({
            'codigo': codigo,
            'descricao': descricao,
            'quantidade': quantidade,
            'valor_unitario': valor_unitario
        })

    valor_total = sum(produto['quantidade'] * produto['valor_unitario'] for produto in produtos)
    icms_total = calcular_icms(valor_total)

    print(f"\nValor total dos produtos: R$ {valor_total:.2f}")
    print(f"Total de ICMS (12%): R$ {icms_total:.2f}")
    
    while True:
        num_parcelas = int(input("Digite o número de parcelas (1 a 12): "))
        if 1 <= num_parcelas <= 12:
            break
        else:
            print("Número de parcelas inválido. Tente novamente.")

    valor_parcela = calcular_parcelas(valor_total + icms_total, num_parcelas)
    
    print(f"\nValor total com ICMS: R$ {valor_total + icms_total:.2f}")
    print(f"Valor de cada parcela (em {num_parcelas}x): R$ {valor_parcela:.2f}")

if __name__ == "__main__":
    main()