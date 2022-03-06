from crypt import methods
from distutils.log import debug
from urllib import response
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import emoji

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_message = request.values.get("Body", '').lower()
    response = MessagingResponse()
    message = response.message()

    if incoming_message == 'hello':
        message.body("Hello, i am a test bot")
    
    return str(response)
if __name__ == "__main__":
    app.run(debug=True)