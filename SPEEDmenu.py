from typing import Text
import pygame
from pygame import draw
from pygame.constants import GL_RED_SIZE
from pygame.draw import rect
from pygame.rect import Rect
# use RGB only!
# text alling_x has left ,right and middle as options
# text alling_y has up, down and middle
# middle is default for both


class MenuElement:
    """
    MenuElement class creates Menu elements U can only use RGB values
    pos(x,y) represents the left top corner of the rectangle
    use updeate_text method for changing text after defining the object
    """

    def __init__(self,
                 screen: pygame.Surface,
                 pos: tuple[float, float],
                 size: tuple[float, float],
                 font: pygame.font.Font,
                 text: str,
                 text_alignment: tuple[str, str] = ("middle", "middle"),
                 rect_color: tuple[int, int, int] = (0, 0, 0),
                 text_color: tuple[int, int, int] = (255, 255, 255),
                 text_anti_alias: bool = True,
                 draw_rect: bool = True,
                 image: pygame.rect.Rect = None,
                 border_radius: int = 0) -> None:

        self.screen = screen
        self.pos = pos
        self.size = size
        self.font = font
        self.text = text
        self.text_alignment = text_alignment
        self.rect_color = rect_color
        self.text_color = text_color
        self.text_anti_alias = text_anti_alias
        self.draw_rect = draw_rect
        #self.image = image
        self.border_radius = border_radius
        self.rendered = self.font.render(
            self.text, self.text_anti_alias, self.text_color)

        if image == None:
            self.rect = Rect(self.pos, self.size)
            self.image = False
        else:
            self.rect = image
            self.image = True

        self.text_pos_x, self.text_pos_y = 0, 0
        self.text_size: tuple[float, float] = self.font.size(self.text)

        self.alignment_text()

        # middle alignment will come back to add more

        # middle alignment

    def alignment_text(self):
        # rows
        if self.text_alignment[0] == "middle":
            self.text_pos_x = self.size[0]/2 - \
                self.text_size[0]/2 + self.pos[0]
        elif self.text_alignment[0] == "right":
            self.text_pos_x += (self.size[0]-self.text_size[0]) + self.pos[0]
        else:
            self.text_pos_x = self.pos[0]
        # collums
        if self.text_alignment[1] == "middle":
            self.text_pos_y = self.size[1]/2 - \
                self.text_size[1]/2 + self.pos[1]
        elif self.text_alignment[1] == "down":
            self.text_pos_y += (self.size[1] - self.text_size[1]) + self.pos[1]
        else:
            self.text_pos_y = self.pos[1]

    def render(self):
        if self.draw_rect:
            if self.image:
                self.screen.blit(self.rect, self.pos)
            else:
                pygame.draw.rect(self.screen, self.rect_color,
                                self.rect, border_radius=self.border_radius)

        self.screen.blit(self.rendered, (self.text_pos_x, self.text_pos_y))

    def update_text(self, color: tuple[int, int, int], text: str, anti_alias: bool = True):
        self.text = text
        self.text_anti_alias = anti_alias
        self.text_color = color
        self.rendered = self.font.render(
            self.text, self.text_anti_alias, self.text_color)

        self.text_size = self.font.size(self.text)
        self.alignment_text()


class menu:
    """
    Menu class creates Menu.  You can only use RGB values
    pos(x,y) the left top corner of the menu
    use updeate_text method for changing text after defining the object
    """
    def __init__(self,
                 screen: pygame.Surface,
                 pos:    tuple[float, float],
                 size:   tuple[float, float],
                 margin: tuple[float, float],
                 font:   pygame.font.Font,
                 grid:   tuple[int, int],
                 * text: str,
                 text_alignment: tuple[str, str] = ("middle", "middle"),
                 rect_color:     tuple[int, int, int] = (0, 0, 0),
                 text_color:     tuple[int, int, int] = (255, 255, 255),
                 text_anti_alias: bool = True,
                 draw_rect:      bool = True,
                 image:          pygame.rect.Rect = None,
                 border_radius:  int = 0) -> None:

        self.screen = screen
        self.pos =    pos
        self.size =   size
        self.margin = margin
        self.font =   font
        self.grid =   grid
        self.text =   text
        self.text_alignment = text_alignment
        self.rect_color =     rect_color
        self.text_color =     text_color
        self.text_anti_alias = text_anti_alias
        self.draw_rect =      draw_rect
        self.image =          image
        self.border_radius =  border_radius
        self.elements =       []        

        self.element_pos_x, self.element_pos_y = self.pos
        self.a = 0
        for y in range(grid[1]):
            for x in range(grid[0]):
                self.elements.append(MenuElement(self.screen,
                                                 (self.element_pos_x,
                                                  self.element_pos_y),
                                                 self.size, self.font,
                                                 text[self.a],
                                                 self.text_alignment,
                                                 self.rect_color, self.text_color,
                                                 self.text_anti_alias, self.draw_rect,
                                                 self.image,
                                                 self.border_radius))
                self.a += 1
                self.element_pos_x += self.size[0] + self.margin[0]
            self. element_pos_x = self.pos[0]
            self.element_pos_y += self.size[1] + self.margin[1]
    def auto_menu(self):
       pass 
   
    def render(self):
        for i in self.elements:
            i.render()


