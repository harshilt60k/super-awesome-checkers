import pygame
import pyautogui
from os import path
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

def makeButtons():
    global buttons
    buttons = []
    buttons.append(button('undo', 0, 8))
    buttons.append(button('redo', 1, 8))
    buttons.append(button('settings', 7, 8))
        
def updatePieces(x = 0, y = 0):
    global size
    size = int(boardsize/8)
    i = 0
    while i < 24:
        pc = checkers[i]
        pc.setX()
        pc.setY()
        pc.show()
        i = i + 1
    i = 0
    while i < 3:
        pc = buttons[i]
        pc.setX()
        pc.setY()
        pc.show()
        i = i + 1
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
    pygame.font.init()
    felt = pygame.image.load(r'greenfelt.jpg')
    felt = pygame.transform.smoothscale(felt, (scrnw, scrnh))
    frame = pygame.image.load(r'GoldFrameTransparent.png')
    frame = pygame.transform.smoothscale(frame, (int(scrnh*3/6), int(scrnh*3/6*(116/81))))
    redprsn = pygame.image.load(r'personiconred.png')
    blackprsn = pygame.image.load(r'personicon.png')
    pointer = pygame.image.load(r'pointer.png')
    boardsize = int(scrnh*4/5)

class button():
    def __init__(self, name, xspot, yspot = 8):
        self.xspot = xspot
        self.yspot = yspot
        self.name = name
        self.selected = False
        if path.exists(r'' + name + '.png'):
            self.pc = pygame.image.load(r'' + name + '.png')
        else:
            self.pc = pygame.image.load(r'' + name + '.jpg')

    def do(self):
        if self.name == 'undo':
            pass
        if self.name == 'redo':
            pass
        if self.name == 'settings':
            while True:
                wh = pygame.display.get_window_size()
                scrnw = int(wh[0])
                scrnh = int(wh[0]*9/16)
                screen = pygame.display.set_mode((scrnw,scrnh), pygame.RESIZABLE)
                xx = (scrnw-boardsize)/2
                yy = (scrnh-boardsize)/2
                load()
                background()
                updatePieces()
                column = 0
                lessr = 153/(boardsize)
                r = 153
                lessg = 179/(boardsize)
                g = 179
                moreb = (255 - 237)/(boardsize)
                b = 237
                while column < boardsize + 1:
                    pygame.draw.line(screen, (r,g,b), (xx,yy+column), (xx+boardsize,yy+column), 1)
                    r = r - lessr
                    g = g - lessg
                    b = b + moreb
                    column = column + 1
                afont = pygame.font.SysFont('microsoftyaheimicrosoftyaheiui', int(scrnh/30))
                text = afont.render('Themes', True, (0, 0, 0))
                screen.blit(text, (xx, yy))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        for i in buttons:
                            if i.getX() <= mouse[0] < i.getX()+size and i.getY() <= mouse[1] < i.getY()+size:
                                choice = i
                                for j in buttons:
                                    if j.getSelect() and j != choice:
                                        j.select()
                                i.select()
                                if i == self:
                                    self.selected = False
                                    return
                                i.do()
                pygame.display.update()
                
        self.selected = False

    def getSelect(self):
        return self.selected

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self):
        self.x = xx + self.xspot*size

    def setY(self):
        self.y = yy + self.yspot*size

    def select(self):
        self.selected = True

    def show(self):
        length = int(scrnh/10*0.7)

        if self.selected:
            if path.exists(r'' + self.name + 'blue.png'):
                self.pc = pygame.image.load(r'' + self.name + 'blue.png')
            else:
                self.pc = pygame.image.load(r'' + self.name + 'blue.jpg')
        else:
            if path.exists(r'' + self.name + '.png'):
                self.pc = pygame.image.load(r'' + self.name + '.png')
            else:
                self.pc = pygame.image.load(r'' + self.name + '.jpg')
        self.pc = pygame.transform.smoothscale(self.pc, (length,length))
        screen.blit(self.pc, (self.x + int(length/0.7 - length)/2, self.y + int((length/0.7 - length)/2)))

