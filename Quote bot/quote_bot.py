from crypt import methods
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import emoji


app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    pass





if __name__ == "__main__":
    app.run()