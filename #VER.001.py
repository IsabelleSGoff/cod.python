#VER.002

import tkinter as tk
from tkinter import ttk

def processar():
    nome = entry_nome.get()
    bairro = entry_bairro.get()
    email = entry_email.get()
    idade = entry_idade.get()
    
    label_resultado.config(text=f"Dados processados. Até mais: {nome}, {idade} anos.")

# Criar Janela
janela = tk.Tk()
janela.title("Captura Dados")

# Criar entry e label para o nome
label_nome = ttk.Label(janela, text="Nome: ")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nome = ttk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

# Criar entry e label para o bairro
label_bairro = ttk.Label(janela, text="Bairro: ")
label_bairro.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_bairro = ttk.Entry(janela)
entry_bairro.grid(row=1, column=1, padx=10, pady=5)

# Criar entry e label para o email
label_email = ttk.Label(janela, text="Email: ")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_email = ttk.Entry(janela)
entry_email.grid(row=2, column=1, padx=10, pady=5)

# Criar entry e label para a idade
label_idade = ttk.Label(janela, text="Idade: ")
label_idade.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_idade = ttk.Entry(janela)
entry_idade.grid(row=3, column=1, padx=10, pady=5)

# Label para resultado
label_resultado = ttk.Label(janela, text="")
label_resultado.grid(row=4, columnspan=2, padx=10, pady=5)

# Botão para processar o cálculo
botao_calcular = ttk.Button(janela, text="Processar", command=processar)
botao_calcular.grid(row=5, columnspan=2, padx=10, pady=10)

# Iniciar loop
janela.mainloop()