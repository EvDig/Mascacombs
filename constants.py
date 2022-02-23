from load_image import load_image
import pygame

tile_images = {
    'wall': load_image('block.png'),
    'empty': load_image('air.png'),
    'saw': load_image('saw.png')
}
player_image = load_image('player.png')
player_moving_image = load_image('player_moving.png')
player_on_right_wall = load_image('player_on_right_wall.png')
player_on_left_wall = load_image('player_on_left_wall.png')
tile_width = tile_height = 50

fps = 144
clock = pygame.time.Clock()
size = width, height = 400, 400
