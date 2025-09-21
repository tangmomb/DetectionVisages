import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# List of scripts to launch
SCRIPTS = [
    ("Comparer un visage", "ComparerVisage.py"),
    ("Extraire visages (Retina)", "ExtraireVisagesRetina.py"),
    ("Calculer embeddings (Colab)", "GoogleColabCalculPkl.py"),
    ("Détecter GPU", "GPUDetect.py"),
    ("Type de fichier PKL", "PklType.py"),
    ("Quelle photo a plusieurs embeddings", "QuellePhotoAPlusieursEmbeddings.py"),
]

WORKDIR = os.path.dirname(os.path.abspath(__file__))

# Function to launch a script
def launch_script(script):
    script_path = os.path.join(WORKDIR, script)
    if not os.path.exists(script_path):
        messagebox.showerror("Erreur", f"Le script {script} n'existe pas.")
        return
    try:
        subprocess.Popen([sys.executable, script_path])
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de lancer {script}: {e}")

# Tkinter UI
root = tk.Tk()
root.title("Launcher - Detection Visages")
root.geometry("400x350")

label = tk.Label(root, text="Choisissez un script à lancer:", font=("Arial", 14))
label.pack(pady=15)

for name, script in SCRIPTS:
    btn = tk.Button(root, text=name, font=("Arial", 12), width=30,
                    command=lambda s=script: launch_script(s))
    btn.pack(pady=5)

root.mainloop()
