from flask import Flask, request
import requests

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAebCpdxrz4BPZAikkaxzHDdOc4ZBllUkRhTVY3ijZCMw4NJqIRvXLTNvzZAZC9NEbZBKO4veZCqzZC7eyQdidmArHMyd5haZB7CC6iGzgkPteduvZCRomeDZCYHcFaKMwx3VIpKoMhj8VM8ZARrTN0PftVkHGiZC0JIqCISZCH56n2Egn2rAPL19KvjTS1qD9E4eDmJFkKNmPvN4KQnAZDZD"
LOCKED_NAME = "🔥TESTING BOT🔥"
GROUP_THREAD_ID = "1304942661186798"

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
