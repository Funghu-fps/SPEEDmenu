import pygame
import unittest
from pygame import image

from SPEEDmenu import *

(width, height) = (700, 700)
running = True
pygame.init()

# setting display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME")


font1 = pygame.font.SysFont("Arial", 25)
a = pygame.image.load("button.png")
rect_color = (255,0,0)
text_color = (0,0,0)
menu1 = menu(screen, (30, 30), (100, 60), (10, 10), font1, (2, 2), "1", "2", "3", "4", image=a)
element1 = MenuElement(screen, (0, 0), (100, 60), font1, "test",rect_color=rect_color,text_color=text_color)


class test_element(unittest.TestCase):
    def test_rect_color(self):
        self.assertEqual(rect_color,(0,0,0))
    def test_text_color(self):
        self.assertEqual(text_color, element1.text_color)  


if __name__ == '__main__':
    unittest.main()
