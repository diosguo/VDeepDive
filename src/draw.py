import node
import menu
import pygame
from pygame.locals import *
def draw(screen):
    backgroung = pygame.Surface((1280, 720), 0, 32)
    backgroung.fill((57, 57, 57))
    screen.blit(backgroung,(0,0))
    for node_t in node.node_list:
        node_t.draw()
        screen.blit(node_t,node_t.get_pos())

    screen.blit(menu.menu,(0,0))
    menu.fast_menu.set_alpha(95)
    if menu.fast_menu.show == 1:
        screen.blit(menu.fast_menu,menu.fast_menu.pos)

    pygame.display.update()