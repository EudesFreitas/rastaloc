from flask import Flask, request, redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL_DESTINO = "eudes.fcine@gmail.com"

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    producao = request.form.get('producao')
    data = request.form.get('data')
    mensagem = request.form.get('mensagem')

    msg = EmailMessage()
    msg['Subject'] = 'Novo pedido de orçamento'
    msg['From'] = 'contato@empresa.com'
    msg['To'] = 'contato@empresa.com'
    msg['Reply-To'] = email

    msg.set_content(f"""
    Novo orçamento recebido

    Nome: {nome}
    Email: {email}
    Produção: {producao}
    Data: {data}

    Mensagem:
    {mensagem}
    """)

    with smtplib.SMTP('smtp.seuprovedor.com', 587) as smtp:
        smtp.starttls()
        smtp.login('contato@empresa.com', 'SENHA_DO_EMAIL')
        smtp.send_message(msg)

    return redirect('/obrigado.html')


if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, request

app = Flask(__name__)

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    producao = request.form.get('producao')
    data = request.form.get('data')
    mensagem = request.form.get('mensagem')

    print("📩 NOVO ORÇAMENTO")
    print("Nome:", nome)
    print("Email:", email)
    print("Produção:", producao)
    print("Data:", data)
    print("Mensagem:", mensagem)

    return "Orçamento recebido com sucesso!"

app.run()
