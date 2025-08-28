from flask import Flask, request
import requests

app = Flask(__name__)

# 🔑 अपना Page Access Token यहाँ डालो
PAGE_ACCESS_TOKEN = "EAAebCpdxrz4BPV916GSL9I4LYOc3eXpZBQfskhvOSoul8ZAwW6DzgE9i2PoLJYJiUkCrE6xqn5ZAvZBRgsOmg66raAdKlFBHYVspD8wPZBxm3Bmp8TBsA4qIekbdPiVjkvfHlj4iFXGBLzjQroMS60YEFvkTcGpAUC6ZCvVzocBC672o58x8Xi6sBoCsX1afkhKeo47Wiz8wZDZD"

# 🛡️ वही Verify Token डालो जो Facebook App में भरा है
VERIFY_TOKEN = "EAAebCpdxrz4BPV916GSL9I4LYOc3eXpZBQfskhvOSoul8ZAwW6DzgE9i2PoLJYJiUkCrE6xqn5ZAvZBRgsOmg66raAdKlFBHYVspD8wPZBxm3Bmp8TBsA4qIekbdPiVjkvfHlj4iFXGBLzjQroMS60YEFvkTcGpAUC6ZCvVzocBC672o58x8Xi6sBoCsX1afkhKeo47Wiz8wZDZD"

# 🔒 Lock किया हुआ नाम और Group Thread ID
LOCKED_NAME = "🔥LOVE ENTER🔥"
GROUP_THREAD_ID = "1304942661186798"


# -----------------------------
# ✅ VERIFY (Facebook Webhook check)
# -----------------------------
@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200   # FB को hub.challenge वापस भेजना जरूरी है
    else:
        return "Verification failed", 403


# -----------------------------
# ✅ EVENT HANDLER (Messenger Events)
# -----------------------------
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("📩 Webhook Event:", data)

    # ⚡️ यहाँ तुम चेक कर सकते हो अगर group name बदला गया है
    # अभी के लिए सिर्फ log कर रहा है
    return "EVENT_RECEIVED", 200


# -----------------------------
# ✅ Function: Group Name Reset
# -----------------------------
def set_group_name():
    url = f"https://graph.facebook.com/v17.0/{GROUP_THREAD_ID}"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    data = {"name": LOCKED_NAME}
    response = requests.post(url, params=params, data=data)
    print("🔒 Group name reset response:", response.text)


# -----------------------------
# ✅ Run App (Render/Local)
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
