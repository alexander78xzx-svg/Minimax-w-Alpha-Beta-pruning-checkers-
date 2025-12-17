matrix = [[0,1,0,1,0,1,0,1],
          [1,0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0,1],
          [1,0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0,1],
          [1,0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0,1],
          [1,0,1,0,1,0,1,0]]

figures = [[0,3,0,3,0,3,0,3],
           [3,0,3,0,3,0,3,0],
           [0,3,0,3,0,3,0,3],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [4,0,4,0,4,0,4,0],
           [0,4,0,4,0,4,0,4],
           [4,0,4,0,4,0,4,0]]

def move():
    move_line = int(input("Enter line number") + 1)
    move_col = int(input("Enter column number") + 1)
    
    final_position = figures[move_line][move_col]
    if final_position==3 or final_position==4:
        return 0
    
    

            
while True:
    for i in range(len(figures)):
        print(figures[i])
    choice_line = int(input("Enter line number") + 1)
    choice_col = int(input("Enter column number") + 1)
    selected_figure = figures[choice_line][choice_col]
    
    print("Now select a cell where you want to move")
    i = 0
    while i<1:
        i = move()