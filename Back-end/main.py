from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor Python funcionando!"

@app.route("/jaca")
def api():
    return {
        "mensagem": "Minha API em Python"
    }
@app.route("/neymar")
def mensagem():
    return {
        "mensagem": "usuario entrou!"
    }
   
if __name__ == "__main__":
    app.run(debug=True)