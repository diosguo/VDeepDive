#!/usr/bin/env python

# 指定图像文件名称

import pygame
import draw
from pygame.locals import *
from sys import exit
import node
import event_handler

def run(screen:pygame.Surface):
    while True:
        event_handler.event_handler()
        draw.draw(screen)



def main():
    pygame.init()
    pygame.font.init()
    main_screen = pygame.display.set_mode((1280,720),0,32)
    backgroung = pygame.Surface((1280,720),0,32)
    backgroung.fill((57,57,57))
    main_screen.blit(backgroung,(0,0))
    pygame.display.set_caption("VDeepDive v0.01")
    run(main_screen)


if __name__ == '__main__':
    main()