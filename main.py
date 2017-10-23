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
FPS = 30

grid= []

def gameLoop():
    global done

    drag_enabled = False

    #----Main Loop----#
    while not done:
        # clear screen
        screen.fill(WHITE)

        # EVENT LOOP
        for event in pg.event.get():
            # QUIT EVENT
            if event.type == pg.QUIT:
                done = True

            if event.type == pg.MOUSEBUTTONDOWN:
                # LEFT CLICK EVENT
                if event.button == 1:
                    drag_enabled = True
                    m_pos = pg.mouse.get_pos()
                    cell_x, cell_y = get_cell(m_pos[0], m_pos[1])

                    grid[cell_x][cell_y].filled = True

            if event.type == pg.MOUSEBUTTONUP:
                # LEFT CLICK UP EVENT
                if event.button == 1:
                    drag_enabled = False

            if event.type == pg.MOUSEMOTION:
                if drag_enabled:
                    m_pos = pg.mouse.get_pos()
                    cell_x, cell_y = get_cell(m_pos[0], m_pos[1])

                    grid[cell_x][cell_y].filled = True


        # --- Game Logic


        # --- Drawing

        drawGrid(grid)

        pg.display.flip()
        clock.tick(FPS)

def get_cell(x, y):
    col = 0
    for i in range(20,800,20):
        if x <= i:
            break
        col += 1

    row = 0
    for i in range(20,800,20):
        if y <= i:
            break
        row += 1

    return (row, col)

def makeGrid(grid):
    x = 0
    y = 0
    for y in range(0,800,20):
        row = []
        for x in range(0,800,20):
            row.append(Cell(x,y))
        grid.append(row)

def drawGrid(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw()
            count += 1

class Cell:
    # x,y - top left
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.filled = False

    def draw(self):
        if(self.filled):
            pg.draw.rect(screen, RED, (self.x,self.y,
                                       self.size,
                                       self.size),
                                       0)
        else:
            pg.draw.rect(screen, BLUE, (self.x,self.y,
                                        self.size,
                                        self.size),
                                        2)



if __name__ == '__main__':
    pg.init()
    makeGrid(grid)
    gameLoop()
