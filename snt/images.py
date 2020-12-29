# run with
# :w|!clear; python images.py

import PIL.Image as pil

img = pil.open('data/paysage.jpeg')
img.show()

print(img.size)
largeur, hauteur = img.size
