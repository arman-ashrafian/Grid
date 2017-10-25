import pygame as pg

# ------------ Setup ------------- #
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREY  = (100,100,100)

WIDTH = 1200
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

    clearButton = ClearButton(1000,100)

    agent = Agent()

    #----Main Loop----#
    while not done:
        # clear screen
        screen.fill(GREY)

        # EVENT LOOP
        for event in pg.event.get():
            # QUIT EVENT
            if event.type == pg.QUIT:
                done = True

            if event.type == pg.MOUSEBUTTONDOWN:
                # LEFT CLICK EVENT
                if event.button == 1:
                    # cell clicked?
                    drag_enabled = True
                    m_pos = pg.mouse.get_pos()
                    cell_x, cell_y = get_cell(m_pos[0], m_pos[1])

                    if cell_x >= 0 and cell_y >= 0:
                        grid[cell_x][cell_y].filled = True
                    else:
                        # clear button clicked?
                        if m_pos[0] > 1000 and m_pos[0] < 1100:
                            if m_pos[1] > 100 and m_pos[1] < 150:
                                clearGrid()

            if event.type == pg.MOUSEBUTTONUP:
                # LEFT CLICK UP EVENT
                if event.button == 1:
                    drag_enabled = False

            if event.type == pg.MOUSEMOTION:
                if drag_enabled:
                    m_pos = pg.mouse.get_pos()
                    cell_x, cell_y = get_cell(m_pos[0], m_pos[1])

                    if cell_x > 0 and cell_y > 0:
                        grid[cell_x][cell_y].filled = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    if agent.x != 40:
                        agent.x += 1

                elif event.key == pg.K_LEFT:
                    if agent.x != 0:
                        agent.x -= 1

                elif event.key == pg.K_DOWN:
                    if agent.y != 40:
                        agent.y += 1

                elif event.key == pg.K_UP:
                    if agent.y != 0:
                        agent.y -= 1


        # --- Game Logic ---


        # --- Drawing ---

        drawGrid(grid)
        clearButton.draw()

        # draw Agent
        grid[agent.y][agent.x].highlight()

        pg.display.flip()
        clock.tick(FPS)

def clearGrid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].filled = False

def get_cell(x, y):

    if x > 800: return (-1,-1)

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
            pg.draw.rect(screen, BLACK, (self.x,self.y,
                                        self.size,
                                        self.size),
                                        2)

    def highlight(self):
        pg.draw.rect(screen, GREEN, (self.x,self.y,
                                   self.size,
                                   self.size),
                                   0)

class ClearButton:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 50

    def draw(self):
        pg.draw.rect(screen, BLACK, (self.x,self.y,
                                    self.width,
                                    self.height),
                                    0)

class Agent:
    def __init__(self):
        self.x = 0
        self.y = 0

if __name__ == '__main__':
    pg.init()
    makeGrid(grid)
    gameLoop()
