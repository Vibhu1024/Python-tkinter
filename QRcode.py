import pyqrcode
import png
from pyqrcode import QRCode
s= "www.google.com"
url = pyqrcode.create(s)
url.svg("myqt.svg", scale = 8)
url.png('myqrcode.png', scale = 6)

#url = pyqrcode.create('http://uca.edu')
#url.svg('uca-url.svg', scale=8)
#url.png('myqrcode.png', scale = 6)
#print(url.terminal(quiet_zone=1))