# 📝 API Tasks - Mini-projet DRF
Une petite API de gestion de tâches réalisée avec **Django** et **Django REST Framework** dans le cadre de ma progression Python.

## 🚀 Installation
### 1. Cloner le project
```bash
git clone <url-du-repo>
cd <nom-du-projet>
```

### 2. Créer un environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate.      # Windows
```

### 3. Installer les dépendances
```bash
cd ../
pip install -r requirements.txt
```

### 4. Appliquer les migrations
```bash
cd <nom-du-projet>
python manage.py migrate
```

### 5. Créer un superutilisateur (pour accéder à l'admin)
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

## 🔑 Authentification
- L'API utilise le système d'authentification de Django.
- Seuls les utilisateurs connectés peuvent accéder aux endpoints.
- Chaque utilisateur ne voit que ses propres tâches.

## 📌 Endpoints principaux
### 📍 Liste et création de tâches
- `GET` `/api/tasks/` → liste de toutes les tâches de l'utilisateur connecté
- `POST` `/api/tasks/` → créer une nouvelle tâche

### 📍 Détail d'une tâche
- `GET` `/api/tasks/{id}/` → voir une tâche précise
- `PUT` `/api/tasks/{id}/` → modifier entièrement une tâche
- `PATCH` `/api/tasks/{id}/` → modifier artiellement une tâche
- `DELETE` `/api/tasks/{id}/` → supprimer une tâche

### 📍 Filtres et tri
- `GET` `/api/tasks/?done=true` → filtre sur les tâches terminées
- `GET` `/api/tasks/?ordering=created_at` → tri par date de création

## 🛠️ Technologies utilisées
- Python 3.13
- Django 5
- Django REST Framework

