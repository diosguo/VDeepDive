#!/usr/bin/env python

# 指定图像文件名称

import pygame
# 导入pygame库
from pygame.locals import *
# 导入一些常用的函数和常量
from sys import exit



MENU_COLOR = (104,104,104)
MAIN_COLOR = (114,114,114)
BACK_COLOR = (57,57,57)
LINE_DEEP_COLOR = (42,42,42)
LINE_LIGHT_COLOR = (47,47,47)
SCREEN_SIZE = (1280,720)
world_center_pos = [2000-SCREEN_SIZE[0]/2,2000-SCREEN_SIZE[1]/2]
world_scale = 0.5
pygame.init()
# 初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
# 创建了一个窗口
pygame.display.set_caption("Hello, World!")
# 设置窗口标题

background = pygame.Surface((4000,4000))
background.fill(BACK_COLOR)
mouse_cursor = pygame.Surface((20,20))
mouse_cursor.fill((255,255,255))
file_node = pygame.Surface((150,250))
file_node.fill((0,0,0))

# 加载并转换图像

LINE_PADDING = 50

MIDDLE_FLAG = 0
MIDDLE_START_POS = (0,0)
while True:
    # 游戏主循环
    for i in range(80):
        pos_y =  i * 50
        if i % 5 == 0:
            pygame.draw.line(background,LINE_DEEP_COLOR,(0, pos_y),(4000,pos_y))
        else:
            pygame.draw.line(background, LINE_LIGHT_COLOR, (0, pos_y), (4000, pos_y))

    for i in range(80):
        pos_x =  i * 50
        if i % 5 == 0:
            pygame.draw.line(background,LINE_DEEP_COLOR,(pos_x, 0),(pos_x,4000),1)
        else:
            pygame.draw.line(background, LINE_LIGHT_COLOR, (pos_x, 0),(pos_x,4000),1)
    pygame.draw.rect(background,(0,0,0),(2000,2000,100,100))
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 2 :
                MIDDLE_FLAG = 1
                MIDDLE_START_POS = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONUP:
            if event.button == 2:
                MIDDLE_FLAG = 0
        if event.type == MOUSEMOTION:
            if MIDDLE_FLAG == 1:
                if 0<world_center_pos[0] - pygame.mouse.get_pos()[0] + MIDDLE_START_POS[0]< 4000 - SCREEN_SIZE[0] :
                    world_center_pos[0] -= pygame.mouse.get_pos()[0] - MIDDLE_START_POS[0]
                if 0<world_center_pos[1] - pygame.mouse.get_pos()[1] + MIDDLE_START_POS[1]<4000 - SCREEN_SIZE[1]:
                    world_center_pos[1] -= pygame.mouse.get_pos()[1] - MIDDLE_START_POS[1]
                MIDDLE_START_POS = pygame.mouse.get_pos()
        if event.type == KEYDOWN:
            if event.key == K_a:
                mouse_pos = pygame.mouse.get_pos()
                # background.blit(file_node, (2000, 2000))
                file_temp = pygame.Surface.convert(file_node)
                background.blit(file_temp,(mouse_pos[0]+world_center_pos[0],mouse_pos[1]+world_center_pos[1]))


    screen.blit(background, (- world_center_pos[0],- world_center_pos[1]))
    x, y = pygame.mouse.get_pos()
    # 获得鼠标位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    # 把光标画上去

    pygame.display.update()
    # 刷新一下画面