from wsgiref.util import request_uri
import requests
from sympy import re


def random_quote():
    '''a function to get random quotes'''
    response_quote = requests.get("https://zenquotes.io/api/today/ff5e73b15a05ca51951b758bd7943ce803d71772")
    if response_quote.status_code == 200:
        quote_data = response_quote.json()
        quote = quote_data[0]['q']
        quote_author = quote_data[0]['a']
        quote_message = f"'{quote_author.title()}' Said:{quote}"

        return quote_message

    else:
        return f"Invalid Request {response_quote.status_code}"

def jokes():
    '''this function gets a joke'''
    response_joke = requests.get("https://some-random-api.ml/joke")
    if response_joke.status_code == 200:
        joke = response_joke.json()

        return joke['joke']
    else:
        return f"Invalid Request {response_joke.status_code}"


def cat_dog(input_message):
    if "cat" in input_message:
        response_cat = requests.get("https://cataas.com/cat/cute")
        cat = response_cat.url

        return cat
    elif "gif" in  input_message:
        response_gif = requests.get("https://cataas.com/cat/gif")
        cat_gif = response_gif.url

        return cat_gif