#--------------------------------------------------------
#Project Name: CMSI 2048
#Description: 2048 game
#Authors: Devan Joaquin Abiva, Nathan Mayeda, Simon Worku
#Date: 12/12/2023
#--------------------------------------------------------
from game import *
import pygame
pygame.init()
pygame.font.init()

#image taken from flaticon.com
icon = pygame.image.load("menu.png") #changes icon in window
pygame.display.set_icon(icon)

main = App2048()
main.mainMenu()