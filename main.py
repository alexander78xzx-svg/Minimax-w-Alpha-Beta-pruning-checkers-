#checkers game

import pygame

#code logic:
#one matrix as a board, another as a figurines placements. every turn we firstly check if a cell is black colored (1) 
#and then we check figurines position
#need to implement figure movement, figurine eating logic, multiple eats at a time logic.

#class Checker():

board   = [[0,2,0,2,0,2,0,2],
           [2,0,2,0,2,0,2,0],
           [0,2,0,2,0,2,0,2],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0]]

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Checkers")


black = pygame.image.load("black.png").convert_alpha()
black = pygame.transform.scale(black, (100,100))

white = pygame.image.load("white.png").convert_alpha()
white = pygame.transform.scale(white, (100,100))

red = pygame.image.load("red.png").convert_alpha()
red = pygame.transform.scale(red, (100,100))

def draw_board():
    imp = pygame.image.load("board.png").convert()
    imp = pygame.transform.scale(imp, (800,800))        #load the board image
    screen.blit(imp, (0, 0))
    screen.blit(imp, (0, 0))
def draw_figs():
    for i in range(8):
        for j in range(8):
            if board[j][i]==2:
                screen.blit(black, (100*i, 100*j))
            elif board[j][i]==1:
                screen.blit(white, (100*i, 100*j))
def draw_available_moves(pos1,pos2):
    if board[pos1][pos2]==1:
        if board[pos1-1][pos2+1]==0 or board[pos1-1][pos2-1]==0:
            screen.blit(red, (100*(pos2+1), 100*(pos1-1)))
            screen.blit(red, (100*(pos2-1), 100*(pos1-1)))
        else:
            pass


pos1 = None
pos2 = None
running = True
while running:
    for event in pygame.event.get():        #game loop
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            #selected = board[position[0]//100][position[1]//100]
            pos1 = position[1]//100
            pos2 = position[0]//100
            selected = board[position[1]//100][position[0]//100]
            print(pos1,pos2)
            #board[position[1]//100][position[0]//100] = 0   
    draw_board()
    draw_figs()
    if pos1!=None and pos2!=None:
        draw_available_moves(pos1,pos2)
    pygame.display.flip()

pygame.quit()