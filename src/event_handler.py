import pygame
from pygame.locals import *
import node
import menu
import tkinter as tk
from tkinter.filedialog import askopenfile
from os import path

OLD_POS = (0,0)
def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == MOUSEMOTION:

            pos = pygame.mouse.get_pos()
            fast_menu = menu.fast_menu
            if fast_menu.show == 1:
                itemlist = menu.item_list
                if (fast_menu.pos[0]-50 > pos[0]) or (fast_menu.pos[0]+fast_menu.size[0]+50 < pos[0]) or \
                        fast_menu.pos[1]-50 > pos[1] or fast_menu.pos[1]+fast_menu.size[1]+50 < pos[1]:
                    fast_menu.show = 0
                for ind,i in enumerate(itemlist):
                    if i[0]<pos[0]<i[0]+i[2] and i[1]<pos[1]<i[1]+i[3] :
                        menu.fast_menu.focused = ind
                        break
                    menu.fast_menu.focused = -1
                menu.fast_menu.draw()

            menu_item = menu.menu_item
            for ind,i in enumerate(menu_item):
                if i[0]<pos[0]<i[0]+i[2] and i[1]<pos[1]<i[1]+i[3] :
                    menu.menu.focused = ind
                    break
                menu.menu.focused = -1
            menu.menu.draw()

            global OLD_POS
            for i in node.node_list:
                if i.clicked == 1:
                    i.pos=(i.pos[0]+pos[0]-OLD_POS[0],i.pos[1]+pos[1]-OLD_POS[1])


            OLD_POS = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                itemlist = menu.item_list
                pos = pygame.mouse.get_pos()
                if menu.fast_menu.show == 1:
                    for ind, i in enumerate(itemlist):
                        if i[0] < pos[0] < i[0] + i[2] and i[1] < pos[1] < i[1] + i[3]:
                            menu.fast_menu.selected = ind
                            menu.fast_menu.clicked()
                            break
                        menu.fast_menu.selected = -1
                for ind,i in enumerate(reversed(node.node_list)):
                    if i.get_pos()[0]<pos[0]<i.get_pos()[0]+i.get_size()[0] and i.get_pos()[1]<pos[1]<i.get_pos()[1]+i.get_size()[1]:
                        i.click(pos)
                        break


            if event.button == 3:
                fast_menu = menu.fast_menu
                fast_menu.set_pos(pygame.mouse.get_pos())
                if fast_menu.show == 0 :
                    fast_menu.show = 1
                    fast_menu.set_pos(pygame.mouse.get_pos())
                # filenode_temp = node.file_node(pygame.mouse.get_pos())

            if event.button == 2:
                root = tk.Tk()
                root.withdraw()
                fname = askopenfile(initialdir = path.dirname(__file__))
                print(fname)
                print(path.dirname(__file__))

        if event.type == MOUSEBUTTONUP:
            for ind, i in enumerate(node.node_list):
                i.release()

        if event.type == KEYDOWN:
            if event.key == K_x:
                for key,i in enumerate(node.node_list):
                    if i.selected == 1:
                        del node.node_list[key]
                        break

