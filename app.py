from flask import Flask

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    # webhook and logic here
    return
    
if __name__ == '__main__':
    app.run()

