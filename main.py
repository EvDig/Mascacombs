import pygame

import sprite_groups as sg
import constants as c
import variables as v
from load_level import load_level
from camera import Camera
from generate_level import generate_level
import screens

pygame.init()
screen = pygame.display.set_mode(c.size)

screens.start_screen()
camera = Camera()
v.camera = camera
player, level_x, level_y = generate_level(load_level(screens.level_choose_screen()))
key = ''
v.tick = round(player.speed / c.fps)
direction = ''
moving = False
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            screens.exit_screen()
        if event.type == pygame.KEYDOWN and not moving:
            key = event.key
            moving = True

    if moving:
        if pygame.sprite.spritecollideany(player, sg.saw_group):
            moving = False
            screens.death_screen(direction)
        if key == pygame.K_UP:
            direction = 'up'
            if pygame.sprite.spritecollideany(player, sg.wall_group):
                player.rect.y += v.tick - 1
                moving = False
            for sprite in sg.all_sprites:
                camera.apply(sprite, direction, moving)
        elif key == pygame.K_DOWN:
            direction = 'down'
            if pygame.sprite.spritecollideany(player, sg.wall_group):
                player.rect.y -= v.tick - 5
                moving = False
            for sprite in sg.all_sprites:
                camera.apply(sprite, direction, moving)
        elif key == pygame.K_RIGHT:
            direction = 'right'
            if pygame.sprite.spritecollideany(player, sg.wall_group):
                player.rect.x -= v.tick + 7
                moving = False
            for sprite in sg.all_sprites:
                camera.apply(sprite, direction, moving)
        elif key == pygame.K_LEFT:
            direction = 'left'
            if pygame.sprite.spritecollideany(player, sg.wall_group):
                player.rect.x += v.tick + 7
                moving = False
            for sprite in sg.all_sprites:
                camera.apply(sprite, direction, moving)

        else:
            distance_pass = 0
            moving = False
    c.clock.tick(c.fps)
    sg.tiles_group.draw(screen)
    sg.saw_group.draw(screen)
    sg.player_group.draw(screen)
    sg.saw_group.update()
    sg.player_group.update(direction, moving)
    pygame.display.flip()

pygame.quit()
