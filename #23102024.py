#23102024
#Colégio Irene Branco - Téc. em Sistemas
#ProfessorÇ: Orlando Gomes
#Autor: Isabelle S. Goffredo

def calcular_frete(peso):
    if 0<= peso <= 100:
        return 9.00
    elif 101 <= peso <= 400:
        return 18.00
    elif 601 <= peso <= 5000:
        return 30.00
    else:
        return None
    
def main():
    try: 
        valor_unitario = float(input("DIgite o valor unitário do produto: R$"))
        quantidade = int(input("Digite a quantidade do produto: "))
        peso = float(input("Digite o peso do produto (Em gramas): "))
        
        frete = calcular_frete(peso)
        
        if frete is not None:
            total = (valor_unitario * quantidade) + frete
            print(f"\nValor unitário: R${valor_unitario:.2f}")
            print(f"Quantidade: {quantidade}")
            print(f"Peso: {peso} gramas")
            print(f"Total a pagar: R$ {total:.2f}")
        else:
            print("Peso fora das faixas definidas para cálculo de frete.")
            
    except ValueError:
        print("Por favor, insira valores válidos.")
        
if __name__ == "__main__":
    main()