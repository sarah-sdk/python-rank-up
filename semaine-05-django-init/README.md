# 🐍 Semaine 05 - Django (Bases)
📅 **Période** : du 11 au 17 août 2025
🎯 **Objectif** : Créer un blog basique avec Django, incluant modèles, vues, adiminstration et templates.

---
## 🔍 Objectifs pédagogiques
- Découvrir et installer Django
- Comprendre la structure d'un projet Django
- Créer et manipuler des modèles dans la base de données
- Configurer et utiliser l'interface administration
- Afficher des données avec des vues et des templates

---
## 📚 Notions abordées
- Commande de base de Django (`startproject`, `startapp`, `migrate`, etc.)
- Organisation des fichiers (`manage.py`, settings, apps)
- Création de modèles et migrations
- Admin Django : configuration et personnalisation
- Vues, URLS et templates
- Utilisation du shell Django pour tester les modèles

---
## ✅ Plan de travail
### 1. Installation et projet de base
- Installer Django
- Créer un projet `blog` et configurer `settings.py`
- Lancer le serveur et vérifier le fonctionnement

### 2. Création de l'app posts et modèle Post
- Définir le modèle `Post` avec titre, contenu, dates
- Faire les migrations et tester dans le shell

### 3. Interface administation
- Configurer l'admin
- Créer un superuser et ajouter des articles depuis l'admin

### 4. Vues et templates
- Lister les posts
- Page de détail pour un post
- Template de base avec héritage (`base.html`)

### 5. Améliorations et finalisation
- Navigation entre pages
- Mise en forme avec CSS ou Bootstrap
- README clair avec instructions et captures d'écran

---
## 💡 Tips de la semaine
- Utilisation `python manage.py shell_plus` (si `django-extensions`installé) pour tester plus vite
- Penser à séparer les templates par app (`posts/templates/posts/...`)
- Utilisation `{% url %}` dans les templates pour éviter les liens en dur
- Bonus : déploiement sur un service gratuit comme **PythonAnywhere** ou **Railway**

