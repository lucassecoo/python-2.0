from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista_jogos = ['clash royale', 'minecraft', 'god of war']
    return render_template('index.html', jogos = lista_jogos)

app.run()