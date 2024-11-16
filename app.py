from flask import Flask, render_template

#aplicação Flask
app = Flask(__name__)

#rota que receben o nome e retorna a saudação
@app.route('/saudacao/<nome>')
def saudacao(nome):
    return (f"Oi {nome}!")

#rodar a aplicação
if __name__ == '__main__':
    app.run(debug= True)