class piece():

    number = 0
    redeaten = 0
    blackeaten = 0

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
        self.timeeaten = None
        piece.number = piece.number + 1
        self.number = piece.number
        screen.blit(self.pc, (self.x,self.y))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def makeKing(self):
        self.king = True
        self.pc = pygame.image.load(r'' + self.color + 'king.png')
        self.pc = pygame.transform.smoothscale(self.pc, (int(scrnh/10),int(scrnh/10)))

    def setX(self):
        if not self.eaten:
            self.x = xx + self.xspot*size
        else:
            inby = int(scrnh/17)
            if self.color == 'red':
                self.x = (int(((scrnw-boardsize)/2-frame.get_width())/2) + inby) + (int(scrnh*3/6) - inby)/3*(self.timeeaten % 3)
            if self.color == 'black':
                self.x = (int(((scrnw-(scrnw-boardsize)/2)+scrnw)/2-frame.get_width()/2) + inby) + (int(scrnh*3/6) - inby)/3*(self.timeeaten % 3)

    def setY(self):
        if not self.eaten:
            self.y = yy + self.yspot*size
        else:
            inby = int(scrnh/17)
            if self.color == 'red':
                self.y = (0 + inby) + (int(scrnh*3/6*(116/81)) - inby*2)/4*int(self.timeeaten / 3)
            if self.color == 'black':
                self.y = (0 + inby) + (int(scrnh*3/6*(116/81)) - inby*2)/4*int(self.timeeaten / 3)

    def getSelect(self):
        return self.selected

    def eat(self):
        self.eaten = True
        self.y = 0
        self.x = 0
        self.yspot = -2
        self.xspot = -2
        if self.color == 'red':
            self.timeeaten = piece.redeaten
            piece.redeaten += 1

        elif self.color == 'black':
            self.timeeaten = piece.blackeaten
            piece.blackeaten += 1

    def motion(self, oldx, oldy, chngsize):
        rect = pygame.Rect(xx, yy, boardsize, boardsize)
        board = screen.subsurface(rect)
        pygame.image.save(board, r'board.png')
        board = pygame.image.load(r'board.png')
        xf = 0
        yf = 0
        x = self.x - oldx
        y = self.y - oldy
        speed = 50
        grow = 3
        i = 0
        while True:
            screen.blit(board, (xx, yy))
            pygame.display.update()
            xf = xf + x/speed
            yf = yf + y/speed
            self.pc = pygame.image.load(r'' + self.color + 'king'*self.king + '.png')
            self.pc = pygame.transform.smoothscale(self.pc, (int(scrnh/10+(-abs(i-speed/2)+speed/2)*grow*chngsize),int(scrnh/10+(-abs(i-speed/2)+speed/2)*grow*chngsize)))
            screen.blit(self.pc, (oldx + xf - (-abs(i-speed/2)+speed/2)*grow*chngsize/2, oldy + yf - (-abs(i-speed/2)+speed/2)*grow*chngsize/2))
            pygame.display.update()
            if i == speed:
                screen.blit(board, (xx, yy))
                screen.blit(self.pc, (self.x, self.y))
                pygame.display.update()
                break
            i = i + 1
    
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
        oldx = self.x
        oldy = self.y
        boolean = False
        if not self.king:
            if yset == int((y-yy)/size)*size+size*fix and xset == int((x-xx)/size)*size+size:
                boolean = True
            elif yset == int((y-yy)/size)*size+size*fix and xset == int((x-xx)/size)*size-size:
                boolean = True
        if self.king:
            if yset == int((y-yy)/size)*size-size*fix and xset == int((x-xx)/size)*size+size:
                boolean = True
            elif yset == int((y-yy)/size)*size-size*fix and xset == int((x-xx)/size)*size-size:
                boolean = True
        if boolean:
            self.y = int((y-yy)/size)*size+yy
            self.x = int((x-xx)/size)*size+xx
            self.yspot = int((y-yy)/size)
            self.xspot = int((x-xx)/size)
            if not self.king and ((self.yspot == 0 and self.color == 'black') or (self.yspot == 7 and self.color == 'red')):
                self.makeKing()
            turn = turn + 1
            self.motion(oldx, oldy, False)
        return boolean

    def jumpValid(self, x, y):
        global turn
        minusturn = False
        if self.color == 'red':
            if turn % 2 == 0:
                minusturn = True
            fix = -1
        if self.color == 'black':
            if turn % 2 == 1:
                minusturn = True
            fix = 1
        xset = int((self.x-xx)/size)*size
        yset = int((self.y-yy)/size)*size
        oldx = self.x
        oldy = self.y
        oldxspot = self.xspot
        oldyspot = self.yspot
        boolean = False
        if yset == int((y-yy)/size)*size+size*fix*2 and xset == int((x-xx)/size)*size+size*2:
            boolean = True
        elif yset == int((y-yy)/size)*size+size*fix*2 and xset == int((x-xx)/size)*size-size*2:
            boolean = True
        if self.king:
            if yset == int((y-yy)/size)*size-size*fix*2 and xset == int((x-xx)/size)*size+size*2:
                boolean = True
            elif yset == int((y-yy)/size)*size-size*fix*2 and xset == int((x-xx)/size)*size-size*2:
                boolean = True
        eatboolean = False
        if boolean:
            self.y = int((y-yy)/size)*size+yy
            self.x = int((x-xx)/size)*size+xx
            self.yspot = int((y-yy)/size)
            self.xspot = int((x-xx)/size)
        for checker in checkers:
            if checker.color != self.color and (xset+xx < checker.getX() < self.x or xset+xx > checker.getX() > self.x) and (yset+yy < checker.getY() < self.y or yset+yy > checker.getY() > self.y):
                checker.eat()
                eatboolean = True
                break
        if not eatboolean:
            print(self.x, self.y, self.xspot, self.yspot)
            self.x = oldx
            self.y = oldy
            self.xspot = oldxspot
            self.yspot = oldyspot
            turn = turn - 1
            boolean = False
        else:
            self.y = int((y-yy)/size)*size+yy
            self.x = int((x-xx)/size)*size+xx
            self.yspot = int((y-yy)/size)
            self.xspot = int((x-xx)/size)
            if not self.king and ((self.yspot == 0 and self.color == 'black') or (self.yspot == 7 and self.color == 'red')):
                self.makeKing()
            turn = turn + 1
            self.motion(oldx, oldy, True)
            if minusturn:
                turn = turn - 1
        return boolean

