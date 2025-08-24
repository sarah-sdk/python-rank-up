# 🔗 Semaine 06 – API REST avec Django REST Framework

📅 **Période :** du 18 au 24 août 2025  
🎯 **Objectif :** Construire une API REST avec Django + DRF.

---

## 🔍 Objectifs pédagogiques

- Créer des endpoints REST (GET, POST, PUT, DELETE)
- Utiliser des serializers pour structurer les données
- Comprendre les vues `APIView` et `ViewSet`
- Protéger l’API avec de l’authentification (Token / Session)

---

## 📚 Notions abordées

- `drf`, `serializers`, `views`, `routers`
- `GET`, `POST`, `PUT`, `DELETE` via Postman
- Permissions : `AllowAny`, `IsAuthenticated`
- Authentification basique / token (ou session)

---

## ✅ Plan de travail

### 1. Exercices (dans `/exercices/`)
- [X] Création d’un modèle exposé via API
- [X] Endpoints `GET`, `POST`
- [X] Authentification simple

### 2. Mini-projet : API de tâches
> Une API pour gérer des tâches via front ou Postman.

Fonctionnalités :
- Créer, lire, modifier, supprimer une tâche
- Lister uniquement ses propres tâches
- Authentification pour limiter l’accès

---

## 💡 Tips de la semaine

- Installe DRF : `pip install djangorestframework`
- Utilise `ModelSerializer` pour aller plus vite
- Lis bien les logs en cas d’erreur 403 ou 500 😉

---
