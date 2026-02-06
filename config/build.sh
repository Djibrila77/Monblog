#!/usr/bin/env bash
# Arrêter le script en cas d'erreur
set -o errexit

# Installer les dépendances
pip install -r requirements.txt

# Collecter les fichiers statiques (pour WhiteNoise)
python manage.py collectstatic --no-input

# Appliquer les migrations de base de données
python manage.py migrate