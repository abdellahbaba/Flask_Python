from flask import Flask

app = Flask(name)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for i in range(1, valeur + 1):
        etoiles += ' ' * (valeur + i) + '' i + '<br>'
    return etoiles

if name == "main":
    app.run(debug=True)

if __name__ == "__main__":
  app.run(debug=True)
