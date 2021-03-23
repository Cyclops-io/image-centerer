#!/usr/bin/env python

import os, sys
from PIL import Image
from pathlib import Path
import argparse

if __name__ == "__main__":
    f = Path(sys.argv[1])
    print(sys.argv[1])
    inputImage = Image.open(sys.argv[1])
    wi = inputImage.size[1]
    he = inputImage.size[0]
    newWi = int(1.5*wi)
    newHe = int(1.5*he)
    topcorH = int(newHe/6)
    topcorW = int(newWi/6)
    newImage = Image.new('RGBA', (newWi, newHe),(255,255,255,0))
    print(f'top corner = {topcorH} {topcorW}')
    newImage.paste(inputImage.copy(), (topcorH,topcorH))
    output_filename = f.stem + '_centered' + f.suffix
    print(output_filename)
    newImage.save(output_filename)
    print(f'centered {f} as {output_filename}')

