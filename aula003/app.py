from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'lucas'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo("clash royale", "Estratégia", "Mobile")
jogo2 = Jogo("minecraft", "Mundo Aberto", "PC")
jogo3 = Jogo("God Of War", "Guerra", "PS2")

lista_jogos = [jogo1, jogo2, jogo3]

@app.route('/')
def index():

    return render_template('index.html', titulo= 'Tabela de jogos', jogos = lista_jogos)

@app.route('/novo')
def novo():
    return render_template('adicionar.html', titulo='Adicionar Jogo')

@app.route('/adicionar', methods = ['POST',])
def adicionar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novo_jogo =Jogo(nome, categoria, console)
    lista_jogos.append(novo_jogo)
    return render_template('index.html', titulo= 'Tabela de jogos', jogos = lista_jogos)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    if request.form['senha'] == 'senha':
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('falha ao logar usuário: '+ session['usuario_logado'])
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash(session['usuario_logado'] + ' deslogado com sucesso!')
    return redirect('/login')

app.run(debug = True)