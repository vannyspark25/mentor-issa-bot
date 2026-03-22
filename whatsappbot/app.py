from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# ─── Auto-reply message ───────────────────────────────────────────────────────
BOT_REPLY = """🤝 *KARIBU NDUGU!*

Mimi ni bot ya Mentor Issa. Nimepokea ujumbe wako!

*NISAVE MENTOR ISSA JE?* Wewe nikusave nani kabla sijaanza kukupa mafunzo 😊

📌 Jiunge hapa kuna mafunzo zaidi👇
https://chat.whatsapp.com/IPabNT6dnTzKcEDPCxvStf?mode=gi_t

✅✅✅✅✅
📌 *Tazama video zote ili uelewe*

Kwa mtaji ni *15,000 tu* ambayo unalipia mara moja tu — hulipii tena! 💰

✅ Unaanza kutengeneza pesa
✅ Kazi yako NI kutazama video tu
✅ Pesa inakuingia kila siku
✅ Unatoa pesa moja kwa moja kwenye Lain yako

👉 *Ukiwa tayari sema NDIO* nikupe maelekezo ufungue account yako! 🚀"""

NDIO_REPLY = """✅ *Vizuri sana NDUGU!*

Hii ndiyo hatua unayofuata:

1️⃣ Niambie *jina lako kamili*
2️⃣ Niambie *namba yako ya M-Pesa/Lain*
3️⃣ Nitakusaidia kufungua account yako hatua kwa hatua

Mtaji ni *KSh 15,000 / TZS 270,000* — unalipia MARA MOJA tu! 💯

Nipigie simu au niandikia hapa tutamaliza haraka! 🙌"""


@app.route("/bot", methods=["POST"])
def bot():
    incoming = (request.values.get("Body", "") or "").strip().upper()
    resp = MessagingResponse()

    if "NDIO" in incoming or "NDIYO" in incoming or "YES" in incoming:
        resp.message(NDIO_REPLY)
    else:
        resp.message(BOT_REPLY)

    return str(resp)


@app.route("/")
def home():
    return "✅ Mentor Issa WhatsApp Bot is running!", 200


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
