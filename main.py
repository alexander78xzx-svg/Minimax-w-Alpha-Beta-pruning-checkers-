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

pos1 = None
pos2 = None
selected_piece = None
target = None
current_player = 1

def draw_board():
    imp = pygame.image.load("board.png").convert()
    imp = pygame.transform.scale(imp, (800,800))        #load the board image
    screen.blit(imp, (0, 0))
    screen.blit(imp, (0, 0))
def draw_figs():
    for i in range(8):
        for j in range(8):
            if board[j][i]==2 or board[j][i]==4:
                screen.blit(black, (100*i, 100*j))
            elif board[j][i]==1 or board[j][i]==3:
                screen.blit(white, (100*i, 100*j))


def draw_available_moves(pos1,pos2):
    if board[pos1][pos2]==1:
        if pos2 + 1 <= 7:
            if board[pos1-1][pos2+1]==0:
                screen.blit(red, (100*(pos2+1), 100*(pos1-1)))
        if pos2-1>=0:
            if board[pos1-1][pos2-1]==0:
                screen.blit(red, (100*(pos2-1), 100*(pos1-1)))

    if board[pos1][pos2]==2:
        if pos2 + 1 <= 7:
            if board[pos1+1][pos2+1]==0:
                screen.blit(red, (100*(pos2+1), 100*(pos1+1)))
        if pos2-1>=0:
            if board[pos1+1][pos2-1]==0:
                screen.blit(red, (100*(pos2-1), 100*(pos1+1)))

def move(selected_piece,target):
    global current_player
    if current_player%2!=0:
        if board[selected_piece[0]][selected_piece[1]]==1:
            # jump logic
            if selected_piece[0] >= 2 and selected_piece[1] >= 2:
                if target==(selected_piece[0]-2,selected_piece[1]-2): # top left
                    if board[selected_piece[0]-1][selected_piece[1]-1] in [2,4]:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            if target[0]==0:
                                board[target[0]][target[1]] = 3
                            else:
                                board[target[0]][target[1]] = 1
                            board[selected_piece[0]-1][selected_piece[1]-1] = 0
                            selected_piece = None
                            #current_player+=1
                            return True
            if selected_piece[0] >= 2 and selected_piece[1] <= 5:
                if target==(selected_piece[0]-2,selected_piece[1]+2): # top right
                    if board[selected_piece[0]-1][selected_piece[1]+1] in [2,4]:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            if target[0]==0:
                                board[target[0]][target[1]] = 3
                            else:
                                board[target[0]][target[1]] = 1
                            board[selected_piece[0]-1][selected_piece[1]+1] = 0
                            selected_piece = None
                            #current_player+=1
                            return True
            if selected_piece[0] <= 5 and selected_piece[1] >= 2:
                if target==(selected_piece[0]+2,selected_piece[1]-2): # bottom left
                    if board[selected_piece[0]+1][selected_piece[1]-1] in [2,4]:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            if target[0]==0:
                                board[target[0]][target[1]] = 3
                            else:
                                board[target[0]][target[1]] = 1
                            board[selected_piece[0]+1][selected_piece[1]-1] = 0
                            selected_piece = None
                            #current_player+=1
                            return True
            if selected_piece[0] <= 5 and selected_piece[1] <= 5:
                if target==(selected_piece[0]+2,selected_piece[1]+2): # bottom right
                    if board[selected_piece[0]+1][selected_piece[1]+1] in [2,4]:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            if target[0]==0:
                                board[target[0]][target[1]] = 3
                            else:
                                board[target[0]][target[1]] = 1
                            board[selected_piece[0]+1][selected_piece[1]+1] = 0
                            selected_piece = None
                            #current_player+=1
                            return True
            if (target==(selected_piece[0]-1,selected_piece[1]-1) or target==(selected_piece[0]-1,selected_piece[1]+1)) and board[target[0]][target[1]]==0 :
                board[selected_piece[0]][selected_piece[1]] = 0
                if target[0]==0:
                    board[target[0]][target[1]] = 3
                else:
                    board[target[0]][target[1]] = 1
                selected_piece = None
                #current_player+=1
                return True
    elif current_player%2==0:
        if board[selected_piece[0]][selected_piece[1]]==2:
            # jump logic
            if selected_piece[0] >= 2 and selected_piece[1] >= 2:
                if target==(selected_piece[0]-2,selected_piece[1]-2): # top left
                    if board[selected_piece[0]-1][selected_piece[1]-1]==1:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            board[target[0]][target[1]] = 2
                            board[selected_piece[0]-1][selected_piece[1]-1] = 0
                            selected_piece = None
                            #current_player+=1
                            return True
            if selected_piece[0] >= 2 and selected_piece[1] <= 5:
                if target==(selected_piece[0]-2,selected_piece[1]+2): # top right
                    if board[selected_piece[0]-1][selected_piece[1]+1]==1:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            board[target[0]][target[1]] = 2
                            board[selected_piece[0]-1][selected_piece[1]+1] = 0
                            selected_piece = None
                            #current_player+=1
                            return True
            if selected_piece[0] <= 5 and selected_piece[1] >= 2:
                if target==(selected_piece[0]+2,selected_piece[1]-2): # bottom left
                    if board[selected_piece[0]+1][selected_piece[1]-1]==1:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            board[target[0]][target[1]] = 2
                            board[selected_piece[0]+1][selected_piece[1]-1] = 0
                            selected_piece = None
                            #current_player+=1
                            return True
            if selected_piece[0] <= 5 and selected_piece[1] <= 5:
                if target==(selected_piece[0]+2,selected_piece[1]+2): # bottom right
                    if board[selected_piece[0]+1][selected_piece[1]+1]==1:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            board[target[0]][target[1]] = 2
                            board[selected_piece[0]+1][selected_piece[1]+1] = 0
                            selected_piece = None
                            #current_player+=1
                            return True
            if (target==(selected_piece[0]+1,selected_piece[1]-1) or target==(selected_piece[0]+1,selected_piece[1]+1)) and board[target[0]][target[1]]==0 :
                board[selected_piece[0]][selected_piece[1]] = 0
                board[target[0]][target[1]] = 2
                selected_piece = None
                #current_player+=1
                return True
    (f"Current Turn: {current_player}")   
    return False


running = True
while running:
    for event in pygame.event.get():        #game loop
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            pos1 = position[1]//100
            pos2 = position[0]//100
            selected = board[position[1]//100][position[0]//100]

            
            if current_player%2==0:
                if (selected==2 or selected==4) and selected_piece==None:
                    selected_piece = (pos1,pos2)

            if current_player%2!=0:
                if (selected==1 or selected==3) and selected_piece==None:
                    selected_piece = (pos1,pos2)

            if selected_piece!=None and selected==0:
                target = (pos1,pos2)
                succes = move(selected_piece,target)
                print(current_player)
                if succes:
                    current_player+=1
                    print(current_player)
                selected_piece = None
                pos1 = None
                pos2 = None


            
    draw_board()
    draw_figs()
    if pos1!=None and pos2!=None:
        draw_available_moves(pos1,pos2)


    pygame.display.flip()

pygame.quit()