import folium
import json
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import csv
import xml.etree.ElementTree as ET

# Arquivos
JSON_FILE = "locais.json"
TXT_FILE = "locais.txt"
MAP_FILE = "mapa.html"

# Capitais do mundo (exemplo simplificado)
capitais_mundo = [
    ("Brasília", -15.793889, -47.882778),
    ("Washington, D.C.", 38.89511, -77.03637),
    ("Paris", 48.8566, 2.3522),
    ("Londres", 51.5074, -0.1278),
    ("Tóquio", 35.6895, 139.6917),
    ("Pequim", 39.9042, 116.4074),
    ("Berlim", 52.52, 13.405),
    ("Moscou", 55.7558, 37.6173),
    ("Canberra", -35.2809, 149.13),
    ("Buenos Aires", -34.6037, -58.3816),
    ("Pretória", -25.7479, 28.2293),
    ("Nova Délhi", 28.6139, 77.209),
    ("Cidade do México", 19.4326, -99.1332),
    ("Ottawa", 45.4215, -75.699),
    ("Roma", 41.9028, 12.4964),
]

# Mapa inicial
mapa = folium.Map(location=[0, 0], zoom_start=2)

# Adiciona capitais
for nome, lat, lon in capitais_mundo:
    folium.Marker(location=[lat, lon], popup=nome, icon=folium.Icon(color='blue')).add_to(mapa)

# Funções de dados
def carregar_locais():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    return []

def salvar_local(nome, lat, lon):
    dados = carregar_locais()
    dados.append({'nome': nome, 'latitude': lat, 'longitude': lon})

    with open(JSON_FILE, 'w') as f_json, open(TXT_FILE, 'a') as f_txt:
        json.dump(dados, f_json, indent=4)
        f_txt.write(f"{nome} - Latitude: {lat}, Longitude: {lon}\n")

def salvar_todos_csv_xml():
    # Junta capitais e locais adicionados
    todos = [{'nome': nome, 'latitude': lat, 'longitude': lon} for nome, lat, lon in capitais_mundo]
    todos += carregar_locais()

    # Salva em CSV
    with open('locais.csv', 'w', newline='', encoding='utf-8') as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=['nome', 'latitude', 'longitude'])
        writer.writeheader()
        writer.writerows(todos)

    # Salva em XML
    root = ET.Element('locais')
    for local in todos:
        loc_elem = ET.SubElement(root, 'local')
        ET.SubElement(loc_elem, 'nome').text = str(local['nome'])
        ET.SubElement(loc_elem, 'latitude').text = str(local['latitude'])
        ET.SubElement(loc_elem, 'longitude').text = str(local['longitude'])
    tree = ET.ElementTree(root)
    tree.write('locais.xml', encoding='utf-8', xml_declaration=True)

def adicionar_no_mapa(nome, lat, lon, abrir_navegador=True):
    folium.Marker([lat, lon], popup=nome, icon=folium.Icon(color='red')).add_to(mapa)
    mapa.save(MAP_FILE)
    if abrir_navegador:
        webbrowser.open(MAP_FILE)

def inicializar_json_com_capitais():
    if not os.path.exists(JSON_FILE) or os.stat(JSON_FILE).st_size == 0:
        dados = [{'nome': nome, 'latitude': lat, 'longitude': lon} for nome, lat, lon in capitais_mundo]
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4)

# Interface Tkinter
def adicionar_local():
    try:
        nome = entrada_nome.get()
        lat = float(entrada_lat.get())
        lon = float(entrada_lon.get())

        if nome:
            salvar_local(nome, lat, lon)
            adicionar_no_mapa(nome, lat, lon)
            salvar_todos_csv_xml()  # Salva CSV e XML sempre que adicionar
            messagebox.showinfo("Sucesso", f"Local '{nome}' adicionado!")
        else:
            messagebox.showwarning("Erro", "O nome do local não pode estar vazio.")
    except ValueError:
        messagebox.showerror("Erro", "Latitude e Longitude devem ser números válidos.")

# GUI
janela = tk.Tk()
janela.title("Adicionar Local no Mapa")

# Define tamanho e cor de fundo da janela
janela.geometry("400x200")
janela.configure(bg="#6a0dad")  # Roxo

# Labels e entradas com fundo roxo e texto verde
label_fg = "#00ff00"  # Verde
entry_bg = "#e0e0e0"

tk.Label(janela, text="Nome do Local:", bg="#6a0dad", fg=label_fg).grid(row=0, column=0, padx=10, pady=10)
entrada_nome = tk.Entry(janela, bg=entry_bg)
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Latitude:", bg="#6a0dad", fg=label_fg).grid(row=1, column=0, padx=10, pady=10)
entrada_lat = tk.Entry(janela, bg=entry_bg)
entrada_lat.grid(row=1, column=1, padx=10, pady=10)

tk.Label(janela, text="Longitude:", bg="#6a0dad", fg=label_fg).grid(row=2, column=0, padx=10, pady=10)
entrada_lon = tk.Entry(janela, bg=entry_bg)
entrada_lon.grid(row=2, column=1, padx=10, pady=10)

botao = tk.Button(janela, text="Adicionar ao Mapa", command=adicionar_local, bg="#00ff00", fg="#6a0dad")
botao.grid(row=3, column=0, columnspan=2, pady=10)

# Antes de qualquer operação, inicialize o JSON com as capitais
inicializar_json_com_capitais()

# Carregar locais salvos
for local in carregar_locais():
    # Só adiciona marcador vermelho se não for uma capital
    if (local['nome'], local['latitude'], local['longitude']) not in capitais_mundo:
        adicionar_no_mapa(local['nome'], local['latitude'], local['longitude'], abrir_navegador=False)

salvar_todos_csv_xml()  # Garante que CSV e XML estejam atualizados ao iniciar

mapa.save(MAP_FILE)
webbrowser.open(MAP_FILE)  # Abre o mapa automaticamente ao iniciar

janela.mainloop()
