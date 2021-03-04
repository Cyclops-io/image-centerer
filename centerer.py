#!/usr/bin/env python

import os, sys
from PIL import Image

def center(file):
    inputImage = Image.open(file)
    try:
        inputImage.verify()
    except Exception:
        print('Invalid image')
    wi = inputImage.size[1]
    he = inputImage.size[0]
    newWi = int(2*wi)
    newHe = int(2*he)
    newImage = Image.new('RGBA', (newWi, newHe),(255,255,255,0))
    topcorH = int(he/2)
    topcorW = int(wi/2)
    newImage.paste(inputImage.copy(), (topcorH,topcorH))
    newName = sys.argv[1].split(".")[0]
    newName += '_Centered.png'
    newImage.save(name, "PNG")

if __name__ == "__main__":    
    #center(str(sys.argv[1]))
    inputImage = Image.open("bank.png")
    wi = inputImage.size[1]
    he = inputImage.size[0]
    newWi = int(2*wi)
    newHe = int(2*he)
    newImage = Image.new('RGBA', (newWi, newHe),(255,255,255,0))
    topcorH = int(he/2)
    topcorW = int(wi/2)
    newImage.paste(inputImage.copy(), (topcorH,topcorH))
    newName = sys.argv[1].split(".")[0]
    newName += '_Centered.png'
    newImage.save('centeredBank.png')

    #print(f'centered {name} as {newName}')
