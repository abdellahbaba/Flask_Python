from flask import Flask

app = Flask(name)

@app.route('/')
def pyramide():
    n = 5
    output = []
    for i in range(1, n + 1):
        # Construction de chaque ligne
        line = '&nbsp;' * (n - i)  # Espaces HTML
        line += ''.join(map(str, range(1, i + 1)))
        line += ''.join(map(str, range(i - 1, 0, -1)))
        output.append(line + '<br>')

    return '<pre>' + ''.join(output) + '</pre>'

if name == 'main':
    app.run()

