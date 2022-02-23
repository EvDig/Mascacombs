import pygame
import sprite_groups as sg
import constants as c


class Finish(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(sg.finish_group, sg.all_sprites)
        self.image = c.finish_image_0
        self.image_1 = c.finish_image_1
        self.image_2 = c.finish_image_2
        self.iterations = 0
        self.frame = 1
        self.rect = self.image.get_rect().move(
            c.tile_width * pos_x, c.tile_height * pos_y)
        self.frames = [self.image, self.image_1, self.image_2]
        # Спрайты на случаи когда игрок двигался Вниз - Вверх - Влево - Вправо - Находится в движении

    def update(self):
        self.iterations += 1
        if self.iterations >= 5:
            self.iterations = 0
            self.image = self.frames[self.frame % 3]
            self.frame += 1
