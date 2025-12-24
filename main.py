#checkers game

import pygame

board  = [[0,2,0,2,0,2,0,2],
           [2,0,2,0,2,0,2,0],
           [0,2,0,2,0,2,0,2],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0]]

board1 = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,0,0,0,0],[0,0,0,0,3,0,0,0],[0,4,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0]]
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Checkers")

# load textures:
black = pygame.image.load("black.png").convert_alpha()
black = pygame.transform.scale(black, (100,100))

white = pygame.image.load("white.png").convert_alpha()
white = pygame.transform.scale(white, (100,100))

red = pygame.image.load("red.png").convert_alpha()
red = pygame.transform.scale(red, (100,100))

white_king = pygame.image.load("white_king.png").convert_alpha()
white_king = pygame.transform.scale(white_king, (100,100))

black_king = pygame.image.load("black_king.png").convert_alpha()
black_king = pygame.transform.scale(black_king, (100,100))

pos1 = None
pos2 = None
selected_piece = None
target = None
current_player = 1
another_move = False #to prevent slides after first jump
def check_win():
    global board
    count_white = 0
    count_black = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] in [1,3]:
                count_white+=1
            if board[i][j] in [2,4]:
                count_black+=1
    if count_white==0 or count_black==0:
        return True
    return False
def can_king_jump_again(board, r_start, c_start, enemy_ids):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for d_row, d_col in directions:
        enemy_seen = False
        for i in range(1, 8):
            r = r_start + (d_row * i)
            c = c_start + (d_col * i)
            
            if not (0 <= r < 8 and 0 <= c < 8): break
            
            cell = board[r][c]
            if cell in enemy_ids:
                if enemy_seen: break 
                enemy_seen = True
            elif cell == 0:
                if enemy_seen: 
                    return True 
            else:
                break
    return False
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
            elif board[j][i]==3:
                screen.blit(white_king, (100*i, 100*j))
            elif board[j][i]==4:
                screen.blit(black_king, (100*i, 100*j))
def check_enemies_drawing(figure_type,selected_piece):
    if figure_type==1 or figure_type==3:
        oponent = (2,4)
    if figure_type==2 or figure_type==4:
        oponent = (1,3)
    moves = []
    if selected_piece[0] >= 2 and selected_piece[1] >= 2: #top left
        if board[selected_piece[0]-1][selected_piece[1]-1] in oponent:
            if board[selected_piece[0]-2][selected_piece[1]-2]==0:
                moves.append((selected_piece[0]-2,selected_piece[1]-2))
    if selected_piece[0] >= 2 and selected_piece[1] <= 5: #top right
        if board[selected_piece[0]-1][selected_piece[1]+1] in oponent:
            if board[selected_piece[0]-2][selected_piece[1]+2]==0:
                moves.append((selected_piece[0]-2,selected_piece[1]+2))
    if selected_piece[0] <= 5 and selected_piece[1] >= 2: #bottom left
        if board[selected_piece[0]+1][selected_piece[1]-1] in oponent:
            if board[selected_piece[0]+2][selected_piece[1]-2]==0:
                moves.append((selected_piece[0]+2,selected_piece[1]-2))
    if selected_piece[0] <= 5 and selected_piece[1] <= 5: #bottom right
        if board[selected_piece[0]+1][selected_piece[1]+1] in oponent:
            if board[selected_piece[0]+2][selected_piece[1]+2]==0:
                moves.append((selected_piece[0]+2,selected_piece[1]+2))
    return moves
