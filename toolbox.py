import tkinter as tk
from tkinter import ttk
import webbrowser
import requests
from tqdm import tqdm
import os
import urllib.parse
import json

# ... (Önceki kodları burada tutun)

def load_button_data_from_internet():
    # Burada internetten veriyi çekerek button_data adlı bir liste döndürebilirsiniz
    # Örnek:
    button_data = [
        {"url": "https://www.example.com", "text": "Örnek Uygulama 1"},
        {"url": "FARKLI_URL", "text": "Uygulama Butonu 2"},
    ]
    return button_data

def create_buttons_from_data(tab_frame, button_data, button_action):
    buttons = []
    for data in button_data:
        button_text = data.get("text", "İsim Yok")
        button_url = data.get("url", "")
        button = tk.Button(tab_frame, text=button_text, font=("Helvetica", 12), bg="black", fg="white", command=lambda url=button_url: button_action(url))
        buttons.append(button)
    return buttons

root = tk.Tk()
root.title("Betabox")
root.geometry("600x400")  # Pencere boyutunu genişlettim
root.configure(bg="black")

title_label = tk.Label(root, text="Gökhan Özen Toolbox 0.5.6", font=("Helvetica", 24, "bold"), bg="black", fg="white")
title_label.pack(pady=20)  # Grid düzeninden pack düzenine geçtim

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=20, pady=20)  # Grid düzeninden pack düzenine geçtim

download_frame = ttk.Frame(notebook)
download_buttons = create_buttons_from_data(download_frame, load_button_data_from_internet(), button_clicked)
for i, button in enumerate(download_buttons):
    button.grid(row=i // 2, column=i % 2, padx=10, pady=10)

notebook.add(download_frame, text="Dosya İndirme")

link_frame = ttk.Frame(notebook)
link_buttons = create_buttons_from_data(link_frame, load_button_data_from_internet(), open_link)
for i, button in enumerate(link_buttons):
    button.grid(row=i // 2, column=i % 2, padx=10, pady=10)

notebook.add(link_frame, text="Linkler")

app_frame = ttk.Frame(notebook)
app_buttons = create_buttons_from_data(app_frame, load_button_data_from_internet(), open_link)
for i, button in enumerate(app_buttons):
    button.grid(row=i // 2, column=i % 2, padx=10, pady=10)

notebook.add(app_frame, text="Uygulamalar")

status_label = tk.Label(root, text="", font=("Helvetica", 14), bg="black", fg="white")
status_label.pack(pady=20)  # Grid düzeninden pack düzenine geçtim

root.mainloop()
