from flask import Flask, request
import requests

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "YOUR_PAGE_TOKEN"
LOCKED_NAME = "🔥 My Group 🔥"
GROUP_THREAD_ID = "YOUR_GROUP_CHAT_ID"

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == "namelock123":  # Verify Token
        return request.args.get("hub.challenge")
    return "Verification failed"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    # यहाँ event check करके name reset कर सकते हो
    print(data)
    return "ok"

def set_group_name():
    url = f"https://graph.facebook.com/v17.0/{GROUP_THREAD_ID}"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    data = {"name": LOCKED_NAME}
    requests.post(url, params=params, data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
