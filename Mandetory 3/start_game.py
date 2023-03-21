import pygame
from main import Game

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.game_loop()