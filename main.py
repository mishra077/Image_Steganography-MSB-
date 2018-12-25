from Stegno import Stegno
from PIL import Image

img = Image.open(r'C:\Users\Dell\Desktop\CRYPTO_PROJ\landscape.jpg').convert('L')
x = Stegno(img)
x.encode(img)
x.decode()