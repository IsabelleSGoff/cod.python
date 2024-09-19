# Curso DS - Semana 23 - Objeto: conhecendo OOP - Teoria e Prática

# Criando a classe chamada Produto
class Produto:
    def __init__(self, nome, marca, preco):
        # Definindo os atributos
        self.nome = nome
        self.marca = marca
        self.preco = preco

    # Definindo Métodos
    # Método Exibir dados
    def exibir_informacoes(self):
        print(f"Nome: {self.nome} - Marca: {self.marca} - Preço: R${self.preco:.2f}")

    # Criando Método exibir 10 vezes
    def exibir_10vezes(self):
        n = 1
        while n <= 10:
            print("Nome - ", n, "  ", self.nome)
            n += 1

    # Criando Método Calcular Juros
    def desconto_10(self):
        desconto = self.preco * 0.10
        print(f"Produto: {self.nome}, Valor: R${self.preco:.2f}, Desconto 10%: R${desconto:.2f}")

class Carro:
    def __init__(self, fabricante, modelo, cor, valor, placa, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.placa = placa
        self.ano = ano

    def exibir_nome_modelo(self):
        print(f"Nome: {self.fabricante} - Modelo: {self.modelo}")

    def exibir_vendas(self):
        print(f"Modelo: {self.modelo} - Cor: {self.cor} - Placa: {self.placa}")

prod2 = Produto("SmartTV", "Philips", 4500)
print(prod2.nome)
prodx = Produto("Notebook", "Samsung", 3600)
print(prodx.nome, prodx.preco)
prodx.exibir_10vezes()
prodx.exibir_informacoes()
print("Valor parcelado em 3 vezes:", prodx.preco / 3)

# Ex. de uso da classe Carro
carro1 = Carro("Toyota", "Corolla", "Preto", 100000, "ABC-1234", 2022)
carro1.exibir_nome_modelo()
carro1.exibir_vendas()