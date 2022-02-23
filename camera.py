import constants as c
from variables import tick


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
