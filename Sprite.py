import pygame.image

from Object import Object


class Sprite (Object):
    def __init__(self, x, y, w, h, imageDir=None):
        super().__init__()
        if imageDir is not None:
            self.image = pygame.image.load(imageDir)
            self.image = pygame.transform.scale(self.image, (w, h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def update(self, time):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def getRect(self):
        result = pygame.Rect()
        result.x = self.x
        result.y = self.y
        result.w = self.w
        result.h = self.h
        return result

