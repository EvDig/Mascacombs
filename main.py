import os
import sys

import pygame

pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data/sprites', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


FPS = 50
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    # intro_text = ["Для движения:", "нажимайте на стрелочки",
    #              "Нажмите ЛКМ чтобы продолжить"]

    image = pygame.transform.scale(load_image('start_screen.png'), (width, 259))
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
        clock.tick(FPS)


def exit_screen():
    image = pygame.transform.scale(load_image('exit_screen.png'), (width, 400))
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
        clock.tick(FPS)


def death_screen():
    image = pygame.transform.scale(load_image('death_screen.png'), (width, 179))
    screen.blit(image, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/txt/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


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

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
saw_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        if tile_type == 'wall':
            self.add(wall_group)
        if tile_type == 'saw':
            self.add(saw_group)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group)
        self.speed = 900
        self.image = player_image
        self.moving_image = player_moving_image
        self.on_right_wall = player_on_right_wall
        self.on_left_wall = player_on_left_wall
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
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


start_screen()
camera = Camera()
player, level_x, level_y = generate_level(load_level('level1.txt'))
key = ''
fps = 144
tick = round(player.speed / fps)
direction = ''
moving = False
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            exit_screen()
        if event.type == pygame.KEYDOWN and not moving:
            key = event.key
            moving = True

    if moving:
        if pygame.sprite.spritecollideany(player, saw_group):
            death_screen()
        if key == pygame.K_UP:
            # player.rect.y -= tick
            direction = 'up'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.y += tick - 1
                moving = False
            for sprite in all_sprites:
                camera.apply(sprite, direction, moving)
        elif key == pygame.K_DOWN:
            # player.rect.y += tick
            direction = 'down'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.y -= tick - 5
                moving = False
            for sprite in all_sprites:
                camera.apply(sprite, direction, moving)
        elif key == pygame.K_RIGHT:
            # player.rect.x += tick
            direction = 'right'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.x -= tick + 7
                moving = False
            for sprite in all_sprites:
                camera.apply(sprite, direction, moving)
        elif key == pygame.K_LEFT:
            # player.rect.x -= tick
            direction = 'left'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.x += tick + 7
                moving = False
            for sprite in all_sprites:
                camera.apply(sprite, direction, moving)

        else:
            moving = False
    clock.tick(fps)
    tiles_group.draw(screen)
    player_group.draw(screen)
    player_group.update(direction, moving)
    pygame.display.flip()

pygame.quit()
