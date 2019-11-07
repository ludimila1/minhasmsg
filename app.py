from flask import Flask, render_template
from flask_sqlalchemy import SQLAlquemy

app = Flask(__name__)
db=SQLAlquemy(app)

app.config["SCLALCHEMY_DATABASE_URI"] = "sqlite:///minhasmensagens.db"

class Mensagens(db.Model):
    id = db.Column(db.integer, primary_key=True)
    mensagem = db.Column(db.Text, nullable=False)

    def __repre__(self):
        return "<<<MSG: %r>>>"self.mensagem



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nova-mensagem")
def novaMensagem():
    return render_template("mensagens.html")


if __name__ == "__main__":
    app.run(debug=True)

