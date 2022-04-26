from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import utils
import emoji

app = Flask(__name__)


@app.route("/bot", methods=['POST'])
def bot():
    incoming_message = request.values.get("Body", '').lower()
    bot_response = MessagingResponse()
    bot_message = bot_response.message()
    # print(incoming_message)
    # print(type(incoming_message))
    if "start" in incoming_message:
        bot_message.body(emoji.emojize("""
        *Hi! I am a Url Shortner Bot* :waving_hand:\
            Just Drop any link and i will shorten it for you :winking_face:""", use_aliases=True))
    elif utils.validate_link(incoming_message):
        shorten_url = utils.shorten_url(incoming_message)
        bot_message.body(f"Your Short Url is:{shorten_url}")
    else:
        bot_message.body("Oh Sorry!! pls give a valid url..")
    return str(bot_response)


if __name__ == "__main__":
    app.run(debug=True)
