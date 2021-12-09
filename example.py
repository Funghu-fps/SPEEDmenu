import pygame
from pygame import image

from SPEEDmenu import *

(width, height) = (700, 700)
running = True
pygame.init()

# setting display
screen = pygame.display.set_mode((width, height))
print(type(screen))
pygame.display.set_caption("GAME")


font1 = pygame.font.SysFont("Arial", 25)
print(type(font1))

a = pygame.image.load("button.png")

menu1 = menu(screen,(30,30),(100,60),(10,10),font1,(2,2),"1","2","3","4")

# element1 = MenuElement(screen, (300, 300), (100, 60),
#                        font1, "31", text_alignment=("a", "bp"),image=a)
#auto menu aligns the menu 
menu1.auto_menu(["left","top"])

#element.update_text((255,255,255), "asdk")
def main():
    running = True
    screen.fill((255, 255, 0))
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        ev = pygame.event.get()
        pygame.event.pump()

        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1== leftclick 2== middle click 3== right click 4== scroll
                # forward 5== scroll back
                if event.button == 1:
                    pass

            if event.type == pygame.QUIT:
                running = False
                break

        pygame.display.flip()
        #rendering menus and elements each loop is ineficent
        menu1.render()
        # element1.render()


def get_MousePos():
    pos = pygame.mouse.get_pos()
    return (pos)


if __name__ == '__main__':
    main()
