import os
import pickle
from deepface import DeepFace
from tqdm import tqdm  # pour la barre de progression

# --- CONFIG ---
dataset_path = "/content/drive/MyDrive/Dataset"
model_name = "ArcFace"
detector_backend = "retinaface"
output_pkl = "/content/embeddings_list.pkl"

# --- 1. Liste de toutes les images ---
images = []
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            images.append(os.path.join(root, file))

# --- 2. Calcul des embeddings avec barre de progression ---
embeddings_list = []

print(f"🚀 Calcul des embeddings pour {len(images)} images...")
for img_path in tqdm(images):
    try:
        emb = DeepFace.represent(
            img_path=img_path,
            model_name=model_name,
            detector_backend=detector_backend,
            enforce_detection=False
        )
        if isinstance(emb, list):
            embeddings_list.extend([{"identity": img_path, "embedding": e["embedding"]} for e in emb])
        else:
            embeddings_list.append({"identity": img_path, "embedding": emb["embedding"]})
    except Exception as e:
        print(f"⚠️ Erreur sur {img_path}: {e}")

# --- 3. Sauvegarde ---
with open(output_pkl, "wb") as f:
    pickle.dump(embeddings_list, f)

print(f"✅ Embeddings sauvegardés dans : {output_pkl}")
print(f"Nombre total d'embeddings : {len(embeddings_list)}")
