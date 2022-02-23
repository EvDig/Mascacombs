import pygame
import constants as c
from load_image import load_image
from terminate import terminate
import variables as v
import sprite_groups as sg
from game_cycle import game_start


pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)


def start_screen():
    # intro_text = ["Для движения:", "нажимайте на стрелочки",
    #              "Нажмите ЛКМ чтобы продолжить"]

    image = pygame.transform.scale(load_image('start_screen.png'), (c.width, 259))
    screen.blit(image, (0, 0))
    # font = pygame.font.Font(None, 30)
    # text_coord = 100
    # for line in intro_text:
    # string_rendered = font.render(line, True, pygame.Color('yellow'))
    # intro_rect = string_rendered.get_rect()
    # text_coord += 30
    # intro_rect.top = text_coord
    # intro_rect.x = 30
    # text_coord += intro_rect.height
    # screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        c.clock.tick(c.fps)


def exit_screen():
    image = pygame.transform.scale(load_image('exit_screen.png'), (c.width, 400))
    screen.blit(image, (0, 0))
    exit_button_rect_coordinates = [140, 180, 260, 250]  # x1, y1, x2, y2 кнопки "Да"
    cancel_button_rect_coordinates = [170, 320, 240, 370]  # x1, y1, x2, y2 кнопки "Нет"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect_coordinates[0] <= event.pos[0] <= exit_button_rect_coordinates[2] and \
                        exit_button_rect_coordinates[1] <= event.pos[1] <= exit_button_rect_coordinates[3]:
                    terminate()
                elif cancel_button_rect_coordinates[0] <= event.pos[0] <= cancel_button_rect_coordinates[2] \
                        and \
                        cancel_button_rect_coordinates[1] <= event.pos[1] <= cancel_button_rect_coordinates[3]:
                    return
        pygame.display.flip()
        c.clock.tick(c.fps)


def level_choose_screen():
    image = pygame.transform.scale(load_image('choose_level.png'), (c.width, 389))
    screen.blit(image, (0, 0))
    one_button_rect_coordinates = [75, 215, 150, 370]  # x1, y1, x2, y2 кнопки "1"
    two_button_rect_coordinates = [245, 215, 320, 370]  # x1, y1, x2, y2 кнопки "2"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if one_button_rect_coordinates[0] <= event.pos[0] <= one_button_rect_coordinates[2] and \
                        one_button_rect_coordinates[1] <= event.pos[1] <= one_button_rect_coordinates[3]:
                    return 'level1.txt'
                elif two_button_rect_coordinates[0] <= event.pos[0] <= two_button_rect_coordinates[2] \
                        and \
                        two_button_rect_coordinates[1] <= event.pos[1] <= two_button_rect_coordinates[3]:
                    return 'level2.txt'
        pygame.display.flip()
        c.clock.tick(c.fps)


def level_complete_screen():
    image = pygame.transform.scale(load_image('level_completed.png'), (c.width, 382))
    screen.blit(image, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                game_start()
        pygame.display.flip()
        c.clock.tick(c.fps)


def death_screen(direction):
    image = pygame.transform.scale(load_image('death_screen.png'), (c.width, 200))
    screen.blit(image, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for sprite in sg.all_sprites:
                    v.camera.revival_position(sprite, direction)
                return
        pygame.display.flip()
        c.clock.tick(c.fps)
