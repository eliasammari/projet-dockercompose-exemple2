# Utiliser une image de base officielle avec Python 3.9
FROM python:slim-bullseye

#Meta-données
LABEL version="1.0" 
LABEL maintainer="Sabeur Elkosantini"


#Mise à jour pip
RUN python3 -m pip install --no-cache-dir --upgrade pip


# Définir le répertoire de travail dans le conteneur
WORKDIR /app



# Mettre à jour le gestionnaire de paquets et installer les dépendances système nécessaires
RUN apt-get update


# Copier les fichiers de dépendances (requirements.txt), le back et le front dans le conteneur
COPY ./docker/requirements.txt .
COPY ./src/ ./back


# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt



# Exposer le port que l'application utilisera
EXPOSE 5000

ENV FLASK_APP=app


# Définir la commande à exécuter lorsque le conteneur démarre
CMD ["python", "./back/app.py"]
