import pygame
import pyautogui
pygame.init()
scrnh = 1080
scrnw = 1920
screen = pygame.display.set_mode((scrnw,scrnh))
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
apricot = (247,187,147)
brown = (113,61,47)
pygame.display.set_caption('Checkers')

def board(x = 0, y = 0):
    ax = 0
    ay = 0
    size = boardsize/8
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

class piece():
    def __init__(self, x, y, color):
        self.pc = pygame.image.load(r'' + color + '.png')
        self.pc = pygame.transform.smoothscale(self.pc, (int(scrnh/10),int(scrnh/10)))
        self.x = x
        self.y = y
        self.color = color
        self.king = False
        self.eaten = False
        screen.blit(self.pc, (self.x,self.y))


def pieces(x = 0, y = 0):
    size = boardsize/8
    ax = size
    ay = 0
    checkers = []
    while True:
        checkers.append(piece(x+ax,y+ay, 'red'))
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
        checkers.append(piece(x+bx,y+by, 'black'))
        bx = bx + size*2
        if bx == size*8:
            bx = size
            by = by + size
            if by == size*8:
                break
        if bx == size*9:
            bx = 0
            by = by + size
    pygame.display.update()

def background():
    
    screen.blit(felt, (0,0))
    board((scrnw-boardsize)/2,(scrnh-boardsize)/2)
    screen.blit(frame, (((scrnw-boardsize)/2-frame.get_width())/2,0))
    screen.blit(frame, (((scrnw-(scrnw-boardsize)/2)+scrnw)/2-frame.get_width()/2,0))

def load():
    global felt
    global frame
    global redprsn
    global blackprsn
    global pointer
    global boardsize
    felt = pygame.image.load(r'greenfelt.jpg')
    felt = pygame.transform.smoothscale(felt, (1920, 1080))
    frame = pygame.image.load(r'GoldFrameTransparent.png')
    frame = pygame.transform.smoothscale(frame, (int(frame.get_width()*0.6), int(frame.get_height()*0.6)))
    redprsn = pygame.image.load(r'personiconred.png')
    blackprsn = pygame.image.load(r'personicon.png')
    pointer = pygame.image.load(r'pointer.png')
    boardsize = 864

load()
background()
pygame.display.update()
pieces((scrnw-boardsize)/2,(scrnh-boardsize)/2)
