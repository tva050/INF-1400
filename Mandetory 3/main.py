import pygame

from config import Config



class Game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        Config.screen.blit(Config.background, (0, 0))
        pygame.display.update()
        


if __name__ == "__main__":
    pygame.init()
    br = Game()
    
    