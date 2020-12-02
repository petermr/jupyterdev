#!/usr/bin/env python
#-*- coding: utf8 -*-

from PIL import Image
from ColorModule import Color
from Octree import OctreeQuantizer


def main():
    image = Image.open('/Users/pm286/projects/pathways/images/pmc6093421.jpeg')
    image = Image.open('/Users/pm286/workspace/jupyter/physchem/images/red_black_cv.png')
    pixels = image.load()
    width, height = image.size

    octree = OctreeQuantizer()

    # add colors to the octree
    for j in range(height):
        for i in range(width):
            octree.add_color(Color(*pixels[i, j]))

    # 256 colors for 8 bits per pixel output image
    size = 4 # might be 16
    palette = octree.make_palette(size * size)

    # create palette for 256 color max and save to file
    palette_image = Image.new('RGB', (size, size))
    palette_pixels = palette_image.load()
    for i, color in enumerate(palette):
        rgb = (color.red, color.green, color.blue)
#        print("rgb ", )
        palette_pixels[i % size, i // size] = rgb
    palette_image.save('rainbow_palette.png')

    # save output image
    out_image = Image.new('RGB', (width, height))
    out_pixels = out_image.load()
    for j in range(height):
        for i in range(width):
            index = octree.get_palette_index(Color(*pixels[i, j]))
            color = palette[index]
            out_pixels[i, j] = (color.red, color.green, color.blue)
    out_image.save('rainbow_out.png')


if __name__ == '__main__':
    main()
