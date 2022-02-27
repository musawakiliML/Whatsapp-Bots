from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import emoji


app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    # webhook and logic here
    incoming_msg = request.values.get('Body','').lower()
    resp = MessagingResponse()
    msg = resp.message()
    #print(str(resp))
    if incoming_msg == "start" or "hello":
        msg.body(emoji.emojize("""
        *Hi! I am an Echo Bot* :wave:
        Let's be Friends :wink:
        I can reply back to you what you wrote to me. :speaking head:
        With an Emoji attached. :wink:
        Nice to Meet You! :grinning_face_with_big_eyes:"""))
    else:
        msg.body(emoji.emojize(incoming_msg+" :robot:"))
    return str(resp)
    
if __name__ == '__main__':
    app.run()