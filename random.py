import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4!")
            return
        
        characters = ""
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
        if digits_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation
        
        if not characters:
            messagebox.showerror("Error", "Select at least one character type!")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied!", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")

root = tk.Tk()
root.title("Password Generator - Andrew Agouridis")
root.geometry("400x300")

tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=uppercase_var, font=("Arial", 10)).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Lowercase (a-z)", variable=lowercase_var, font=("Arial", 10)).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Digits (0-9)", variable=digits_var, font=("Arial", 10)).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Symbols (!@#...)", variable=symbols_var, font=("Arial", 10)).pack(anchor='w', padx=50)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

tk.Label(root, text="Generated Password:", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 12), width=25)
password_entry.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 10), bg="#2196F3", fg="white")
copy_btn.pack(pady=5)

root.mainloop()