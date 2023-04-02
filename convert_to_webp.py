import os
from PIL import Image

def conversie(fisier, ext):
    nume = fisier.split(ext)
    if len(nume) == 2:
        img = nume[0]+ext
        image = Image.open(img)
        image = image.convert('RGB')
        img_webp = nume[0]+'.webp'
        print (img_webp)
        image.save(img_webp, 'webp')

files = os.listdir()
for file in files:
    conversie(file, '.jpeg')
    conversie(file, '.jpg')
    conversie(file, '.png')
