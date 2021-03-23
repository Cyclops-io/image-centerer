#!/usr/bin/env python

import os, sys
from PIL import Image
from pathlib import Path
import argparse

def center(file, half=False, double=True):
    inputImage = Image.open(file)
    wi = inputImage.size[1]
    he = inputImage.size[0]
    if double:
        newWi = int(2*wi)
        newHe = int(2*he)
        topcorH = int(newHe/4)
        topcorW = int(newWi/4)
    elif half:
        newWi = int(1.5*wi)
        newHe = int(1.5*he)
        topcorH = int(newHe/6)
        topcorW = int(newWi/6)
    newImage = Image.new('RGBA', (newWi, newHe),(255,255,255,0))
    print(f'top corner = {topcorH} {topcorW}')
    newImage.paste(inputImage.copy(), (topcorH,topcorH))
    output_filename = file.stem + '_centered' + file.suffix
    newImage.save(output_filename)
    print(f'centered {file} as {output_filename}')

def main():
    parser = argparse.ArgumentParser(description='Sends a messge to a discord chat at 12:01AM with the days date.')
    parser.add_argument('-d', '--double', action='store_true', help='make new image 2x wide/tall')
    parser.add_argument('-a', '--half', action='store_true', help='make new image 1.5x wide/tall')
    parser.add_argument('file', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    print(f'{args.half}, {args.double}, {args.file}')

    with args.file as file:
        center(file, half=args.half, double=args.double)
    #try:
    #    inputImage.verify()
    #except Exception:
        #print('Invalid image')
    

if __name__ == "__main__":    
    sys.exit(main())

