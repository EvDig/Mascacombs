import os
import sys

import pygame

import sprite_groups as sg
import constants as c
from variables import tick
from tile import Tile
from load_image import load_image
from load_level import load_level
from terminate import terminate
from player import Player
import screens


class Camera:

    def apply(self, obj, direction, moving):
        if moving:
            if direction == 'up':
                obj.rect.y += tick
            elif direction == 'down':
                obj.rect.y -= tick
            elif direction == 'right':
                obj.rect.x -= tick
            elif direction == 'left':
                obj.rect.x += tick
        else:
            if direction == 'up':
                obj.rect.y -= tick - 5
            elif direction == 'down':
                obj.rect.y += tick
            elif direction == 'right':
                obj.rect.x -= tick
            elif direction == 'left':
                obj.rect.x += tick

    def revival_position(self, obj, direction):
        if direction == 'up':
            obj.rect.y += -tick
        elif direction == 'down':
            obj.rect.y -= -tick
        elif direction == 'right':
            obj.rect.x -= -tick
        elif direction == 'left':
            obj.rect.x += -tick
