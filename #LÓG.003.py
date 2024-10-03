#LÓG.003

def calcular_media(notas):
    media = sum(notas) / len(notas)
    
    if media < 3:
        return media, "Retido"
    elif media < 6:
        return media, "Recuperação"
    else:
        return media, "Aprovado"

def receber_notas():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    return notas

def main():
    nome = input("Digite o nome do aluno: ")
    notas = receber_notas()
    if notas:
        media, status = calcular_media(notas)
        print(f"Aluno: {nome} - Média: {media:.2f} - Status: {status}")

if __name__ == "__main__":
    main()
