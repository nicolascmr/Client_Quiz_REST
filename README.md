# Client_Quiz_REST

## Instructions de lancement

Ce projet est composé d'un serveur API REST et d'une application fclient. Il faut lancer les deux parties séparément.

### 1. Lancement de l'API REST 

Ouvrez un terminal à la racine du projet :

1. **Créer l'environnement virtuel :**
   ```bash
   python -m venv venv
   ```

2. **Activer l'environnement virtuel :**
     ```bash
     source venv/bin/activate
     ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer le serveur Flask :**
   ```bash
   flask run
   ```
   L'API devrait être accessible à l'adresse `http://127.0.0.1:5000`.

### 2. Lancement du Client Vue.js

Ouvrez un **nouveau** terminal en laissant tourner le serveur Flask :

1. **Se déplacer dans le dossier du client Vue :**
   ```bash
   cd vue_quizz
   ```

2. **Installer les dépendances Node.js :**
   ```bash
   npm install
   ```

3. **Lancer le serveur de développement Vite :**
   ```bash
   npm run dev
   ```
   L'application sera accessible via l'URL indiquée dans le terminal.

4. **Le mot de passe pour accéder à la page admin est : "admin"**

## Structure du projet Vue

Nous avons structuré notre client avec plusieurs dossiers : 

- **components/** : Elle contient tous les composants enfants de la partie views/ comprenant les listes de quizz, les quizz en elle-même, les questions affichées lors d’un jeu et les questions modifiables en administrateur. 
- **routeur/** : contenant le fichier javascript pour les différentes routes. 
- **services/** : comprenant les fichiers js afin de faire les requêtes CRUD de notre serveur.
- **views/** : Comprenant les vues principales PlayView pour la partie jeu, et AdminView pour la partie administrateur.

**App.vue** est l’affichage principal qui redirige vers les views. 