wh = pygame.display.get_window_size()
tempscrnw = int(wh[0])
tempscrnh = int(wh[0]*9/16)
load()
pieces((scrnw-boardsize)/2,(scrnh-boardsize)/2)
makeButtons()
choice = None
global xx
global yy
global turn
turn = 0
while True:
    xx = (scrnw-boardsize)/2
    yy = (scrnh-boardsize)/2
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for i in buttons:
                if i.getX() <= mouse[0] < i.getX()+size and i.getY() <= mouse[1] < i.getY()+size:
                    choice = i
                    for j in buttons:
                        if j.getSelect() and j != choice:
                            j.select()
                    i.select()
                    i.do()
            for i in checkers:
                if i.getX() <= mouse[0] < i.getX()+size and i.getY() <= mouse[1] < i.getY()+size:
                    choice = i
                    for j in checkers:
                        if j.getSelect() and j != choice:
                            j.select()
                    i.select()
            if choice != None and choice.getSelect() and abs(choice.xspot - (int((mouse[0]-xx)/size))) == 2 and abs(choice.yspot - (int((mouse[1]-yy)/size))) == 2:
                choice.jumpValid(mouse[0], mouse[1])
            elif choice != None and choice.getSelect() and not(choice.getX() <= mouse[0] < choice.getX()+size and choice.getY() <= mouse[1] < choice.getY()+size):
                choice.valid(mouse[0], mouse[1])
    wh = pygame.display.get_window_size()
    scrnw = int(wh[0])
    scrnh = int(wh[0]*9/16)
    screen = pygame.display.set_mode((scrnw,scrnh), pygame.RESIZABLE)
    load()
    background()
    updatePieces((scrnw-boardsize)/2,(scrnh-boardsize)/2)
    pygame.display.update()


    
