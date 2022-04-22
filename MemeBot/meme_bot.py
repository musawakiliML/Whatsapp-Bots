from flask import Flask, request
import utils
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    incoming_message = request.values.get('Body', "").lower()
    response = MessagingResponse()
    message = response.message()
    if incoming_message == "Hello" or incoming_message == "hello":
        message.body("This is a Meme Bot:\
                    1. Random Meme\
                    2. Create Meme. ")
    elif "meme" in incoming_message:
        meme = utils.random_meme()
        message.media(meme[1])
        message.body(meme[0])

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)
