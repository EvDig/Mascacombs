import pygame
import sprite_groups as sg
import constants as c


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sg.tiles_group, sg.all_sprites)
        self.image = c.tile_images[tile_type]
        if tile_type == 'wall':
            self.add(sg.wall_group)
        if tile_type == 'saw':
            self.add(sg.saw_group)
        self.rect = self.image.get_rect().move(
            c.tile_width * pos_x, c.tile_height * pos_y)

