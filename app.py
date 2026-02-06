from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL_REMETENTE = "denilsonnunessantos554@gmail.com"
SENHA_EMAIL = "vppg oxnh kiqs ojbm"
EMAIL_DESTINO = "denilsonnunessantos554@gmail.com"  # pode ser outro

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]

        msg = EmailMessage()
        msg["Subject"] = "Novo contato pelo site"
        msg["From"] = EMAIL_REMETENTE
        msg["To"] = EMAIL_DESTINO

        msg.set_content(f"""
        Nome: {nome}
        Email: {email}

        Mensagem:
        {mensagem}
        """)

        with smtplib.SMTP_SSL("smtp.gmail.com", 587) as smtp:
            smtp.login(EMAIL_REMETENTE, SENHA_EMAIL)
            smtp.send_message(msg)

        return redirect(url_for("contato"))

    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)
