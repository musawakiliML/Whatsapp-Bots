from crypt import methods
from email import message
import re
from urllib import response
from flask import Flask, request
import utils
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    incoming_message = request.values.get('Body', "").lower()
    response = MessagingResponse()
    message = response.message()

    if "meme" in incoming_message:
        meme = utils.random_meme()
        message.media(meme[1])
        message.body(meme[0])

    return str(response)
