def generer_pyramide(valeur):
    for i in range(1, valeur + 1):
       
        espaces = ' ' * (valeur - i)
        
      
        gauche = ''.join(str(j) for j in range(1, i + 1))
        
    
        droite = ''.join(str(j) for j in range(i - 1, 0, -1))
        

        ligne = espaces + gauche + droite
        
        print(ligne)


generer_pyramide(5)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Ceci est affiché à l’écran du visiteur, pas dans les logs."



