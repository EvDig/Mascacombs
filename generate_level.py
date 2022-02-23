import os
import sys

import pygame

import sprite_groups as sg
import constants as c
from tile import Tile
from load_image import load_image
from load_level import load_level
from terminate import terminate
from player import Player
import screens


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '*':
                Tile('saw', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y
