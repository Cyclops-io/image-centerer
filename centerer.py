#!/usr/bin/env python

import os, sys
from PIL import Image
from pathlib import Path

if __name__ == "__main__":    
    file = Path(sys.argv[1])
    #try:
    #    inputImage.verify()
    #except Exception:
        #print('Invalid image')
    inputImage = Image.open(file)
    wi = inputImage.size[1]
    he = inputImage.size[0]
    newWi = int(2*wi)
    newHe = int(2*he)
    newImage = Image.new('RGBA', (newWi, newHe),(255,255,255,0))
    topcorH = int(he/2)
    topcorW = int(wi/2)
    newImage.paste(inputImage.copy(), (topcorH,topcorH))
    output_filename = file.stem + '_centered' + file.suffix
    newImage.save(output_filename)
    print(f'centered {file} as {output_filename}')
