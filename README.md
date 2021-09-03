# Simple projet en python

## démarrage

```shell
# lancer l'environnement virtuel
python -m venv .venv
# activer l'environnement virtuel
# pour powershell :
.\.venv\Scripts\Activate.ps1
# pour cmd :
.\.venv\Scripts\Activate.bat
# installer les dépendances du projet
pip install -r requirements
```

## notes

```shell
# pour sauvegarder les dépendances
pip freeze > requirements.txt

# lancer les tests
pytest
```
