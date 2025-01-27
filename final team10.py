import random
import time
import pygame                    # Importing libraries
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)           # >>>>>>>>>>>>>>>>>>>Defining variables<<<<<<<<<<<<<<<<<
GREEN = (0, 255, 0)
BLUE = (0, 71, 171)
RED = (255, 69, 0)
x = 0
y = 0
z = [x, y]
blx = [137, 203, 269, 335, 401]
bly = [137, 203, 269, 335, 401]
bl_mouse = [137, 203, 269, 335, 401, 71, 467]
random_catx = random.choice(blx)
random_caty = random.choice(blx)
random_catv = (random_catx, random_caty)
random_mousex = random.choice(blx)
random_mousey = random.choice(blx)
mouse_posx = random.choice(blx)
mouse_posy = random.choice(blx)
current_pos = (mouse_posx, mouse_posy)
Screen = pygame.display.set_mode([650, 650])
win = pygame.display
win.set_caption('My Window')
surface = win.set_mode(z)
mouse = pygame.image.load("mouse.png").convert_alpha()
mouse = pygame.transform.scale(mouse, (60, 60))
cat = pygame.image.load("cat.png").convert_alpha()
cat = pygame.transform.scale(cat, (60, 60))
LEFT_presses = 0
right_presses = 0
UP_presses = 0
DOWN_presses = 0
WIDTH = 66
HEIGHT = 66
MARGIN = 1
grid = []
seif = [[66, 0], [-66, 0], [0, -66], [0, 66]]
way = random.randint(0, 1)                             # >>>>>>>>>>>><<<<<<<<<<<<

for row in range(10):                           # Drawing grid
    grid.append([])
    for column in range(10):
        grid[row].append(0)
grid[1][5] = 1

pygame.init()                        # Initializing

WINDOW_SIZE = [600, 600]                        # Window setting
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mouse Escape")
done = False
window = True
clock = pygame.time.Clock()import random
import time
import pygame                    # Importing libraries
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)           # >>>>>>>>>>>>>>>>>>>Defining variables<<<<<<<<<<<<<<<<<
GREEN = (0, 255, 0)
BLUE = (0, 71, 171)
RED = (255, 69, 0)
x = 0
y = 0
z = [x, y]
blx = [137, 203, 269, 335, 401]
bly = [137, 203, 269, 335, 401]
bl_mouse = [137, 203, 269, 335, 401, 71, 467]
random_catx = random.choice(blx)
random_caty = random.choice(blx)
random_catv = (random_catx, random_caty)
random_mousex = random.choice(blx)
random_mousey = random.choice(blx)
mouse_posx = random.choice(blx)
mouse_posy = random.choice(blx)
current_pos = (mouse_posx, mouse_posy)
Screen = pygame.display.set_mode([650, 650])
win = pygame.display
win.set_caption('My Window')
surface = win.set_mode(z)
mouse = pygame.image.load("mouse.png").convert_alpha()
mouse = pygame.transform.scale(mouse, (60, 60))
cat = pygame.image.load("cat.png").convert_alpha()
cat = pygame.transform.scale(cat, (60, 60))
LEFT_presses = 0
right_presses = 0
UP_presses = 0
DOWN_presses = 0
WIDTH = 66
HEIGHT = 66
MARGIN = 1
grid = []
seif = [[66, 0], [-66, 0], [0, -66], [0, 66]]
way = random.randint(0, 1)                             # >>>>>>>>>>>><<<<<<<<<<<<

for row in range(10):                           # Drawing grid
    grid.append([])
    for column in range(10):
        grid[row].append(0)
grid[1][5] = 1

pygame.init()                        # Initializing

WINDOW_SIZE = [600, 600]                        # Window setting
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mouse Escape")
done = False
window = True
clock = pygame.time.Clock()
def text_objects(text, font):      # Font and size function
    textsurface = font.render(text, True, RED)
    return textsurface, textsurface.get_rect()


def message_display(text):         # Message function
    largetext = pygame.font.Font('freesansbold.ttf', 50)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((600 / 2), (600 / 2))
    screen.blit(textsurf, textrect)
    pygame.display.update()


def starve():         # Message when starving
    message_display('You starved to Death')


def escape():         # Message when escape
    message_display('You escaped')


def water():          # Message when drowned
    message_display("you drowned")


def dead():            # Message when die
    message_display("you are dead")


def movement():        # Mouse moving function
    i, j = random.choice(seif)
    global current_pos, mouse_posy, mouse_posx
    mouse_posy += j
    mouse_posx += i
    current_pos = (mouse_posx, mouse_posy)


def keys():
    message_display("Move the mouse using the arrows")