import requests
import urllib
import random

username = "MusaAdamuWakili"
password = "meme_bot_1234"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"


def random_meme():
    data = requests.get("https://api.imgflip.com/get_memes")
    if data.status_code == 200:
        meme_data = data.json()['data']['memes']
        images = [{'name': image['name'], 'url':image['url'],
                   'id':image['id']} for image in meme_data]
        random_meme = random.choice(images)['url']
        return random_meme
    else:
        return f"Invalid Response:{data.status_code} Code"


def main():
    random_meme()


# if "__name__" == "__main__":
main()
