# 📌 Mini-Projet : BucketList (Semaine-07)

Ce mini-projet fait partie de mon parcours d'entraînement sur **Python + Django + React**.
L'objectif de la semaine était de mettre en place une petite application permettant de gérer une _bucketlist_ : liste de choses à réaliser.

## 🚀 Fonctionnalités
- Affichage de la liste des items
- Ajout d'un nouvel item (nom, catégorie, statut réalisé ou non)
- Modification d'un item existant
- Suppression d'un item
- Interface simple avec des modales (`<dialog>`) pour l'édition, l'ajout et la suppression

## 🛠️ Stack technique
- **Backend** : Django + Django REST Framework
- **Frontend** : React (Vite) + TypeScript
- **Auth** : Token d'authentification (DRF)
- **Base de données** : SQLite (par défaut Django)

## 📁 Organisation
Le projet est inclus dans le repo global de mes semaines d'entraînement.
Les dossiers importants pour ce mini-projet :

```bash
/backend      → API Django REST Framework
/frontend     → Application React (bucketlist)
```

## ▶️ Installation et lancement
### Backend (Django et DRF)
- Se placer dans le dossier `backend`
- Créer et activer un environnement virtuel
- Installer les dépendances :
```bash
pip install -r requirements.txt
```

- Lancer les migrations :
```bash
python manage.py migrate
```

- Créer un super utilisateur si besoin :
```bash
python manage.py createsuperuser
```

- Démarrer le serveur :
```bash
python manage.py runserver
```

L’API est disponible sur : `http://127.0.0.1:8000/api/` ou `http://127.0.0.1:8000/admin/``
---
### Frontend (React + Vite)
- Se placer dans le dossier `frontend`
- Installer les dépendances :
```bash
npm install
```

- Lancer le serveur de développement :
```bash
npm run dev
```

L’application est disponible sur : `http://localhost:5173/`

---
## 🎯 Objectif pédagogique
- Découvrir **Django REST Framework** et la mise en place d'une API REST.
- Gérer le CRUD complet (Create, Read, Update, Delete).
- Connecter un **frontend React** à un **backend Django**.

