import pygame
from pygame.font import Font

size = 120

colors = {
    0: (119, 110, 101),
    1: (249, 246, 242)
}

class Tile:
    def __init__(self, surface, coordinates, color, value): #initializes the coordinates and values of a new tile
        self.surface = surface
        self.row = coordinates[0] + 202
        self.column = coordinates[1] + 114
        self.color = color
        self.value = value
        self.fontColor = None

    def drawTile(self): #draws a new tile onto the screen
        if int(self.value) > 4:
            self.fontColor = colors.get(1)
        else:
            self.fontColor = colors.get(0)

        self.font = pygame.font.SysFont('comicsansms', 55).render(self.value, True, self.fontColor)
        self.rect = pygame.Rect(self.column, self.row, 121, 121)
        rectangle = pygame.draw.rect(self.surface, self.color, self.rect)
        center = self.font.get_rect(center = rectangle.center)
        self.surface.blit(self.font, center)

    def setTileValue(self, value): #updates the value of the tile
        self.value = value

    def getTileValue(self): #returns value
        return self.value