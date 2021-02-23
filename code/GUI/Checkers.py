import pygame
import pyautogui
pygame.init()
scrnw = int(1920)
scrnh = int(1080)
screen = pygame.display.set_mode((scrnw,scrnh), pygame.RESIZABLE)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
apricot = (247,187,147)
brown = (113,61,47)
pygame.display.set_caption('Checkers')

def drawboard(x = 0, y = 0):
    ax = 0
    ay = 0
    size = int(boardsize/8)
    while True:
        pygame.draw.rect(screen, red, (int(x+ax),int(y+ay),int(size),int(size)), 0)
        ax = ax + size*2
        if ax == size*8:
            ax = size
            ay = ay + size
        if ax == size*9:
            ax = 0
            ay = ay + size
            if ay == size*8:
                break
    bx = size
    by = 0
    while True:
        pygame.draw.rect(screen, black, (int(x+bx),int(y+by),int(size),int(size)), 0)
        bx = bx + size*2
        if bx == size*8:
            bx = size
            by = by + size
            if by == size*8:
                break
        if bx == size*9:
            bx = 0
            by = by + size

def pieces(x = 0, y = 0):
    global size
    size = int(boardsize/8)
    ax = size
    ay = 0
    global checkers
    checkers = []
    while True:
        checkers.append(piece(x+ax,y+ay, ax/size, ay/size, 'red'))
        ax = ax + size*2
        if ax == size*8:
            ax = size
            ay = ay + size
        if ax == size*9:
            ax = 0
            ay = ay + size
            if ay == size*8:
                break
        if ay == size*3:
            break
    bx = 0
    by = size*5
    while True:
        checkers.append(piece(x+bx,y+by, bx/size, by/size, 'black'))
        bx = bx + size*2
        if bx == size*8:
            bx = size
            by = by + size
            if by == size*8:
                break
        if bx == size*9:
            bx = 0
            by = by + size

def updatePieces(x = 0, y = 0):
    global size
    size = int(boardsize/8)
    i = 0
    while i < 12:
        pc = checkers[i]
        pc.setX(pc.getX())
        pc.setY(pc.getY())
        pc.show()
        i = i + 1
    while i < 24:
        pc = checkers[i]
        pc.setX(pc.getX())
        pc.setY(pc.getY())
        pc.show()
        i = i + 1
    pygame.display.update()
def background():
    screen.blit(felt, (0,0))
    drawboard((scrnw-boardsize)/2,(scrnh-boardsize)/2)
    screen.blit(frame, (int(((scrnw-boardsize)/2-frame.get_width())/2),0))
    screen.blit(frame, (int(((scrnw-(scrnw-boardsize)/2)+scrnw)/2-frame.get_width()/2),0))

def load():
    global felt
    global frame
    global redprsn
    global blackprsn
    global pointer
    global boardsize
    felt = pygame.image.load(r'greenfelt.jpg')
    felt = pygame.transform.smoothscale(felt, (scrnw, scrnh))
    frame = pygame.image.load(r'GoldFrameTransparent.png')
    frame = pygame.transform.smoothscale(frame, (int(scrnh*3/6), int(scrnh*3/6*(116/81))))
    redprsn = pygame.image.load(r'personiconred.png')
    blackprsn = pygame.image.load(r'personicon.png')
    pointer = pygame.image.load(r'pointer.png')
    boardsize = int(scrnh*4/5)

class board():
    pass

class piece():

    number = 0

    def __init__(self, x, y, xspot, yspot, color):
        self.pc = pygame.image.load(r'' + color + '.png')
        self.pc = pygame.transform.smoothscale(self.pc, (int(scrnh/10),int(scrnh/10)))
        self.x = int(x)
        self.y = int(y)
        self.xspot = xspot
        self.yspot = yspot
        self.color = color
        self.king = False
        self.eaten = False
        self.selected = False
        piece.number = piece.number + 1
        self.number = piece.number
        screen.blit(self.pc, (self.x,self.y))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
