from collections import Counter
import pickle
import tkinter as tk
from tkinter import filedialog

# Ouvre l'explorateur pour sélectionner un fichier
file_path = filedialog.askopenfilename(
    title="Choisissez un fichier .pkl",
    filetypes=[("Fichiers pickle", "*.pkl")]  # tu peux filtrer par type si besoin
)

with open(file_path, "rb") as f:
    embeddings_list = pickle.load(f)

images = [e["identity"] for e in embeddings_list]
counts = Counter(images)

# Affiche les images avec plus d’un embedding
for img, c in counts.items():
    if c > 1:
        print(f"{img} → {c} embeddings")
