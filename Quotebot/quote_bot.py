from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import emoji
import utils

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_message = request.values.get("Body", '').lower()
    response = MessagingResponse()
    message = response.message()

    if incoming_message == 'hello' or "Hello":
        message.body(emoji.emojize("""Hello, i am a Bot :robot: :
        I can do the following things:
        1. Tell you Joke (Just type "joke")
        2. Tell a Qoute(Just type "joke")
        3. Show Pictures and Gif of animals (Just type a "cat" or "dog" or "gif cat")
        4. Get you a Meme :smiling_face:(just type the command "meme")
        """))
    elif "quote" or "Quote" in incoming_message:
        #message.body(emoji.emojize("Hello Aishatunah :red_heart: \n You look glamorous :rose:"))
        quote = utils.random_quote()
        message.body(quote)
    
    return str(response)
    
if __name__ == "__main__":
    app.run(debug=True)