#!/usr/bin/env python
#####################################################
#
# Filename      : floor_join.py
#
# Author        : JiangTingyu - Jiangty08@gmail.com
# Description   : ---
# Create        : 2017-08-23 19:47:47
# coding=utf-8
#####################################################


import os
import time
from PIL import Image
from random import randint

image_width = 630
image_height = 630
image_left = 10
image_top = 10
default_box = (image_top, image_left, image_top+image_height, image_left+image_width)


tiles_num = [6, 4, 5, 5, 6, 9, 16, 6, 6]

tiles_rotate = [0, 90, 180, 270]

output_size = (5, 11)
output_height = image_height*output_size[0]
output_width = image_width*output_size[1]


def load_tiles(dir_path, num):
    """
    load tile picture from jpg
    """
    image_list = []
    for i in range(num):
        image = Image.open(dir_path + '/%d.jpg'%(i+1))
        image_list.append(image.crop(default_box))

    return image_list


def generate_random_mat(tiles_num, output_size):
    """
    generate floors map, random
    @tiles_num: tiles number(we have) of all types
    @output_size: size of floor, need how many tiles
    """
    tiles_mat = [0] * output_size[0]
    for i in range(output_size[0]):
        tiles_mat[i] = [0]*output_size[1]
        for j in range(output_size[1]):
            while True:
                tmp = randint(0,8)
                if tiles_num[tmp] != 0:
                    tiles_num[tmp] -= 1
                    tiles_mat[i][j] = (tmp+1, randint(0,3))
                    break;
    print(tiles_mat)

    return tiles_mat

def generate_fix_mat(tiles_mat, tiles_num, output_size):
    """
    generate floors map, part of the map fixed
    @tiles_mat: input floors map, with part of the mpa fixed
    @tiles_num: tiles number(we have) of all types
    @output_size: size of floor, need how many tiles
    """
    for i in range(output_size[0]):
        for j in range(output_size[1]):
            if tiles_mat[i][j] != (0,0):
                index, _ = tiles_mat[i][j]
                tiles_num[index-1] -= 1
    print(tiles_mat)

    for i in range(output_size[0]):
        for j in range(output_size[1]):
            while True:
                if tiles_mat[i][j] != (0,0):
                    break;
                tmp = randint(0,8)
                if tiles_num[tmp] != 0:
                    tiles_num[tmp] -= 1
                    tiles_mat[i][j] = (tmp+1, randint(0,3)) #index start from 1
                    break;
    print(tiles_mat)

    return tiles_mat




def compose_tiles(mat, images):
    """
    compose the floor pic, using floor map and tile images
    @mat: floor map matrix, elements means (image_index, rotate_index)
    @images: image list witch contains all tiles picture
    """
    canvas = Image.new('RGB', (output_width, output_height))
    l, t, r, b = 0, 0, image_width, image_height
    for lines in mat:
        for tile in lines:
            index, rotate = tile
            #index start from 1
            canvas.paste(images[index-1].rotate(tiles_rotate[rotate]), (l, t, r, b))
            l += image_width
            r += image_width
        l, r = 0, image_width
        t += image_height
        b += image_height

    # save the map
    canvas.save('output/%d.jpg'%int(time.time()), quality = 100)
    return 0


if __name__ == "__main__":

    if not os.path.exists("./output"):
        os.mkdir("./output")


    choose = 0

    # total random
    if choose == 0:

        tiles_image = load_tiles('./input', 9)

        tiles_mat = generate_random_mat(tiles_num, output_size)

        compose_tiles(tiles_mat, tiles_image)


    # fix floor map
    if choose == 1:

        mat_1 = [
                [(6,1), (9,0), (1,0), (4,3), (5,0), (9,0), (6,1), (5,0), (7,0), (8,0),
                    (7,0)],
                [(1,0), (5,0), (8,0), (7,0), (2,3), (3,0), (7,0), (4,0), (6,2), (1,0),
                    (9,0)],
                [(7,0), (4,0), (6,0), (3,0), (9,0), (1,0), (6,2), (8,0), (1,0), (3,0),
                    (6,2)],
                [(2,0), (3,0), (8,0), (2,2), (5,0), (8,0), (4,1), (5,0), (9,0), (6,0),
                    (7,0)],
                [(6,3), (5,0), (1,0), (7,0), (4,0), (6,3), (9,0), (2,1), (3,0), (7,0),
                    (8,0)]
                ]
        tiles_image = load_tiles('./input', 9)

        compose_tiles(mat_1, tiles_image)

    # fix part of the floor map
    if choose == 2:

        mat_1 = [
                [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (6,0), (0,0), (6,3), (0,0),
                    (0,0)],
                [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (3,0), (0,0), (0,0),
                    (0,0)],
                [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (6,1), (0,0), (6,2), (0,0),
                    (0,0)],
                [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0),
                    (0,0)],
                [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0),
                    (0,0)]
                ]
        mat_2 = [
                [(0,0), (0,0), (4,0), (0,0), (0,0), (0,0), (6,0), (6,3), (3,0), (0,0),
                    (0,0)],
                [(0,0), (0,0), (0,0), (4,0), (0,0), (0,0), (6,1), (6,2), (0,0), (3,0),
                    (0,0)],
                [(4,1), (0,0), (0,0), (0,0), (4,0), (3,0), (0,0), (0,0), (0,0), (0,0),
                    (0,0)],
                [(0,0), (4,1), (6,0), (6,3), (0,0), (0,0), (3,0), (0,0), (0,0), (0,0),
                    (0,0)],
                [(0,0), (0,0), (6,1), (6,2), (0,0), (0,0), (0,0), (3,0), (0,0), (0,0),
                    (0,0)]
                ]

        tiles_image = load_tiles('./input', 9)

        tiles_mat = generate_fix_mat(mat_2, tiles_num, output_size)

        compose_tiles(tiles_mat, tiles_image)
