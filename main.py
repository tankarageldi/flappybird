import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import pygame
from sys import exit
import config
import components
import population 
 
pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

def genereate_pipes():
    config.pipes.append(components.Pipes(config.win_width))
def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    pipes_spawn_time = 10

    while True:
        quit_game()

        config.window.fill((0,0,0))

        # draw the ground 
        config.ground.draw(config.window)

        # spawn pipes

        if pipes_spawn_time <= 0:
            genereate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()

            if p.off_screen:
                config.pipes.remove(p)
        
        if not population.extinct():
            population.update_live_players()
        else:
            config.pipes.clear()
            population.natural_selection()
        clock.tick(60)
        pygame.display.flip()

main()