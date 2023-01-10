import pygame.image

from Sprite import Sprite


class SpriteAnimation(Sprite):
    def __init__(self, x, y, w, h, imageDirList, framesPerSecond):
        super().__init__(x, y, w, h)
        self.images = []
        for dir in imageDirList:
            self.images.append(pygame.image.load(dir))

        self.frameCount = len(self.images)

        self.framesPerSecond = framesPerSecond
        self.frameTime = 0.0

    def update(self, time):
        super().update(time)
        self.frameTime += time * self.framesPerSecond
        if(self.frameTime > self.frameCount):
            self.frameTime -= self.frameCount

    def draw(self, screen):
        frameIndex = self.frameTime
        screen.blit(self.images[int(self.frameTime)], (self.x, self.y))
