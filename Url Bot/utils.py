import requests
from urllib.parse import urlparse

# your account details
username = "o_36um82e226"
password = "pro244grammer."

# get authentication key


def get_auth_key():

    auth_key_response = requests.post(
        "https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))

    if auth_key_response.status_code == 200:
        auth_key = auth_key_response.content.decode()
        # print(auth_key)
        return auth_key
    else:
        return f"Invalid Request {auth_key_response.status_code} Status Code"


headers = {"Authorization": f"Bearer {get_auth_key()}"}


def get_guid():
    groups_guid = requests.get(
        "https://api-ssl.bitly.com/v4/groups", headers=headers)
    if groups_guid.status_code == 200:
        guid = groups_guid.json()['groups'][0]['guid']
        # print(guid)
        return guid
    else:
        return f"Invalid Request{groups_guid.status_code} Status Code"


def shorten_url(url):
    auth_key = get_auth_key()
    guid = get_guid()

    link_url = url

    url_shortner = requests.post("https://api-ssl.bitly.com/v4/shorten", json={
                                 "group_guid": guid, "long_url": url}, headers=headers)
    if url_shortner.status_code == 200:
        url_response = url_shortner.json()['link']
        # print(url_response)
        return url_response
    else:
        return f"Invalid Request {url_shortner.status_code} Status Code"


def validate_link(link):
    min_attr = ('scheme', 'netloc')
    try:
        result = urlparse(link)
        if all([result.scheme, result.netloc]):
            return True
        else:
            return False
    except ValueError:
        return False


# shorten_url("https://www.linkedin.com/in/musa-adamu-wakili-711704154/")
#auth_key = get_auth_key()
# is_url = validate_link(
 #   "https://www.linkedin.com/in/musa-adamu-wakili-711704154/")
# print(is_url)
