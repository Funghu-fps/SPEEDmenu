from typing import Text
import pygame
from pygame import draw
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
    # full constructor

    def __init__(self,
                 screen: pygame.Surface,
                 pos: tuple[float, float],
                 size: tuple[float, float],
                 font: pygame.font.Font,
                 text: str,
                 text_alingment: tuple[str, str] = ("middle", "middle"),
                 rect_color: tuple[int, int, int] = (0, 0, 0),
                 text_color: tuple[int, int, int] = (255, 255, 255),
                 text_anti_alias: bool = True,
                 draw_rect: bool = True,
                 border_radius: int = 0) -> None:

        self.screen = screen
        self.pos = pos
        self.size = size
        self.font = font
        self.text = text
        self.text_alingment = text_alingment
        self.rect_color = rect_color
        self.text_color = text_color
        self.text_anti_alias = text_anti_alias
        self.draw_rect = draw_rect
        self.border_radius = border_radius
        self.rendered = self.font.render(
            self.text, self.text_anti_alias, self.text_color)
        self.rect = Rect(pos, size)
        self.text_pos_x, self.text_pos_y = 0, 0
        self.text_size: tuple[float, float] = self.font.size(self.text)
        
        self.allingment_text()


        # middle alingment
    def allingment_text(self):
        if self.text_alingment[0] == "middle":
            self.text_pos_x = self.size[0]/2 - \
                self.text_size[0]/2 + self.pos[0]

        if self.text_alingment[1] == "middle":
            self.text_pos_y = self.size[1]/2 - \
                self.text_size[1]/2 + self.pos[1]

    def render(self):
        pygame.draw.rect(self.screen, self.rect_color,
                         self.rect, border_radius=self.border_radius)
        self.screen.blit(self.rendered, (self.text_pos_x, self.text_pos_y))

    def update_text(self, color: tuple[int, int, int], text: str, anti_alias: bool = True):
        self.text = text
        self.text_anti_alias = anti_alias
        self.text_color = color
        self.rendered = self.font.render(
            self.text, self.text_anti_alias, self.text_color)

        self.text_size: tuple[float, float] = self.font.size(self.text)
        self.allingment_text()
