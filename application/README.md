📱 Cloud Native Calculator Application
Bienvenue dans l'application Cloud Native Calculator, un projet conçu pour démontrer l'architecture des applications cloud-native en utilisant des conteneurs Docker. Ce projet est divisé en trois parties principales : Frontend, Backend, et Consumer, interconnectées via des services tels que RabbitMQ et Redis.

🚀 Architecture de l'Application
L'application est structurée en plusieurs microservices :

🌐 Frontend (Interface Utilisateur)
Développé en HTML, CSS, et JavaScript.
Interface moderne et responsive pour effectuer des calculs.
Communique avec l'API Backend via des requêtes HTTP.
⚙️ Backend (API REST)
Développé en Python (Flask).
Gère la logique métier des opérations mathématiques.
Envoie des tâches de calcul au service RabbitMQ et récupère les résultats depuis Redis.

🗂️ Consumer (Worker)
Également développé en Python.
Consomme les messages de la file RabbitMQ, effectue les calculs, et stocke les résultats dans Redis.

📡 Services de Message et Cache
RabbitMQ : Sert de broker de messages pour la gestion des tâches de calcul.
Redis : Utilisé pour le stockage temporaire des résultats de calcul.

⚙️ Technologies Utilisées
Frontend : HTML, CSS, JavaScript, NGINX
Backend : Python, Flask, REST API
Consumer : Python, RabbitMQ, Redis
Conteneurisation : Docker
Orchestration (optionnel) : Docker Compose / Kubernetes



🐳 Instructions pour le Déploiement avec Docker

1️⃣ Construire les images Docker :
Pour le frontend :
docker build -t frontend-app ./frontend

Pour le backend :
docker build -t backend-app ./backend

Pour le consumer :
docker build -t consumer-app ./consumer

2️⃣ Lancer les conteneurs :
Créer un réseau Docker pour les conteneurs :
docker network create calc-network

Lancer les services nécessaires :
docker run -d --network=calc-network --name redis-service redis
docker run -d --network=calc-network --name rabbitmq-service -p 15672:15672 -p 5672:5672 rabbitmq:3-management

Lancer les microservices :
docker run -d --network=calc-network --name backend-app -p 5000:5000 backend-app
docker run -d --network=calc-network --name consumer-app consumer-app
docker run -d --network=calc-network --name frontend-app -p 8080:80 frontend-app

3️⃣ Accéder à l'Application :
Frontend (Calculatrice) : http://localhost:8080
API Backend : http://localhost:5000/api
Interface RabbitMQ : http://localhost:15672 (Login : guest / guest)

📊 Fonctionnalités Clés

✅ Calculs de base : Addition, Soustraction, Multiplication, Division.

🔗 Communication asynchrone via RabbitMQ.

⚡ Stockage rapide des résultats avec Redis.

🌗 Changement de thème (mode clair/sombre).

📝 Auteur
Projet développé par Ahmed et Oussama .
