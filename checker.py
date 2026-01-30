import requests
import os

URL = "https://www.jammukashmircablecar.com/"
CHECK_TEXTS = ["17 March", "17/03", "March 17"]

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

def check():
    r = requests.get(URL, timeout=20)
    page = r.text

    # ✅ Check if ANY text is present
    if any(text in page for text in CHECK_TEXTS):
        send_telegram("🚨 Gulmarg 17 March tickets AVAILABLE! Book now!")
    else:
        send_telegram("❌ Gulmarg tickets not opened yet.")

if __name__ == "__main__":
    send_telegram("Test message from Gulmarg bot ✅")
    check()
