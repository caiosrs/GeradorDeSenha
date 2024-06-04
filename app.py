import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''
    
    all_chars = lowercase + uppercase + numbers + special_chars
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_special_chars:
        password.append(random.choice(special_chars))
    
    while len(password) < length:
        password.append(random.choice(all_chars))
    
    random.shuffle(password)
    return ''.join(password)

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        include_uppercase = uppercase_var.get()
        include_numbers = numbers_var.get()
        include_special_chars = special_chars_var.get()
        
        if length < 4:
            messagebox.showwarning("Comprimento inválido", "O comprimento da senha deve ser pelo menos 4.")
            return
        
        password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o comprimento da senha.")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

tk.Label(root, text="Comprimento da Senha:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Incluir Letras Maiúsculas", variable=uppercase_var).grid(row=1, columnspan=2, padx=10, pady=5)

numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Incluir Números", variable=numbers_var).grid(row=2, columnspan=2, padx=10, pady=5)

special_chars_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Incluir Caracteres Especiais", variable=special_chars_var).grid(row=3, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Gerar Senha", command=generate_and_display_password).grid(row=4, columnspan=2, pady=10)

tk.Label(root, text="Senha Gerada:").grid(row=5, column=0, padx=10, pady=10)
password_entry = tk.Entry(root)
password_entry.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()
