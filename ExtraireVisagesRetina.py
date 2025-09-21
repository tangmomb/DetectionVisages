import cv2
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from retinaface import RetinaFace
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Créer le dossier pour sauvegarder les visages
os.makedirs("faces", exist_ok=True)

# Demander à l'utilisateur le chemin de l'image
image_path = filedialog.askopenfilename(
    title="Photo à analyser",
    filetypes=[("Images", "*.jpg *.jpeg *.png *.gif")]
)

# Charger l'image
img = cv2.imread(image_path)
if img is None:
    print("Erreur : impossible de charger l'image. Vérifiez le chemin.")
    exit()

# Détection des visages avec RetinaFace
faces = RetinaFace.detect_faces(image_path)

if isinstance(faces, dict):
    for i, (key, face_data) in enumerate(faces.items(), start=1):
        x1, y1, x2, y2 = face_data["facial_area"]

        # Recadrer le visage
        face = img[y1:y2, x1:x2]

        # Redimensionner en 224x224 (utile pour IA type FaceNet/VGG)
        face_resized = cv2.resize(face, (224, 224))
        face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)

        # Sauvegarder
        Image.fromarray(face_rgb).save(f"faces/face_{i}.jpg")

    print(f"{len(faces)} visage(s) détecté(s) et sauvegardé(s) dans 'faces/'")
else:
    print("Aucun visage détecté.")
