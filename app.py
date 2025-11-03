# app.py

import secrets_email  # Importa as configurações de email
from flask import Flask, render_template, request, redirect
from config import CONFIG # Importa a configuração
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações do Flask-Mail usando secrets_email
app.config['MAIL_SERVER'] = getattr(secrets_email, 'MAIL_SERVER', 'smtp.example.com')
app.config['MAIL_PORT'] = getattr(secrets_email, 'MAIL_PORT', 587)
app.config['MAIL_USE_TLS'] = getattr(secrets_email, 'MAIL_USE_TLS', True)
app.config['MAIL_USERNAME'] = getattr(secrets_email, 'MAIL_USERNAME', 'seu.email@exemplo.com')
app.config['MAIL_PASSWORD'] = getattr(secrets_email, 'MAIL_PASSWORD', 'sua_senha')
app.config['MAIL_DEFAULT_SENDER'] = getattr(secrets_email, 'MAIL_DEFAULT_SENDER', app.config['MAIL_USERNAME'])
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html', config=CONFIG)

@app.route('/enviar_email', methods=['POST'])
def enviar_email():
    assunto = request.form['assunto']
    mensagem = request.form['mensagem']

    # Usa destinatário do arquivo de secrets_email ou um padrão
    destinatario = getattr(secrets_email, 'MAIL_RECIPIENT', 'destino@exemplo.com')

    msg = Message(subject=assunto,
                  recipients=[destinatario],
                  body=mensagem)

    mail.send(msg)

    return redirect('/#contato')

def index():
    return render_template("index.html", config=CONFIG)

if __name__ == '__main__':
    app.run(debug=True)