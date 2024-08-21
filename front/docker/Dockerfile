# Utiliser une image de base officielle avec Python 3.9
FROM nginx:1.26-alpine3.19-slim

#Meta-données
LABEL version="1.0" 
LABEL maintainer="Sabeur Elkosantini"


# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/share/nginx/html

COPY ./src/ .

# Exposer le port que l'application utilisera
EXPOSE 80


