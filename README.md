# 😀 Detection Visages

Ce projet permet d'effectuer différentes opérations sur des images de visages à l'aide de l'intelligence artificielle et de la reconnaissance faciale. Il propose un menu graphique pour lancer facilement chaque script.

## Installation

1. **Créer un environnement Python**

   Ouvrez un terminal dans le dossier du projet et tapez :

   ```
   python -m venv venv
   ```

   Cela créera un environnement virtuel nommé `venv`.

2. **Activer l'environnement**

   Sous Windows :

   ```
   venv\Scripts\activate
   ```

3. **Installer les dépendances**

   Installez les modules nécessaires :

   ```
   pip install -r requirements.txt
   ```

## Utilisation

1. **Lancer le menu**

   Double-cliquez sur le fichier `Launcher.bat`.

   Ce fichier va activer l'environnement et ouvrir le menu graphique (Tkinter).

2. **Choisir une opération**

   Le menu propose les scripts suivants :

   - **Comparer un visage** : Compare une photo à une base d'embeddings pour trouver les correspondances. Exemple de dataset pour tester https://www.kaggle.com/datasets/vishesh1412/celebrity-face-image-dataset. Le fichier Pickle (.pkl) de ce dataset est disponible sur ce repository (All.pk).
   - **Extraire visages (Retina)** : Détecte et extrait les visages d'une image.
   - **Calculer embeddings (Colab)** : Calcule les embeddings pour toutes les images d'un dossier (usage typique sur Google Colab).
   - **Détecter GPU** : Vérifie si un GPU est disponible pour l'accélération.
   - **Type de fichier PKL** : Affiche le type et le contenu d'un fichier pickle (embeddings ou DataFrame).
   - **Quelle photo a plusieurs embeddings** : Liste les images qui ont plusieurs embeddings dans la base.

## Notes

- Les scripts utilisent des modules comme DeepFace, RetinaFace, OpenCV, etc.
- Les fichiers `.pkl` contiennent les embeddings des visages pour la comparaison.
- Le menu graphique facilite l'utilisation sans avoir à lancer chaque script manuellement.
