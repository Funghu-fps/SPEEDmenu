#classic pygma stuff
import pygame
from menu import * #import
(width, height) = (700, 700)#window size
running = True
pygame.init()

#setting display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME")


font1 = pygame.font.SysFont("Arial",25)#pygame font object must be created to use in single/menu objects





#creating menus object 
menus = menus()

#adding menu to menus object. screen is pygame.surface
#menus.addMenu("keyword", menu object)
menus.addMenu("Test",  menu(screen, (0,0), font1, (255,255,255), (2,3), (10,10), "elma yes","elma yes","elma no","elma","elma","elma", background = True,  backcolor = (255,0,0), size = (100,50), width = 0, backgroundcolor = (0,255,0),   textAling_x = "middle",textAling_y = "middle"))
#another one
menus.addMenu("menu", menu(screen, (300,0), font1, (255,255,255), (1,3), (10,10), "continue", "New Game", "Test", background = True, backcolor = (0,255,0),  size = (100,50), width = 0, backgroundcolor = (255,0,0),  textAling_x = "middle",textAling_y = "middle"))
#setting active menu                    
menus.activeMenu = menus.menus["menu"]


def main():
    global running, screen, colors, showmenu, ev
    screen.fill((255,0,0))
    clock = pygame.time.Clock()
    showmenu = True

    while running:
        clock.tick(60)
        ev = pygame.event.get()
        pygame.event.pump()
        
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #1== leftclick 2== middle click 3== right click 4== scroll
                #forward 5== scroll back
                if event.button == 1:
                    checkhitmenu()

            if event.type == pygame.QUIT:
               running = False
               break

        if showmenu == True:
            #filling  screen
            screen.fill(menus.activeMenu.backgroundcolor)
            showmenu = False
            menus.activeMenu.render()#rendering menu

        pygame.display.flip()#bu satır tüm ekranı yeniliyor
#clicking on menus
def get_MousePos():
    pos = pygame.mouse.get_pos()
    return (pos)
def checkhitmenu():
    global  showmenu, ev
    posx,posy = get_MousePos()
    a = 0
    #if clicked on menu element
    for i in menus.activeMenu.menu_rects:
        if posx >= i.left and posx <= i.right and posy >= i.top and posy <= i.bottom :
            print(menus.activeMenu.menu_elements[a].msg)
            msg = menus.activeMenu.menu_elements[a].msg
#___________game______________________________________________________________________________________________________________________________________________________________________________________
            try:        
                #if menus contains a menu named "msg"  the "msg" menu will become active menu
                #similar things can be used to start events
                    skrrt = menus.menus.get(msg)
                    showmenu = True
                    if skrrt:
                        menus.activeMenu = skrrt


            except :
                pass
        a+=1
        pass
if __name__ == '__main__':
   main()
