#LÓG.003

import tkinter as tk
from tkinter import messagebox

def calcular_media(notas):
    media = sum(notas) / len(notas)
    
    if media < 3:
        return media, "Retido"
    elif media < 6:
        return media, "Recuperação"
    else:
        return media, "Aprovado"

def calcular():
    try:
        notas = [
            float(entry_nota1.get()),
            float(entry_nota2.get()),
            float(entry_nota3.get()),
            float(entry_nota4.get())
        ]
        
        media, status = calcular_media(notas)
        
        resultado = f"Aluno: {entry_nome.get()} - Média: {media:.2f} - Status: {status}"
        messagebox.showinfo("Resultado", resultado)
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para as notas.")

# criação da janela principal
root = tk.Tk()
root.title("Cálculo de Média Escolar")

tk.Label(root, text="Nome do Aluno:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nota 1:").grid(row=1, column=0, padx=10, pady=5)
entry_nota1 = tk.Entry(root)
entry_nota1.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Nota 2:").grid(row=2, column=0, padx=10, pady=5)
entry_nota2 = tk.Entry(root)
entry_nota2.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Nota 3:").grid(row=3, column=0, padx=10, pady=5)
entry_nota3 = tk.Entry(root)
entry_nota3.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Nota 4:").grid(row=4, column=0, padx=10, pady=5)
entry_nota4 = tk.Entry(root)
entry_nota4.grid(row=4, column=1, padx=10, pady=5)

btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
