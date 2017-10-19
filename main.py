import pygame as pg

# ------------ Setup ------------- #
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

WIDTH = 800
HEIGHT = 800
CENTERX = int(WIDTH/2)
CENTERY = int(HEIGHT/2)

size = (WIDTH, HEIGHT)
screen = pg.display.set_mode(size)
pg.display.set_caption("Grid")

# game loop done?
done = False
# pygame clock object
clock = pg.time.Clock()
# frame rate
FPS = 60

def gameLoop():
    global done

    #----Main Loop----#
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True


        # --- Game Logic


        # clear screen
        screen.fill(WHITE)

        # --- Drawing

        drawGrid()

        pg.display.flip()
        clock.tick(FPS)

def drawGrid():
    x1, x2 = -20, 0
    y1, y2 = -20, 0

    # pg.draw.rect(screen, BLUE, (0,0,20,20), 2)
    for i in range(40):
        y1 += 20
        y2 += 20
        x1, x2 = 0, 20
        for j in range(40):
            x1 += 20
            x2 += 20
            pg.draw.rect(screen, BLUE, (x1,y1,x2,y2), 2)

class Square:
    def __init__(self, x, y):
        pass

if __name__ == '__main__':
    pg.init()
    gameLoop()
