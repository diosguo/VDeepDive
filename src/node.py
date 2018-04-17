import pygame

MENU_COLOR = (104,104,104)
MAIN_COLOR = (114,114,114)
BACK_COLOR = (57,57,57)
LINE_DEEP_COLOR = (42,42,42)
LINE_LIGHT_COLOR = (47,47,47)

node_list = []

class Node(pygame.Surface):
    mouse_down = 0
    name = ''
    selected = 1
    pos = ()
    size = (150,250)
    clicked = 0

    def set_pos(self,pos:tuple):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def get_size(self):
        return self.size

    def click(self,pos):
        global node_list
        for i in node_list:
            i.selected = 0
        self.selected = 1
        loc = (pos[0]-self.pos[0],pos[1]-self.pos[1])
        self.clicked = 1


        i = node_list.index(self)
        del node_list[i]
        node_list.append(self)

    def release(self):
        self.clicked = 0

    def draw(self):
        if self.selected == 1:
            self.fill((217, 190, 5))
        else:
            self.fill((0,0,0))
        self.set_pos(self.pos)
        pygame.draw.rect(self, (90, 90, 90), (1, 1, 148, 248))
        pygame.draw.rect(self, (77, 77, 77), (1, 1, 148, 20))
        my_font = pygame.font.SysFont('arial', 16)
        text_surface = my_font.render(self.name, True, (0, 0, 0))
        self.blit(text_surface, (10, 0))

class variable_node(Node):

    def __init__(self,pos):
        super().__init__((150,250))
        self.name = 'Variable'
        self.pos = pos
        self.draw()
        for node in node_list:
            node.selected = 0
        node_list.append(self)

class file_node(Node):
    def __init__(self,pos):
        super().__init__((150,250))
        self.name = 'File'
        self.pos = pos
        self.draw()
        for node in node_list:
            node.selected = 0
        node_list.append(self)


class relation_node(Node):
    def __init__(self,pos):
        super().__init__((150,250))
        self.name = 'Relation'
        self.pos = pos
        self.draw()
        for node in node_list:
            node.selected = 0
        node_list.append(self)

class udf_node(Node):
    def __init__(self,pos):
        super().__init__((150,250))
        self.name = 'UDF'
        self.pos = pos
        self.draw()
        for node in node_list:
            node.selected = 0
        node_list.append(self)
