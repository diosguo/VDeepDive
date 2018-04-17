import pygame
import node

pygame.font.init()
MENU_COLOR = (104,104,104)
NAME_LIST = ['file node','relation node','udf node','variable node']
NODE_INDEX = {'file node':node.file_node,'relation node':node.relation_node,'udf node':node.udf_node,'variable node':node.variable_node}
item_list = []
menu_item = []


class TopMenu(pygame.Surface):
    menu_list = ['File','Edit','Build','Help']
    font_height = 0
    focused = -1
    selected = -1
    def __init__(self):
        super().__init__((1280,25))
        self.draw()
        global menu_item
        for i in range(4):
            menu_item.append((5+i*40,1,40,25))
    def draw(self):
        self.fill(MENU_COLOR)
        font = pygame.font.SysFont('arial',16)
        self.font_height = font.get_height()
        top_y = int((25-self.font_height)/2)
        for key,value in enumerate(self.menu_list):
            temp = font.render(value,True,(0,0,0))
            if self.focused == key:
                blue = pygame.Surface((40,23))
                blue.fill((0,0,255))
                blue.set_alpha(90)
                self.blit(blue,(5+key*40,1))
            # pygame.Surface.get
            self.blit(temp,(12+key*40,top_y))


class FastMenu(pygame.Surface):
    show = 0
    pos = ( 0, 0)
    font_height = 0
    focused = -1
    selected = -1
    size = (100,140)
    def __init__(self):
        super().__init__(self.size)
        self.draw()


    def draw(self):
        self.fill((28, 28, 28))
        my_font = pygame.font.SysFont('arial', 16)
        font_height = my_font.get_linesize()
        self.font_height = font_height
        title = my_font.render('New Node', True, (200, 200, 200))
        self.blit(title, (1, 2))
        for index, name in enumerate(NAME_LIST):
            temp = my_font.render(name, True, (255, 255, 255))
            if self.focused == index:
                blue = pygame.Surface((100,self.font_height))
                blue.fill((0,0,255))
                blue.set_alpha(90)
                self.blit(blue,(0,1+index*font_height+30))
            self.blit(temp, (10, 1 + index * font_height + 30))



    def set_pos(self,pos):
        self.pos = pos
        global item_list
        item_list= []
        for i in range(len(NAME_LIST)):
            item_list.append((self.pos[0]+10,self.pos[1]+i*self.font_height+30,100,self.font_height))

    def clicked(self):
        temp = NODE_INDEX[NAME_LIST[self.selected]](self.pos)
        self.show = 0



menu = TopMenu()
fast_menu = FastMenu()