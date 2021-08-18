# Menu
## Creating menus never been so easy and fast
this module can create simple menus in a second.

exaple images
-------

![example](https://preview.redd.it/wnvm141qt3i71.png?width=374&format=png&auto=webp&s=7befe3a7e376fa8306ef87cf446188c0cb84b110)


![example](https://preview.redd.it/i13adtutt3i71.png?width=703&format=png&auto=webp&s=e8a715bd815a00c453d4246fe88afbf015830dc5)

# 1 start
> get the menu.py file and  put it in the same folder as your project then use code down bellow to import it.
```py
    from menu import*
```
## 1.1 what is single?
>"Single" objects are used to create menu elements meaning each menu element is a "single object"

## 1.2 How to define a single object ?
>pos is the position of object (left top corner) and must be a tuple (x,y)\
>font is pygame font object (will be rendered on single object[menu element])\
>color is rgb color in tuple (r,g,b) \
>msg is string \
>if background is true  a box will willbe drawn behind text.\
background color is rgb color (r,g,b) \
textalling_x has 3 options "left","right","middle"\
textalling_y has 3 optins "top","down","middle"



```py
single(screen, pos: tuple, font, color: tuple, msg: str, background: bool = False, backcolor: tuple = (0, 0, 0), size: tuple = (30, 30), width: int = 0, textAling_x: str = "middle", textAling_y: str = "middle") //height comingsoon
```
to render a single object use the render method
```py
single.render()
```

# Menu object
## menu object creates menus using single objets 
```py
(self, screen, pos: tuple, font, color: tuple, collumNline: tuple, gap: int, *msg: str, background=False, backcolor: tuple = (0, 0, 0), size=(30, 30), width=0, backgroundcolor=(255, 0, 0), textAling_x="middle", textAling_y="middle")
```
>collumNline is an int tuple (number of collums , number of lines)\
Background color is rendered seperetly with pygame.fill()method

# Menus object
## manage menus with ease 
```py
menus = menus()
menus.addMenu("keyword",menu object)
```
# Example
>first create a pygame display then a pygame font
```py
...
#create menus
pos = (30, 50)
menus =menus()
#add menu to menus screen = pygame.surface 
#font = pygame.font
menus.addMenu("menu", menu(screen, (300,100), font1, (255,255,255), (1,3), (10,10), "continue", "New Game", "Test", background = True, backcolor = (0,255,0),  size = (150,50), width = 0, backgroundcolor = (255,0,0),  textAling_x = "middle",textAling_y = "middle"))

menus.activeMenu = menus.menus["menu"]

menus.activeMenu.render()

...

```


