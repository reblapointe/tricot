from flask import Flask, render_template, request
from models import modele


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/broches')
def broches():
    broches = [2, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 9, 10]
   
    signe = request.args.get('TailleSigne')
    valeur = request.args.get('TailleValeur')

    if signe and valeur:
        match signe:
            case '>':
                broches = [x for x in broches if x > float(valeur)]
            case '<':
                broches = [x for x in broches if x < float(valeur)]
            case '=':
                broches = [x for x in broches if x == float(valeur)]

    return render_template('broches.html', broches=broches, signe=signe or '>', valeur=valeur or '0')


@app.route('/echantillon')
def donnees():
    # Chargement du DataFrame
    df = modele.get_echantillon()
    
    # Conversion en listes pour Jinja2
    colonne = df.columns.tolist()
    rangees = df.values.tolist() 
    # print(rangees)
    # print(df.to_html())

    moyenne = df["8"].mean()
    return render_template("echantillon.html", moyenne=moyenne, colonnes=colonne, rangees=rangees)


@app.route('/atomes')
def atomes():
    df = modele.get_atomes()[["Element", "Symbol", "AtomicMass", "AtomicNumber", "MeltingPoint", "BoilingPoint"]]
    
    print(df.to_string())
    print(df["MeltingPoint"].max())
    # print(df.to_html())

    print(df["AtomicMass"].mean())
    print(df['AtomicMass'].corr(df['AtomicNumber'])) 
    colonne = df.columns.tolist()
    rangees = df.values.tolist() 
    moyenne = df["MeltingPoint"].mean()
    return render_template("atomes.html", moyenne=moyenne, colonnes=colonne, rangees=rangees)


@app.route('/demo')
def demo():
    nom = request.args.get('nom', 'le monde')
    return f"Bonjour {nom}!"


# Démo exception

# try:
#     montant = 100
#     x = 10
#     y = 0
#     print(montant / x)
#     print(montant / y)
# except ZeroDivisionError as erreur:
#     print('Erreur de division par zéro : ', erreur)
# except Exception as erreur:
#     print('Erreur inconnue : ', erreur)
# else:
#     # Bloc de code qui s'exécute si aucune exception n'est levée
#     print('Aucune exception levée!')
# finally:
#     # Bloc de code qui s'exécute toujours, qu'une exception soit levée ou non
#     print('Ce code sera toujours exécuté.')