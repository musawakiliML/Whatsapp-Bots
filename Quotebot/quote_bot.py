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

    if incoming_message == 'hello' or "Hello":
        message.body("""Hello, i am a Bot :robot: :
        I can do the following things:
        1.Tell you Joke (Just type "joke")
        2.Tell a Qoute(Just type "joke")
        3.Show Pictures of animals (cat and dog)
        4.Get you a Meme(just type the command "meme")
        """)
    elif incoming_message == "aisha":
        message.body(emoji.emojize("Hello Aishatunah :red_heart: \n You look glamorous :rose:"))
    
    return str(response)
    
if __name__ == "__main__":
    app.run(debug=True)