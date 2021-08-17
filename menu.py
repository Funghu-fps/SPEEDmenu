import pygame
#use RGB only! 
#text alling_x has left ,right and middle as options
#text alling_y has up, down and middle
#middle is default for both

#after crating a "single" object u can use single.render() to render it on the screen
class single:       #screen is pygame.surface class                                                                               with,height                            
    def __init__(self, screen, pos: tuple, font, color: tuple, msg: str, background: bool = False, backcolor: tuple = (0, 0, 0), size: tuple = (30, 30), width: int = 0, textAling_x: str = "middle", textAling_y: str = "middle"):
        # variables            position is (x,y)
        self.screen = screen
        self.pos = pos
        self.font = font
        self.color = color
        self.msg = msg
        self.background = background
        self.backcolor = backcolor
        self.size = size
        self.width = width
        self.textAling_x = textAling_x
        self.textAling_y = textAling_y

        self.text = 0
        self.text_x = 0
        self.text_y = 0

        # Middle
        if self.textAling_x == "middle":
            self.text = self.font.render(self.msg, True, self.color)
            self.text_x = self.size[0]/2 - \
                self.text.get_width()/2 + self.pos[0]
        if self.textAling_y == "middle":
            self.text = self.font.render(self.msg, True, self.color)
            self.text_y = self.size[1]/2 - \
                self.text.get_height()/2 + self.pos[1]

        # none
        if self.textAling_x == "none" or self.textAling_x == "left":
            self.text = self.font.render(self.msg, True, self.color)
            self.text_x = self.pos[0]
        if self.textAling_y == "none" or self.textAling_y == "up":
            self.text = self.font.render(self.msg, True, self.color)
            self.text_y = self.pos[1]

        if self.textAling_x == "right":
            self.text = self.font.render(self.msg, True, self.color)
            self.text_x = (self.size[0]-self.text.get_width())+self.pos[0]
        if self.textAling_y == "down":
            self.text = self.font.render(self.msg, True, self.color)
            self.text_y = (self.size[1]-self.text.get_height())+self.pos[1]

    # render
    #rendering both text and box
    def render(self):
        if self.background:
            pygame.draw.rect(self.screen, self.backcolor,
                             (self.pos, self.size), self.width)
            self.screen.blit(self.text, (self.text_x, self.text_y))
            

        # just text
        else:
            self.screen.blit(self.text, (self.text_x, self.text_y))
            

#menu class 

#menu using singles creates a menu and singles are stored in a list and u can change or edit them when ever u want
#use menu.render() to render
class menu:             #screen is pygame.surface class
    def __init__(self, screen, pos: tuple, font, color: tuple, collumNline: tuple, gap: int, *msg: str, background=False, backcolor: tuple = (0, 0, 0), size=(30, 30), width=0, backgroundcolor=(255, 0, 0), textAling_x="middle", textAling_y="middle"):
        # variables
        self.menu_elements = []#singles here :)
        self.menu_rects = []#pygame rect objects
        self.gapx,  self.gapy = gap
        self.posx,  self.posy = pos
        self.sizex,  self.sizey = size
        self.collum,  self.line = collumNline
        self.a = 0

        self.screen = screen
        self.pos = pos
        self.font = font
        self.color = color
        self.msg = msg
        self.background = background
        self.backcolor = backcolor
        self.size = size
        self.width = width
        self.backgroundcolor = backgroundcolor
        self.textAling_x = textAling_x
        self.textAling_y = textAling_y
        for x in range(self.line):
            for i in range(self.collum):
                menu_element = single(self.screen, (self.posx, self.posy),  self.font,  self.color,self.msg[i + self.a],  self.background,  self.backcolor,  self.size,  self.width, self.textAling_x, self.textAling_y)
                self.menu_elements.append(menu_element)
                self.menu_rects.append(pygame.Rect(
                    (self.posx, self.posy), self.size))

                self.posx = self.posx + self.gapx + self.sizex
            if self.collum != 1:
                self.a += 2
            else:
                self.a += 1
            self.posx = self.pos[0]
            self.posy = self.posy + self.sizey + self.gapy

    def render(self):

        for i in self.menu_elements:
            i.render()
        pass

# menus class can be used to manage multiple menu
#menus are kept in a dict so ucan edit them as well
#create menus object then use addmenu(keyword,menuobject) method to creare and add menus to menus.menus dict
#you can render menus by menus.render(key)
class menus(object):
    def __init__(self):
        self.menus = {

        }
        self.activeMenu = []

    def addMenu(self, name: str, menu: menu):
        self.menus[name] = menu
        pass

    def render(self, key: str):
        self.menus[key].render()
