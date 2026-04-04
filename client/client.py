import tkinter as tk
from tkinter import ttk
import requests
import random
import uuid
from datetime import datetime

SERVIDOR_URL = "http://servidor_api:5000/sensor"

historico = []

def enviar_temperatura():

    temperatura = round(random.uniform(-10, 40), 2)

    dados = {
        "uuid": str(uuid.uuid4()),
        "sensor_id": "sensor_01",
        "temperatura": temperatura
    }

    try:
        resposta = requests.post(SERVIDOR_URL, json=dados)
        status = resposta.json().get("status")

        atualizar_status(status)
        atualizar_temperatura(temperatura)
        adicionar_historico(temperatura, status)

    except:
        rotulo_status.config(text="ERRO DE CONEXÃO", fg="red")


def atualizar_temperatura(temp):
    rotulo_temp.config(text=f"{temp} °C")


def atualizar_status(status):

    cores = {
        "Normal": "#2ecc71",
        "Alerta": "#f1c40f",
        "Crítico": "#e74c3c"
    }

    cor = cores.get(status, "white")

    rotulo_status.config(
        text=status,
        fg=cor
    )


def adicionar_historico(temp, status):

    leitura = f"{datetime.now().strftime('%H:%M:%S')} | {temp}°C | {status}"

    historico.append(leitura)

    historico_list.delete(0, tk.END)

    for item in historico[-10:]:
        historico_list.insert(tk.END, item)


# ==============================
# JANELA PRINCIPAL
# ==============================

root = tk.Tk()
root.title("Monitoramento de Temperatura")
root.geometry("500x500")
root.configure(bg="#1e1e1e")


titulo = tk.Label(
    root,
    text="Sensor de Temperatura",
    font=("Segoe UI", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

titulo.pack(pady=15)


# ==============================
# CARD TEMPERATURA
# ==============================

temp_frame = tk.Frame(root, bg="#2c2c2c", padx=20, pady=20)
temp_frame.pack(pady=10)

tk.Label(
    temp_frame,
    text="Temperatura Atual",
    font=("Segoe UI", 12),
    bg="#2c2c2c",
    fg="#bbbbbb"
).pack()

rotulo_temp = tk.Label(
    temp_frame,
    text="-- °C",
    font=("Segoe UI", 28, "bold"),
    bg="#2c2c2c",
    fg="white"
)

rotulo_temp.pack()


# ==============================
# STATUS
# ==============================

status_frame = tk.Frame(root, bg="#2c2c2c", padx=20, pady=15)
status_frame.pack(pady=10)

tk.Label(
    status_frame,
    text="Status do Sistema",
    font=("Segoe UI", 12),
    bg="#2c2c2c",
    fg="#bbbbbb"
).pack()

rotulo_status = tk.Label(
    status_frame,
    text="---",
    font=("Segoe UI", 18, "bold"),
    bg="#2c2c2c",
    fg="white"
)

rotulo_status.pack()


# ==============================
# BOTÃO ENVIAR
# ==============================

enviar_btn = tk.Button(
    root,
    text="Enviar Temperatura",
    command=enviar_temperatura,
    font=("Segoe UI", 12, "bold"),
    bg="#3498db",
    fg="white",
    padx=20,
    pady=10,
    relief="flat",
    cursor="hand2"
)

enviar_btn.pack(pady=20)


# ==============================
# HISTÓRICO
# ==============================

tk.Label(
    root,
    text="Histórico de Leituras",
    font=("Segoe UI", 12),
    bg="#1e1e1e",
    fg="white"
).pack()


historico_list = tk.Listbox(
    root,
    width=45,
    height=10,
    bg="#2c2c2c",
    fg="white",
    font=("Consolas", 10),
    borderwidth=0
)

historico_list.pack(pady=10)

root.mainloop()