#!/usr/bin/env python
#-*- coding: utf8 -*-

from PIL import Image
import Octree as oct

def main():
    image = Image.open('/Users/pm286/projects/pathways/images/pmc6093421.jpeg')
    image = Image.open('/Users/pm286/workspace/jupyter/physchem/images/red_black_cv.png')
    out_image = oct.quantize(image)
    out_image.save('rainbow_out.png')


if __name__ == '__main__':
    main()
