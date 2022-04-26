import requests
import pyqrcode
import lxml.html

s = "https://www.google.com"

url = pyqrcode.create(s)
#url.png('mygoogle.png', scale=8)

html = requests.get("https://www.reddit.com/r/memes/")
doc = lxml.html.fromstring(html.content)
print(doc)
images = doc.xpath('.//divimg[@alt="Post image"]')

print(images)
