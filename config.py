'''
Created on Jun 23, 2020

@author: Neil
'''
import pygame

BLACK = (8, 8, 16)
GREEN = (0, 160, 0)
WHITE = (255, 255, 255)

SCALE = 32

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

map_tile_image = {
    "S" : pygame.transform.scale(pygame.image.load("sprites/Sand.png"), (SCALE, SCALE)),
    "W": pygame.transform.scale(pygame.image.load("sprites/Wall.png"), (SCALE, SCALE)),
    "B": pygame.transform.scale(pygame.image.load("sprites/Black Tile.png"), (SCALE, SCALE)),
    "X": pygame.transform.scale(pygame.image.load("sprites/White Tile.png"), (SCALE, SCALE)),
    "D": pygame.transform.scale(pygame.image.load("sprites/Door.png"), (SCALE, SCALE)),
    "I": pygame.transform.scale(pygame.image.load("sprites/Ice.png"), (SCALE, SCALE)),
    "J": pygame.transform.scale(pygame.image.load("sprites/Jump Tile.png"), (SCALE, SCALE)),
    "E": pygame.transform.scale(pygame.image.load("sprites/Exit.png"), (SCALE, SCALE)), 
    "C": pygame.transform.scale(pygame.image.load("sprites/Cracked Tile.png"), (SCALE, SCALE)),
    "H": pygame.transform.scale(pygame.image.load("sprites/Hole.png"), (SCALE, SCALE)),
    "_": pygame.transform.scale(pygame.image.load("sprites/Black.png"), (SCALE, SCALE)),
}