def draw_available_moves(pos1,pos2):
    global current_player
    global selected_piece
    global another_move
    if current_player%2!=0:
        if board[pos1][pos2]==1:
            moves = check_enemies_drawing(board[selected_piece[0]][selected_piece[1]],selected_piece)
            if len(moves)==0:
                if pos2 + 1 <= 7:
                    if board[pos1-1][pos2+1]==0:
                        screen.blit(red, (100*(pos2+1), 100*(pos1-1)))
                if pos2-1>=0:
                    if board[pos1-1][pos2-1]==0:
                        screen.blit(red, (100*(pos2-1), 100*(pos1-1)))
            for i,j in moves:
                screen.blit(red, (j*100, i*100))
        if board[pos1][pos2]==3:
            for i in range(1,8,1):
                if pos1-i>=0 and pos2-i>=0: #top left
                    if board[pos1-i][pos2-i]==0:
                        screen.blit(red, (100*(pos2-i), 100*(pos1-i)))
                    if board[pos1-i][pos2-i] in [1,3]:
                        break
                    if pos1-i-1<8 and pos2-i-1>=0:
                        if board[pos1-i][pos2-i] in [2,4]:
                            if board[pos1-i-1][pos2-i-1] in [2,4]:
                                break
            for i in range(1,8,1):
                if pos1-i>=0 and pos2+i<8: #top right
                    if board[pos1-i][pos2+i]==0:
                        screen.blit(red, (100*(pos2+i), 100*(pos1-i)))
                    if board[pos1-i][pos2+i] in [1,3]:
                        break
                    if pos1-i-1<8 and pos2+i+1>=0:
                        if board[pos1-i][pos2+i] in [2,4]:
                            if board[pos1-i-1][pos2+i+1] in [2,4]:
                                break
            for i in range(1,8,1):
                if pos1+i<8 and pos2-i>=0: #bottom left
                    if board[pos1+i][pos2-i]==0:
                        screen.blit(red, (100*(pos2-i), 100*(pos1+i)))
                    if board[pos1+i][pos2-i] in [1,3]:
                        break
                    if pos1+i+1<8 and pos2-i-1>=0:
                        if board[pos1+i][pos2-i] in [2,4]:
                            if board[pos1+i+1][pos2-i-1] in [2,4]:
                                break
            for i in range(1,8,1):
                if pos1+i<8 and pos2+i<8: #bottom right
                    if board[pos1+i][pos2+i]==0:
                        screen.blit(red, (100*(pos2+i), 100*(pos1+i)))
                    if board[pos1+i][pos2+i] in [1,3]:
                        break
                    if pos1+i+1<8 and pos2+i-1>=0:
                        if board[pos1+i][pos2+i] in [2,4]:
                            if board[pos1+i+1][pos2-i+1] in [2,4]:
                                break
    if current_player%2==0:
        if board[pos1][pos2]==2:
            moves = check_enemies_drawing(board[selected_piece[0]][selected_piece[1]],selected_piece)
            if len(moves)==0:
                if pos2 + 1 <= 7:
                    if board[pos1+1][pos2+1]==0:
                        screen.blit(red, (100*(pos2+1), 100*(pos1+1)))
                if pos2-1>=0:
                    if board[pos1+1][pos2-1]==0:
                        screen.blit(red, (100*(pos2-1), 100*(pos1+1)))
            for i,j in moves:
                screen.blit(red, (j*100, i*100))
        if board[pos1][pos2]==4:
            for i in range(1,8,1):
                if pos1-i>=0 and pos2-i>=0: #top left
                    if board[pos1-i][pos2-i]==0:
                        screen.blit(red, (100*(pos2-i), 100*(pos1-i)))
                    if board[pos1-i][pos2-i] in [2,4]:
                        break
            for i in range(1,8,1):
                if pos1-i>=0 and pos2+i<8: #top right
                    if board[pos1-i][pos2+i]==0:
                        screen.blit(red, (100*(pos2+i), 100*(pos1-i)))
                    if board[pos1-i][pos2+i] in [2,4]:
                        break
            for i in range(1,8,1):
                if pos1+i<8 and pos2-i>=0: #bottom left
                    if board[pos1+i][pos2-i]==0:
                        screen.blit(red, (100*(pos2-i), 100*(pos1+i)))
                    if board[pos1+i][pos2-i] in [2,4]:
                        break
            for i in range(1,8,1):
                if pos1+i<8 and pos2+i<8: #bottom right
                    if board[pos1+i][pos2-i]==0:
                        screen.blit(red, (100*(pos2+i), 100*(pos1+i)))
                    if board[pos1+i][pos2+i] in [2,4]:
                        break
def check_ememies(figure_type,selected_piece):
    piece = board[selected_piece[0]][selected_piece[1]]
    is_king = piece in [3,4]
    is_white = piece in [1,3]
    oponent = [2,4] if is_white else [1,3]
    if is_king:
        return can_king_jump_again(board,selected_piece[0],selected_piece[1],enemy_ids=oponent)
    else:
        moves = [(1,1),(1,-1),(-1,1),(-1,-1)]
        for dr,dc in moves:
            land_r,land_c = selected_piece[0]+(dr*2),selected_piece[1]+(dc*2)
            mid_r,mid_c = selected_piece[0]+dr,selected_piece[1]+dc
            if 0<= land_r <8 and 0<=land_c <8:
                if board[land_r][land_c]==0:
                    if board[mid_r][mid_c] in oponent:
                        return True
    return False
def get_pieces_that_can_eat():
    global current_player
    moves = []
    if current_player%2!=0:
        for i in range(8):
            for j in range(8):
                if board[i][j] in [1,3]:
                    if check_ememies(board[i][j],(i,j)):
                        moves.append((i,j))
    elif current_player%2==0:
        for i in range(8):
            for j in range(8):
                if board[i][j] in [2,4]:
                    if check_ememies(board[i][j],(i,j)):
                        moves.append((i,j))
    return moves
