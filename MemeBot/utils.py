import requests
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
        random_meme_data = random.choice(images)
        random_meme_url = random_meme_data['url']
        random_meme_name = random_meme_data['name']

        return [random_meme_name, random_meme_url]  # f"Url: {random_meme}"
    else:
        return f"Invalid Response:{data.status_code} Code"


#h = random_meme()
# print(h)
# def main():
# random_meme()
# if "__name__" == "__main__":
# main()
