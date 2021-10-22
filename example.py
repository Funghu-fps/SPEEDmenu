import pygame

from SPEEDmenu import * 

(width, height) = (700, 700)
running = True
pygame.init()

#setting display
screen = pygame.display.set_mode((width, height))
print(type(screen))
pygame.display.set_caption("GAME")


font1 = pygame.font.SysFont("Arial",25)
print(type(font1))

<<<<<<< Updated upstream
element = MenuElement(screen, (20,30), (60,50),font1, "DENEME",rect_color=(0,255,255), text_color=(0,0,0))
=======
menu1 = menu(screen,(10,10),(100,60),(20,10),font1,(9,1),"1","2","3","4","5","6","7","8","9",)
menu2 = menu()


>>>>>>> Stashed changes
#element.update_text((255,255,255), "asdk")
def main():
    running = True
    screen.fill((255,0,0))
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        ev = pygame.event.get()
        pygame.event.pump()
        
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #1== leftclick 2== middle click 3== right click 4== scroll
                #forward 5== scroll back
                if event.button == 1:
                    pass

            if event.type == pygame.QUIT:
               running = False
               break

        pygame.display.flip()
<<<<<<< Updated upstream
        element.render()
=======
        menu1.render()
>>>>>>> Stashed changes
def get_MousePos():
    pos = pygame.mouse.get_pos()
    return (pos)


if __name__ == '__main__':
   main()
