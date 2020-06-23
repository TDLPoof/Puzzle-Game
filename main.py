'''
Created on Jun 23, 2020

Based on tutorial at https://www.youtube.com/watch?v=6oVZ-VBaC2E

@author: Neil
'''
import pygame
import config
from game_state import GameState
from game import Game

def main(width = 500, height = 500, frameRate = 50):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Puzzle Game")
    game = Game(screen)
    game.set_up()
    
    clock = pygame.time.Clock()
    #main loop
    while game.game_state == GameState.RUNNING:
        clock.tick(frameRate)
        game.update()
        pygame.display.flip()

main()