import pandas as pd
import numpy as np
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from deepface import DeepFace
import tkinter as tk
from tkinter import filedialog

# Chemin de la photo à tester"
photo_test = filedialog.askopenfilename(
    title="Photo à tester",
    filetypes=[("Images", "*.jpg *.jpeg *.png *.gif")]
)

# Chemin du fichier pickle des embeddings"
pkl_path = filedialog.askopenfilename(
    title="Choisissez un fichier .pkl de comparaison",
    filetypes=[("Fichiers pickle", "*.pkl")]  # tu peux filtrer par type si besoin
)  

# --- 1. Charger les embeddings de la base ---
print("📂 Chargement de la base d'embeddings...")
embeddings_list = pd.read_pickle(pkl_path)

print(f"✅ Base chargée avec {len(embeddings_list)} visages.")

# --- 2. Embedding de la photo test ---
print("🔍 Calcul de l'embedding de la photo test...")
embedding_test = DeepFace.represent(
    img_path=photo_test,
    model_name="ArcFace",
    detector_backend="retinaface",
    enforce_detection=False
)

# Si plusieurs visages détectés, on prend le premier
if isinstance(embedding_test, list):
    embedding_test = embedding_test[0]["embedding"]
else:
    embedding_test = embedding_test["embedding"]

embedding_test = np.array(embedding_test)

# --- 3. Fonction de comparaison (cosinus) ---
def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# --- 4. Comparer avec toute la base ---
print("⚖️ Comparaison avec la base...")
results = []
for item in embeddings_list:
    sim = cosine_similarity(embedding_test, item["embedding"])
    results.append((item["identity"], sim))

# --- 5. Trier et afficher les meilleurs ---
results.sort(key=lambda x: x[1], reverse=True)

print("\n🏆 Top 5 des correspondances :")
for i, (identity, sim) in enumerate(results[:5], start=1):
    name = os.path.basename(os.path.dirname(identity))  # récupère le nom du dossier célébrité
    print(f"{i}. {name} ({sim:.4f})")
