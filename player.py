import pygame

import sprite_groups as sg
import constants as c

pygame.init()
screen = pygame.display.set_mode(c.size)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(sg.player_group)
        self.speed = 900
        self.image = c.player_image
        self.moving_image = c.player_moving_image
        self.on_right_wall = c.player_on_right_wall
        self.on_left_wall = c.player_on_left_wall
        self.rect = self.image.get_rect().move(
            c.tile_width * pos_x + 15, c.tile_height * pos_y + 5)
        self.frames = [self.image, pygame.transform.flip(self.image, True, True),
                       self.on_right_wall,
                       self.on_left_wall, self.moving_image]
        # Спрайты на случаи когда игрок двигался Вниз - Вверх - Влево - Вправо - Находится в движении

    def update(self, direction, moving):
        if not moving:
            if direction == 'down':
                self.image = self.frames[0]

            elif direction == 'up':
                self.image = self.frames[1]

            elif direction == 'right':
                self.image = self.frames[2]

            elif direction == 'left':
                self.image = self.frames[3]

            else:
                self.image = self.frames[0]
        else:
            self.image = self.frames[4]
