# run with
# :w|!clear; python images.py

import PIL.Image as pil

img = pil.open('data/paysage.jpeg')
img_chat = pil.open('data/chat.jpeg')
# img.show()
# img_chat.show()

print(f'Largeur et hauteur de l"image: {img.size}')
# print(img.size)
# (600, 479)

largeur, hauteur = img.size

img_r = pil.new('RGB', (largeur, hauteur))
img_g = pil.new('RGB', (largeur, hauteur))
img_b = pil.new('RGB', (largeur, hauteur))

for l in range(largeur):
    for h in range(hauteur):
        r,g, b = img.getpixel((l, h))
        img_r.putpixel((l, h), (r, 0, 0))
        img_g.putpixel((l, h), (0, g, 0))
        img_b.putpixel((l, h), (0, 0, b))
# img_r.show()
# img_g.show()
# img_b.show()
img_r.save('paysage_rouge.png')
img_g.save('paysage_vert.png')
img_b.save('paysage_bleu.png')


img_chat = pil.open('data/chat.jpeg')
img = pil.open('data/paysage.jpeg')
img_mixt = pil.new('RGB', (largeur, hauteur))

for l in range(largeur):
    for h in range(hauteur-95):
        r1, g1, b1 = img.getpixel((l, h))
        r2, g2, b2 = img_chat.getpixel((l, h))
        img_mixt.putpixel((l, h), (max(r1, r2), max(g1, g2), max(b1, b2)))

img_mixt.show()
img_mixt.save('img_mixt.png')
