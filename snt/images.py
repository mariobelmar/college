# run with
# :w|!clear; python images.py

import PIL.Image as pil

img = pil.open('data/paysage.jpeg')
img.show()
print(f'Largeur et hauteur de l"image: {img.size}')
# print(img.size)
# (600, 479)

largeur, hauteur = img.size
