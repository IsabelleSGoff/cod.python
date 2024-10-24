#18102024
#Colégio Irene Branco - Téc. em Sistemas
#Professor: Orlando Gomes
#Autor: Isabelle S. Goffredo
#Versão 2.0

import tkinter as tk
from tkinter import messagebox

def calc_inss(salario):
    if salario <= 1100:
        inss = salario * 0.075
    elif salario <= 2000:
        inss = salario * 0.09
    elif salario <= 4000:
        inss = salario * 0.12
    else:
        inss = salario * 0.14
    return inss

def adicionar_funcionario():
    vnome = entry_nome.get()
    vqtde_hora = entry_qtde_hora.get()
    vvalor_hora = entry_valor_hora.get()

    if vnome and vqtde_hora.isdigit() and vvalor_hora.replace('.', '', 1).isdigit():
        funcionarios.append({
            'nome': vnome,
            'qtde_hora': int(vqtde_hora),
            'valor_hora': float(vvalor_hora)
        })
        
        entry_nome.delete(0, tk.END)
        entry_qtde_hora.delete(0, tk.END)
        entry_valor_hora.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente")

def calc_salario():
    vnome = entry_busca_nome.get()
    funcionario = procurar_funcionario(vnome)

    if funcionario:
        salario = funcionario['qtde_hora'] * funcionario['valor_hora']
        inss = calc_inss(salario)
        salario_liquido = salario - inss

        resultado = f"Funcionário: {funcionario['nome']}\n"
        resultado += f"Salário Bruto: R$ {salario:.2f}\n"
        resultado += f"INSS: R$ {inss:.2f}\n"
        resultado += f"Salário Líquido: R$ {salario_liquido:.2f}"
        messagebox.showinfo("Resultado", resultado)
        
        continuar = messagebox.askyesno("Confirmação", "Deseja continuar calculando? (Sim/Não)")
        if not continuar:
            root.quit()
    else:
        messagebox.showerror("Erro", "Funcionário não encontrado.")

def procurar_funcionario(vnome):
    for funcionario in funcionarios:
        if funcionario['nome'].lower() == vnome.lower():
            return funcionario
    return None

def mostrar_estatisticas():
    if funcionarios:
        salarios = [funcionario['qtde_hora'] * funcionario['valor_hora'] for funcionario in funcionarios]
        maior_salario = max(salarios)
        menor_salario = min(salarios)
        soma_salarios = sum(salarios)
        media_salarios = soma_salarios / len(salarios)

        estatisticas = f"Total de funcionários: {len(funcionarios)}\n"
        estatisticas += f"Maior Salário: R$ {maior_salario:.2f}\n"
        estatisticas += f"Menor Salário: R$ {menor_salario:.2f}\n"
        estatisticas += f"Soma dos Salários: R$ {soma_salarios:.2f}\n"
        estatisticas += f"Média dos Salários: R$ {media_salarios:.2f}"
        
        messagebox.showinfo("Estatísticas", estatisticas)
    else:
        messagebox.showinfo("Estatísticas", "Nenhum funcionário cadastrado.")

funcionarios = []

# Interface
root = tk.Tk()
root.title("Cadastro de Funcionários")


root.configure(bg="#f0f0f0")

fonte_padrao = ("Arial", 12)
fonte_titulo = ("Arial", 16, "bold")

padx = 10
pady = 5

titulo = tk.Label(root, text="Sistema de Cadastro de Funcionários", font=fonte_titulo, bg="#8a42f5", fg="white", padx=10, pady=10)
titulo.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

tk.Label(root, text="Nome do Funcionário:", font=fonte_padrao, bg="#f0f0f0").grid(row=1, column=0, padx=padx, pady=pady, sticky="e")
entry_nome = tk.Entry(root, font=fonte_padrao)
entry_nome.grid(row=1, column=1, padx=padx, pady=pady)

tk.Label(root, text="Quantidade de Horas:", font=fonte_padrao, bg="#f0f0f0").grid(row=2, column=0, padx=padx, pady=pady, sticky="e")
entry_qtde_hora = tk.Entry(root, font=fonte_padrao)
entry_qtde_hora.grid(row=2, column=1, padx=padx, pady=pady)

tk.Label(root, text="Valor da Hora:", font=fonte_padrao, bg="#f0f0f0").grid(row=3, column=0, padx=padx, pady=pady, sticky="e")
entry_valor_hora = tk.Entry(root, font=fonte_padrao)
entry_valor_hora.grid(row=3, column=1, padx=padx, pady=pady)

tk.Button(root, text="Adicionar Funcionário", font=fonte_padrao, bg="#8a42f5", fg="white", command=adicionar_funcionario).grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(root, text="Nome para Calcular Salário:", font=fonte_padrao, bg="#f0f0f0").grid(row=5, column=0, padx=padx, pady=pady, sticky="e")
entry_busca_nome = tk.Entry(root, font=fonte_padrao)
entry_busca_nome.grid(row=5, column=1, padx=padx, pady=pady)

tk.Button(root, text="Calcular Salário", font=fonte_padrao, bg="#8a42f5", fg="white", command=calc_salario).grid(row=6, column=0, columnspan=2, pady=10)

tk.Button(root, text="Mostrar Estatísticas", font=fonte_padrao, bg="#8a42f5", fg="white", command=mostrar_estatisticas).grid(row=7, column=0, columnspan=2, pady=20)

root.minsize(400, 400)

root.mainloop()
