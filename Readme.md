# Énoncé de Lab : Docker Compose avec Dépendance entre Conteneurs

Ce projet configure une application Flask avec un proxy inverse Nginx à l'aide de Docker Compose. Il est conçu pour un environnement de développement, mais peut être adapté pour une utilisation en production.

## Structure du Projet

Le projet est organisé en plusieurs services, chacun exécuté dans un conteneur Docker distinct. Voici la structure des fichiers et répertoires :

```
.
├── docker-compose.yml       # Fichier de configuration Docker Compose
├── app/                     # Répertoire contenant l'application Flask
│   ├── app.py               # Code source de l'application Flask
│   ├── requirements.txt     # Dépendances Python pour Flask
├── nginx/                   # Répertoire contenant la configuration Nginx
│   └── nginx.conf           # Fichier de configuration Nginx
├── Dockerfile               # Dockerfile unique pour construire l'image
└── README.md                # Documentation du projet

```

- **docker-compose.yml**  
  - Définit deux services : `flask` (application) et `nginx` (serveur web).  
  - `flask` est construit à partir d’un Dockerfile personnalisé.  
  - `nginx` utilise l’image officielle et charge un fichier de configuration spécifique.  
  - `depends_on` garantit que le service Flask démarre avant Nginx.

- **app.py**  
  - Application Flask simple affichant le message : *"Bonjour depuis Flask via Nginx !"*.

- **nginx.conf**  
  - Fichier de configuration Nginx qui redirige les requêtes HTTP vers le service Flask.

- **Dockerfile**  
  - Basé sur l’image Python 3.11.  
    - Installe Flask et ses dépendances à partir de `requirements.txt`.  
    - Lance l’application Flask définie dans `app.py`.

## Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Services

1. **Flask** : Framework web Python.
    - URL : `http://localhost:5000`
    - Conteneur : `flask_app`

2. **Nginx** : Proxy inverse pour l'application Flask.
    - URL : `http://localhost:80`
    - Conteneur : `nginx_proxy`

## Instructions

### 1. Cloner le Dépôt

Clonez le dépôt Git et accédez au répertoire du projet :

```bash
git clone https://github.com/fayeboua/tp-a57-lab2.git
cd tp-a57-lab2
```

### 2. Construire et Lancer les Services

Utilisez Docker Compose pour construire et démarrer les conteneurs :

```bash
docker-compose up --build
```

### 3. Accéder aux Services

- **Flask** : [http://localhost:5000](http://localhost:5000)
- **Nginx** : [http://localhost:80](http://localhost:80)
- **Portainer** (si activé) : [http://localhost:9000](http://localhost:9000)

### 4. Arrêter les Services

Pour arrêter et supprimer les conteneurs, exécutez :

```bash
docker-compose down
```

## Notes

- Assurez-vous que les ports requis (5000, 80, 9000) ne sont pas utilisés par d'autres applications.
- Pour une utilisation en production, envisagez de sécuriser Nginx avec HTTPS et de configurer des variables d'environnement pour Flask.

---

**Folly Tata Ayeboua**
