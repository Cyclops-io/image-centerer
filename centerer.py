#!/usr/bin/env python

import os, sys
from PIL import Image

def center(file):
    inputImage = Image.open(file)
    wi = inputImage.shape[1]
    he = inputImage.shape[0]
    newWi = 2*wi
    newHe = 2*he
    image = Image.new('RGBA', (newWi, newHe))
    image.putalpha(0) 
    
    name = os.path.splitext(file)[0]
    name +=  '_Centered.png'

    img.save(name, "PNG")