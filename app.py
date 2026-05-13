from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN    = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_IDS = os.environ.get("TELEGRAM_CHAT_IDS", "").split(",")

@app.route("/enviar", methods=["GET"])
def enviar():
    texto = request.args.get("texto", "")
    if not texto:
        return "sem texto", 400

    url = "https://api.telegram.org/bot{}/sendMessage".format(TELEGRAM_TOKEN)
    for chat_id in TELEGRAM_CHAT_IDS:
        requests.post(url, json={
            "chat_id": chat_id.strip(),
            "text": texto,
            "parse_mode": "HTML"
        })
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
