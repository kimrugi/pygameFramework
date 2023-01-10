import pygame

from Mario import Mario


class Framework:
    def __init__(self, screen_width=480, screen_height=640, caption='SampleGame', framePerSecond=60):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(caption)
        self.fps = pygame.time.Clock()
        self.framePerSecond = framePerSecond
        
        self.objects = []
        self.addObject(Mario())
        pass

    def start(self):

        pass

    def update(self):
        pass

    def draw(self):
        for object in self.objects:
            object.draw(self.screen)
        pygame.display.update()

    def handleEvent(self, event):
        pass

    def addObject(self, object):
        self.objects.append(object)
        pass

    def removeObject(self, object):
        pass