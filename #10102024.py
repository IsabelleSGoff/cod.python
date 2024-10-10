#LÓG.004
#Colégio Irene Branco - Téc. em Sistemas
#Professor: Orlando Gomes
#Autor: Isabelle S. Goffredo
#Data - 10/10/2024
        
import tkinter as tk 
from tkinter import messagebox

def calc_inss(salario):
    if salario <= 1412:
        inss = salario * 0.075
    elif salario <= 2666:
        inss = salario * 0.09
    elif salario <= 4000:
        inss = salario * 0.12
    else:
        inss = salario * 0.14
    return inss

def procurar_funcionario(nome):
    for funcionario in funcionarios:
        if funcionario['nome'].lower() == nome.lower():
            return funcionario
    return None

def adicionar_funcionario():
    nome = entry_nome.get()
    carga_horaria = entry_carga_horaria.get()
    valor_hora = entry_valor_hora.get() 
    
    if nome and carga_horaria.isdigit() and valor_hora.replace('.', '', 1).isdigit():
        funcionarios.append({
            'nome':nome,
            'carga_horaria': float(carga_horaria),
            'valor_hora': float(valor_hora)
        })
        entry_nome.delete(0,tk.END)
        entry_carga_horaria.delete(0,tk.END)
        entry_valor_hora.delete(0,tk.END)
        messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")
    else:
        messagebox.showinfo("Erro", "Preencha todos os campos corretamente")
        
def calc_salario():
    nome_busca = entry_busca_nome.get()  # FIQUEI 30 MINUTOS AQUIIIIIIIIIII
    funcionario = procurar_funcionario(nome_busca)
    
    if funcionario:
        salario = funcionario['carga_horaria'] * funcionario['valor_hora']
        inss = calc_inss(salario)
        
        resultado = f"Funcionário: {funcionario['nome']}\n"
        resultado += f"Salário Bruto: R$ {salario:.2f}\n"
        resultado += f"INSS: R$ {inss:.2f}\n"
        resultado += f"Salário Líquido: R$ {salario - inss:.2f}"
        
        messagebox.showinfo("Resultado", resultado)
    else:
        messagebox.showerror("Erro", "Funcionário não encontrado.")

funcionarios = []

root = tk.Tk()
root.title("Cadastro de Funcionários")

tk.Label(root, text="Nome do Funcionário:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Carga Horária:").grid(row=1, column=0)
entry_carga_horaria = tk.Entry(root)
entry_carga_horaria.grid(row=1, column=1)

tk.Label(root, text="Valor da Hora:").grid(row=2, column=0)
entry_valor_hora = tk.Entry(root)
entry_valor_hora.grid(row=2, column=1)

tk.Button(root, text="Adicionar Funcionário", command=adicionar_funcionario).grid(row=3, columnspan=2)

tk.Label(root, text="Nome para Calcular Salário:").grid(row=4, column=0)
entry_busca_nome = tk.Entry(root)
entry_busca_nome.grid(row=4, column=1)

tk.Button(root, text="Calcular Salário", command=calc_salario).grid(row=5, columnspan=2)

def mostrar_total():
    messagebox.showinfo("Total de Funcionários", f"Total de funcionários cadastrados: {len(funcionarios)}")

tk.Button(root, text="Mostrar Total de Funcionários", command=mostrar_total).grid(row=6, columnspan=2)

root.mainloop()