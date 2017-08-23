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
    image_list = {}
    for i in range(num):
        image = Image.open(dir_path + '/%d.jpg'%(i+1))
        image_list.append(image.crop(default_box))

    return image_list

def generate_random_mat(tiles_num, output_size):
    tiles_mat = []
    for i in range(output_size[0]):
        tiles_mat[i] = [0]*output_size[1]
        for j in range(output_size[1]):
            while True:
                tmp = randint(0,8)
                if tiles_num[tmp] != 0:
                    tiles_num[tmp] -= 1
                    tiles_mat[i][j] = (tmp, randint(0,3))
                    break;
    print(tiles_mat)

    return tiles_mat




#(tile_index, rotate_index)
def compose_tiles(mat):


load_tiles('./input', 9)

tiles_mat = generate_random_mat()


