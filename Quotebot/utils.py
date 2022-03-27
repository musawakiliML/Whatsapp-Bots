import requests


def random_quote():
    '''a function to get random quotes'''
    response_quote = requests.get()
    if response_quote.status_code == 200:
        quote_data = response_quote.json()
        quote = quote_data[0]['q']
        quote_author = quote_data[0]['a']
        quote_message = f"'{quote_author.title()}' Said:{quote}"

        return quote_message



def jokes():
    '''this function gets a joke'''
    response_joke = requests.get("")
    if response_joke.status_code == 200:
        joke = response_joke.json()

        return joke['joke']
    else:
        return f"Invalid Request {response_joke.status_code}"
    

