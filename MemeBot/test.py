import pyqrcode

s = "https://www.google.com"

url = pyqrcode.create(s)

url.png('mygoogle.png', scale=8)
