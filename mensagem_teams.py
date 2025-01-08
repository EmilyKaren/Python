import requests
import json
from datetime import datetime

data = datetime.now()
dt = data.strftime("%d-%m-%Y %H:%M:%S")

def mensagem_teams():
    url_webhook = "https://agropeuind.webhook.office.com/webhookb2/6d02bda9-d755-4bdf-aacd-efb27de78fb3@80bcc796-ae6c-4d5c-909b-f5ae4287583f/IncomingWebhook/66d9c9a374c94a7bbde569c1cce27aec/7406cfcf-8485-4959-a30d-3f034251e69c"

    headers = {
        'Content-Type': 'application/json'
    }

    mensagem = {
        "text": "\nErro na execução\n"
                "\ndata e hora do erro: {dt}\n"
    }

    response = requests.post(url_webhook, headers=headers, data=json.dumps(mensagem))

    if response.status_code == 200:
        print("Mensagem enviada com sucesso.")
    else:
        print(f"Falha ao enviar mensagem: {response.status_code}, {response.text}")

# Chamar a função para enviar a mensagem
mensagem_teams()
