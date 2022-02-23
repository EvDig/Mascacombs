import pygame
import constants as c
from load_image import load_image
from terminate import terminate
import sprite_groups as sg


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
    exit_button_rect_coordinates = [160, 170, 240, 240]  # x1, y1, x2, y2 кнопки "Да"
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


def death_screen(direction):
    image = pygame.transform.scale(load_image('death_screen.png'), (c.width, 200))
    screen.blit(image, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for sprite in sg.all_sprites:
                    camera.revival_position(sprite, direction)
                return
        pygame.display.flip()
        c.clock.tick(c.fps)