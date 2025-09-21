import pickle
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Ouvre l'explorateur pour sélectionner un fichier
file_path = filedialog.askopenfilename(
    title="Choisissez un fichier .pkl",
    filetypes=[("Fichiers pickle", "*.pkl")]  # tu peux filtrer par type si besoin
)

# --- Essayer avec pickle ---
try:
    with open(file_path, "rb") as f:
        obj = pickle.load(f)
except Exception:
    # fallback avec pandas
    obj = pd.read_pickle(file_path)

# --- Détecter le type ---
if isinstance(obj, list):
    print(f"✅ Le .pkl est une list avec {len(obj)} éléments")
elif isinstance(obj, pd.DataFrame):
    print(f"✅ Le .pkl est un DataFrame avec {obj.shape[0]} lignes")
    print(obj.head())
else:
    print("❌ Format inattendu :", type(obj))
