import pygame as pg
from dijkstra import Graph

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
                        if not (cell_x == agent.x and cell_y == agent.y):
                            grid[cell_x][cell_y].filled = True
                    else:
                        # clear button clicked?
                        clearButton.checkClick(m_pos[0], m_pos[1])

            if event.type == pg.MOUSEBUTTONUP:
                # LEFT CLICK UP EVENT
                if event.button == 1:
                    drag_enabled = False

            if event.type == pg.MOUSEMOTION:
                if drag_enabled:
                    m_pos = pg.mouse.get_pos()
                    cell_x, cell_y = get_cell(m_pos[0], m_pos[1])

                    if cell_x >= 0 and cell_y >= 0:
                        if not (cell_x == agent.x and cell_y == agent.y):
                            grid[cell_x][cell_y].filled = True


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
    num = 0
    for y in range(0,800,20):
        row = []
        for x in range(0,800,20):
            row.append(Cell(x,y,num))
            num += 1
        grid.append(row)

    for row in grid:
        for cell in row:
            cell.addNeighbors(grid)

def drawGrid(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw()
            count += 1


class Cell:
    # x,y - top left
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.size = 20
        self.filled = False
        self.neighbors = []
        self.id = num

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)

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

    def addNeighbors(self, grid):
        i = int(self.y/20)
        j = int(self.x/20)

        if i < len(grid[0]) - 1:
            if not grid[i + 1][j].filled:
                self.neighbors.append(grid[i + 1][j])
        if i > 0:
            if not grid[i - 1][j].filled:
                self.neighbors.append(grid[i - 1][j])
        if j < len(grid[0]) - 1:
            if not grid[i][j + 1].filled:
                self.neighbors.append(grid[i][j + 1])
        if j > 0:
            if not grid[i][j - 1].filled:
                self.neighbors.append(grid[i][j - 1])

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
    def checkClick(self, x, y):
        if x > self.x and x < self.x + self.width:
            if y > self.y and y < self.y + self.height:
                clearGrid()


class Agent:
    def __init__(self):
        self.x = 0
        self.y = 0

if __name__ == '__main__':
    pg.init()
    makeGrid(grid)

    g = Graph(1600, grid)
    print(g.dijkstra(grid[0][0], grid[5][5]))

    gameLoop()
