#LÓG.002

class Carro:
    def __init__(self, fabricante, modelo, cor, valor, ano, placa):
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor  
        self.valor = valor 
        self.ano = ano  
        self.placa = placa

celta = Carro("gm", "Celta", "Azul", 12000, 2012, "BDNI1580")
print("Carro: ", celta.modelo, "; Ano: ", celta.ano)

carro1 = Carro("VW", "Nivs", "Prata", 85000, 2020, "ANCI538")
print("Placa:", carro1.placa)