def move(selected_piece,target):
    global current_player
    global another_move
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
                            if check_ememies(board[target[0]][target[1]],target):
                                another_move = True
                                return "double"
                            else:
                                another_move = False
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
                            if check_ememies(board[target[0]][target[1]],target):
                                another_move = True
                                return "double"
                            else:
                                another_move = False
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
                            if check_ememies(board[target[0]][target[1]],target):
                                another_move = True
                                return "double"
                            else:
                                another_move = False
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
                            if check_ememies(board[target[0]][target[1]],target):
                                another_move = True
                                return "double"
                            else:
                                another_move = False
                                return True
            if another_move == False:
                if (target==(selected_piece[0]-1,selected_piece[1]-1) or target==(selected_piece[0]-1,selected_piece[1]+1)) and board[target[0]][target[1]]==0 :
                    board[selected_piece[0]][selected_piece[1]] = 0
                    if target[0]==0:
                        board[target[0]][target[1]] = 3
                    else:
                        board[target[0]][target[1]] = 1
                    selected_piece = None
                    return True
        if board[selected_piece[0]][selected_piece[1]]==3:
            #slide logic:
            if (target==(selected_piece[0]-1,selected_piece[1]-1) or target==(selected_piece[0]-1,selected_piece[1]+1) or target==(selected_piece[0]+1,selected_piece[1]+1) or target==(selected_piece[0]+1,selected_piece[1]-1)) and board[target[0]][target[1]]==0 :
                board[selected_piece[0]][selected_piece[1]] = 0
                board[target[0]][target[1]] = 3
                selected_piece = None
                return True
            #jump logic:
            r_start, c_start = selected_piece
            valid_moves = []
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            for d_row, d_col in directions:
                enemy_seen = False
                for i in range(1, 8):
                    r = r_start + (d_row * i)
                    c = c_start + (d_col * i)
                    
                    if not (0 <= r < 8 and 0 <= c < 8):
                        break

                    cell = board[r][c]
                    if cell == 0:
                        if enemy_seen:
                            valid_moves.append((r, c))
                        else:
                            valid_moves.append((r, c))
                    elif cell in [2, 4]:
                        if enemy_seen: break 
                        enemy_seen = True
                    elif cell in [1, 3]:
                        break
            if (target[0], target[1]) in valid_moves:
                # Move the King
                board[target[0]][target[1]] = 3
                board[r_start][c_start] = 0
                selected_piece = None
                
                captured = False
                if abs(target[0] - r_start) > 1:
                    step_r = 1 if target[0] > r_start else -1
                    step_c = 1 if target[1] > c_start else -1
                    current_r, current_c = r_start + step_r, c_start + step_c
                    while current_r != target[0]:
                        if 0 <= current_r < 8 and 0 <= current_c < 8:
                            if board[current_r][current_c] in [2, 4]:
                                board[current_r][current_c] = 0
                                captured = True
                        current_r += step_r
                        current_c += step_c
                if captured:
                    if can_king_jump_again(board, target[0], target[1], enemy_ids=[2, 4]):
                        print("Double jump available! Turn continues.")
                        return "double"
                    else:
                        return True
                else:
                    return True
    elif current_player%2==0:
        if board[selected_piece[0]][selected_piece[1]]==2:
            # jump logic
            if selected_piece[0] >= 2 and selected_piece[1] >= 2:
                if target==(selected_piece[0]-2,selected_piece[1]-2): # top left
                    if board[selected_piece[0]-1][selected_piece[1]-1] in [1,3]:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            if target[0]==7:
                                board[target[0]][target[1]] = 4
                            else:
                                board[target[0]][target[1]] = 2
                            board[selected_piece[0]-1][selected_piece[1]-1] = 0
                            selected_piece = None
                            if check_ememies(board[target[0]][target[1]],target):
                                another_move = True
                                return "double"
                            else:
                                another_move = False
                                return True
            if selected_piece[0] >= 2 and selected_piece[1] <= 5:
                if target==(selected_piece[0]-2,selected_piece[1]+2): # top right
                    if board[selected_piece[0]-1][selected_piece[1]+1] in [1,3]:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            if target[0]==7:
                                board[target[0]][target[1]] = 4
                            else:
                                board[target[0]][target[1]] = 2
                            board[selected_piece[0]-1][selected_piece[1]+1] = 0
                            selected_piece = None
                            if check_ememies(board[target[0]][target[1]],target):
                                another_move = True
                                return "double"
                            else:
                                another_move = False
                                return True
            if selected_piece[0] <= 5 and selected_piece[1] >= 2:
                if target==(selected_piece[0]+2,selected_piece[1]-2): # bottom left
                    if board[selected_piece[0]+1][selected_piece[1]-1] in [1,3]:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            if target[0]==7:
                                board[target[0]][target[1]] = 4
                            else:
                                board[target[0]][target[1]] = 2
                            board[selected_piece[0]+1][selected_piece[1]-1] = 0
                            selected_piece = None
                            if check_ememies(board[target[0]][target[1]],target):
                                another_move = True
                                return "double"
                            else:
                                another_move = False
                                return True
            if selected_piece[0] <= 5 and selected_piece[1] <= 5:
                if target==(selected_piece[0]+2,selected_piece[1]+2): # bottom right
                    if board[selected_piece[0]+1][selected_piece[1]+1] in [1,3]:
                        if board[target[0]][target[1]]==0:
                            board[selected_piece[0]][selected_piece[1]] = 0
                            if target[0]==7:
                                board[target[0]][target[1]] = 4
                            else:
                                board[target[0]][target[1]] = 2
                            board[selected_piece[0]+1][selected_piece[1]+1] = 0
                            selected_piece = None
                            if check_ememies(board[target[0]][target[1]],target):
                                another_move = True
                                return "double"
                            else:
                                another_move = False
                                return True
            if another_move == False:
                if (target==(selected_piece[0]+1,selected_piece[1]-1) or target==(selected_piece[0]+1,selected_piece[1]+1)) and board[target[0]][target[1]]==0 :
                    board[selected_piece[0]][selected_piece[1]] = 0
                    if target[0]==7:
                        board[target[0]][target[1]] = 4
                    else:
                        board[target[0]][target[1]] = 2
                    selected_piece = None
                    return True
        if board[selected_piece[0]][selected_piece[1]] == 4:
            # slide logic (Standard move)
            if (target == (selected_piece[0]-1, selected_piece[1]-1) or 
                target == (selected_piece[0]-1, selected_piece[1]+1) or 
                target == (selected_piece[0]+1, selected_piece[1]+1) or 
                target == (selected_piece[0]+1, selected_piece[1]-1)) and board[target[0]][target[1]] == 0:
                
                board[selected_piece[0]][selected_piece[1]] = 0
                board[target[0]][target[1]] = 4
                selected_piece = None
                return True

            # jump logic:
            r_start, c_start = selected_piece
            valid_moves = []
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for d_row, d_col in directions:
                enemy_seen = False
                for i in range(1, 8):
                    r = r_start + (d_row * i)
                    c = c_start + (d_col * i)
                    
                    if not (0 <= r < 8 and 0 <= c < 8): break

                    cell = board[r][c]
                    if cell == 0:
                        valid_moves.append((r, c))
                    elif cell in [1, 3]:
                        if enemy_seen: break
                        enemy_seen = True
                    elif cell in [2, 4]:
                        break

            if (target[0], target[1]) in valid_moves:
                board[target[0]][target[1]] = 4
                board[r_start][c_start] = 0
                selected_piece = None
                
                captured = False
                if abs(target[0] - r_start) > 1:
                    step_r = 1 if target[0] > r_start else -1
                    step_c = 1 if target[1] > c_start else -1
                    current_r, current_c = r_start + step_r, c_start + step_c
                    
                    while current_r != target[0]:
                        if 0 <= current_r < 8 and 0 <= current_c < 8:
                            if board[current_r][current_c] in [1, 3]:
                                board[current_r][current_c] = 0
                                captured = True
                        current_r += step_r
                        current_c += step_c
                if captured:
                    if can_king_jump_again(board, target[0], target[1], enemy_ids=[1, 3]):
                        return "double"
                    else:
                        return True
                else:
                    return True
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
                if len(get_pieces_that_can_eat())==0:
                    if (selected==2 or selected==4):
                        selected_piece = (pos1,pos2)
                else:
                    if (selected==2 or selected==4):
                        if (pos1,pos2) in get_pieces_that_can_eat():
                            selected_piece = (pos1,pos2)

            if current_player%2!=0:
                if len(get_pieces_that_can_eat())==0:
                    if (selected==1 or selected==3):
                        selected_piece = (pos1,pos2)
                else:
                    if (selected==1 or selected==3):
                        if (pos1,pos2) in get_pieces_that_can_eat():
                            selected_piece = (pos1,pos2)
            if selected_piece!=None and selected==0:
                target = (pos1,pos2)
                succes = move(selected_piece,target)
                if succes=="double":
                    another_move = True
                    selected_piece=target
                elif succes==True:
                    current_player+=1
                    print(current_player)
                selected_piece = None
                pos1 = None
                pos2 = None
                if check_win():
                    running = False


            
    draw_board()
    draw_figs()

    if selected_piece is not None:
        draw_available_moves(selected_piece[0],selected_piece[1])

    pygame.display.flip()

pygame.quit()