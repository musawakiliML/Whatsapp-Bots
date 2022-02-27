from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    # webhook and logic here
    incoming_msg = request.values.get('Body','').lower()
    resp = MessagingResponse()
    msg = resp.message()
    #print(str(resp))
    if 'start' in incoming_msg:
        msg.body("""I am an Echo Bot, by job is to reply back to you what
        you wrote to me. Nice to Meet You!""")
    else:
        msg.body(incoming_msg)
    return str(resp)
    
if __name__ == '__main__':
    app.run()