##        self.x = xx + self.xspot*size
        self.x = x

    def setY(self, y):
##        self.y = yy + self.yspot*size
        self.y = y

    def getSelect(self):
        return self.selected

    def select(self):
        self.selected = not self.selected

    def show(self):
        self.pc = pygame.transform.smoothscale(self.pc, (int(scrnh/10),int(scrnh/10)))
        screen.blit(self.pc, (self.x,self.y))
        if self.selected:
            pygame.draw.circle(screen, white, (int((self.x+(self.x+int(boardsize/8)))/2),int((self.y+(self.y+int(boardsize/8)))/2)), int(boardsize/8*0.4), int(scrnh/250))
    def valid(self, x, y):
        global turn
        if self.color == 'red':
            if turn % 2 == 0:
                return False
            fix = -1
        if self.color == 'black':
            if turn % 2 == 1:
                return False
            fix = 1
        xset = int((self.x-xx)/size)*size
        yset = int((self.y-yy)/size)*size
        if not self.king:
            print(yset, xset, int((y-yy)/size)*size, int((x-xx)/size)*size)
            if yset == int((y-yy)/size)*size+size*fix and xset == int((x-xx)/size)*size+size:
                self.y = int((y-yy)/size)*size+yy
                self.x = int((x-xx)/size)*size+xx
                turn = turn + 1
                return True
            elif yset == int((y-yy)/size)*size+size*fix and xset == int((x-xx)/size)*size-size:
                self.y = int((y-yy)/size)*size+yy
                self.x = int((x-xx)/size)*size+xx
                turn = turn + 1
                return True
        if self.king:
            if yset == int((y-yy)/size)*size-size*fix and xset == int((x-xx)/size)*size+size:
                self.y = int((y-yy)/size)*size+yy
                self.x = int((x-xx)/size)*size+xx
                turn = turn + 1
                return True
            elif yset == int((y-yy)/size)*size-size*fix and xset == int((x-xx)/size)*size-size:
                self.y = int((y-yy)/size)*size+yy
                self.x = int((x-xx)/size)*size+xx
                turn = turn + 1
                return True
        return False
        
wh = pygame.display.get_window_size()
tempscrnw = int(wh[0])
tempscrnh = int(wh[0]*9/16)
load()
pieces((scrnw-boardsize)/2,(scrnh-boardsize)/2)
choice = None
global xx
global yy
global turn
turn = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.WINDOWEVENT_MINIMIZED:
            scrnw = tempscrnw
            scrnh = tempscrnh
        elif event.type == pygame.WINDOWEVENT_MAXIMIZED:
            tempscrnw = scrnw
            tempscrnh = scrnh
            root.state('zoomed')
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
 
    xx = (scrnw-boardsize)/2
    yy = (scrnh-boardsize)/2
    if xx <= mouse[0] <= xx+boardsize and yy <= mouse[1] <= yy+boardsize:
        pyautogui.click(button='left')
        if click[0] == 1:
            for i in checkers:
                if i.getX() <= mouse[0] < i.getX()+size and i.getY() <= mouse[1] < i.getY()+size:
                    choice = i
                    for j in checkers:
                        if j.getSelect() and j != choice:
                            j.select()
                    i.select()
            if choice != None and choice.getSelect() and not(choice.getX() <= mouse[0] < choice.getX()+size and choice.getY() <= mouse[1] < choice.getY()+size):
                print(choice.valid(mouse[0], mouse[1]))

    wh = pygame.display.get_window_size()
    scrnw = int(wh[0])
    scrnh = int(wh[0]*9/16)
    screen = pygame.display.set_mode((scrnw,scrnh), pygame.RESIZABLE)
    load()
    background()
    updatePieces((scrnw-boardsize)/2,(scrnh-boardsize)/2)
    pygame.display.update()
    


    
