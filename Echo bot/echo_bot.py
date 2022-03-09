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
    #responded = False
    #print(str(resp))
    if incoming_msg == "hello":
        msg.body(emoji.emojize("""
        *Hi! I am an Echo Bot* :waving_hand:
        Let's be Friends :winking_face:
        I can reply back to you what you wrote to me. :speaking_head:
        With an Emoji attached. :winking_face:
        Nice to Meet You! :grinning_face_with_big_eyes:""", use_aliases=True))
        #responded = True
    else:
    #if not responded:
        response = emoji.emojize(":robot:" + " : Hi!, You Wrote '" + incoming_msg + "'", use_aliases=True)
        msg.body(response)
    return str(resp)
    
if __name__ == '__main__':
    app.run(debug=True)