from flask import Flask, render_template, request
from models import modele

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/broches')
def broches():
    broches = [2, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 9, 10]
    return render_template('broches.html', broches=broches)


@app.route('/echantillon')
def donnees():
    # Chargement du DataFrame
    df = modele.get_donnees()
    
    # Conversion en listes pour Jinja2
    colonne = df.columns.tolist()
    rangees = df.values.tolist()    
    moyenne = df["8"].mean()
    return render_template("echantillon.html", moyenne=moyenne, colonnes=colonne, rangees=rangees)

@app.route('/demo')
def demo():
    nom = request.args.get('nom', 'le monde')
    return f"Bonjour {nom}!"