n1 = int(input("Enter N1: "))
n2 = int(input("Enter N2: "))
n3 = int(input("Enter N3: "))
A = float(input("Enter A: "))
B = float(input("Enter B: "))
N = n1 + n2 + n3

# n1 >= n2 >= n3
# 0 < B <= A < 1

Strategies = [[["V","V","V"],["C","V","V"],["O","V","V"]],
              [["V","V","C"],["C","V","C"],["O","V","C"]],
              [["V","V","O"],["C","V","O"],["O","V","O"]],
              [["V","C","V"],["C","C","V"],["O","C","V"]],
              [["V","C","C"],["C","C","C"],["O","C","C"]],
              [["V","C","O"],["C","C","O"],["O","C","O"]],
              [["V","O","V"],["C","O","V"],["O","O","V"]],
              [["V","O","C"],["C","O","C"],["O","O","C"]],
              [["V","O","O"],["C","O","O"],["O","O","O"]]]

Values = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]

for i in range(0,9):
    for j in range(0,3):
        # player1
        if Strategies[i][j][0] == "V":
            if n1 < B*N:
                value1 = 1
            else:
                value1 = 3
        if Strategies[i][j][0] == "C":
            if Strategies[i][j][1] != "C" and Strategies[i][j][2] != "C":
                value1 = 0
            elif Strategies[i][j][1] == "O":
                if n1 + n3 < A*N:
                    value1 = 1
                elif n1 + n3 < B*N:
                    value1 = 1
                else:
                    value1 = 3
            elif Strategies[i][j][2] == "O":
                if n1 + n2 < A*N:
                    value1 = 1
                elif n1 + n2 < B*N:
                    value1 = 1
                else:
                    value1 = 3
            elif Strategies[i][j][1] == "C":
                if n1 + n2 > B*N:
                    value1 = 3
                else:
                    value1 = 1
            elif Strategies[i][j][2] == "C":
                if n1 + n3 > B*N:
                    value1 = 3
                else:
                    value1 = 1
            if Strategies[i][j][1] == "C" and Strategies[i][j][2] == "C":
                value1 = 3
        if Strategies[i][j][0] == "O":
            if Strategies[i][j][1] == "O" or Strategies[i][j][2] == "O":
                    value1 = 2
            else:
                if n2 + n3 < A*N:
                    value1 = 2
                else:
                    value1 = 1
        Values[i][j].append(value1)


for i in range(0,9):
    for j in range(0,3):
        # player2
        if Strategies[i][j][1] == "V":
            if n2 < B*N:
                value2 = 1
            else:
                value2 = 3
        if Strategies[i][j][1] == "C":
            if Strategies[i][j][0] != "C" and Strategies[i][j][2] != "C":
                value2 = 0
            elif Strategies[i][j][0] == "O":
                if n2 + n3 < A*N:
                    value2 = 1
                elif n2 + n3 < B*N:
                    value2 = 1
                else:
                    value2 = 3
            elif Strategies[i][j][2] == "O":
                if n1 + n2 < A*N:
                    value2 = 1
                elif n1 + n2 < B*N:
                    value2 = 1
                else:
                    value2 = 3
            elif Strategies[i][j][0] == "C":
                if n1 + n2 > B*N:
                    value2 = 3
                else:
                    value2 = 1
            elif Strategies[i][j][2] == "C":
                if n2 + n3 > B*N:
                    value2 = 3
                else:
                    value2 = 1
            if Strategies[i][j][0] == "C" and Strategies[i][j][2] == "C":
                value2 = 3
        if Strategies[i][j][1] == "O":
            if Strategies[i][j][0] == "O" or Strategies[i][j][2] == "O":
                value2 = 2
            else:
                if n1 + n3 < A*N:
                    value2 = 2
                else:
                    value2 = 1
        Values[i][j].append(value2)


for i in range(0,9):
    for j in range(0,3):
        # player3
        if Strategies[i][j][2] == "V":
            if n3 < B*N:
                value3 = 1
            else:
                value3 = 3
        if Strategies[i][j][2] == "C":
            if Strategies[i][j][1] != "C" and Strategies[i][j][0] != "C":
                value3 = 0
            elif Strategies[i][j][1] == "O":
                if n1 + n3 < A*N:
                    value3 = 1
                elif n1 + n3 < B*N:
                    value3 = 1
                else:
                    value3 = 3
            elif Strategies[i][j][0] == "O":
                if n2 + n3 < A*N:
                    value3 = 1
                elif n2 + n3 < B*N:
                    value3 = 1
                else:
                    value3 = 3
            elif Strategies[i][j][1] == "C":
                if n2 + n3 > B*N:
                    value3 = 3
                else:
                    value3 = 1
            elif Strategies[i][j][0] == "C":
                if n1 + n3 > B*N:
                    value3 = 3
                else:
                    value3 = 1
            if Strategies[i][j][0] == "C" and Strategies[i][j][1] == "C":
                value3 = 3
        if Strategies[i][j][2] == "O":
            if Strategies[i][j][0] == "O" or Strategies[i][j][1] == "O":
                value3 = 2
            else:
                if n1 + n2 < A*N:
                    value3 = 2
                else:
                    value3 = 1
        Values[i][j].append(value3)

Label = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]

for row in range(9):
    for col in range(3):
        for r in range(9):
            if Label[row][col] == 0:
                if Values[r][col][1] > Values[row][col][1]:
                    # this is not a Nash Equilibrium
                    Label[row][col] = 2
        if Label[row][col] == 0:
            for c in range(3):
                if Label[row][col] == 0:
                    if Values[row][c][2] > Values[row][col][2]:
                        Label[row][col] = 2
for row in range(9):
    for col in range(3):
        for r in range(9):
            if Label[row][col] == 0:
                if Values[r][col][2] > Values[row][col][2]:
                    # this is not a Nash Equilibrium
                    Label[row][col] = 2
        if Label[row][col] == 0:
            for c in range(3):
                if Label[row][col] == 0:
                    if Values[row][c][0] > Values[row][col][0]:
                        Label[row][col] = 2
        if Label[row][col] == 0:
            Label[row][col] = 1

Winners = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]

for i in range(9):
    for j in range(3):
        # player1
        if Values[i][j][0] == 3:
            if Strategies[i][j][0] == "V":
                if Values[i][j][1] != 3 and Values[i][j][2] != 3:
                    if Winners[i][j] == []:
                        Winners[i][j].append("player1")
                else:
                    if Strategies[i][j][1] == "V" or Strategies[i][j][2] == "V":
                        if Winners[i][j] == "":
                            Winners[i][j].append("player1")
                    elif Strategies[i][j][1] == "C":
                        if n2 + n3 <= n1:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player1")
                        else:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player2 and player3")
            elif Strategies[i][j][0] == "C":
                if Strategies[i][j][1] == "C":
                    if Strategies[i][j][2] == "V":
                        if n1 + n2 < n3:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player3")
                        else:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player1 and player2")
                    else:
                        if Winners[i][j] == []:
                            Winners[i][j].append("player1 and player2 and player3")
                if Strategies[i][j][2] == "C":
                    if Strategies[i][j][1] == "V":
                        if n1 + n3 < n2:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player2")
                        else:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player1 and player3")
                    else:
                        if Winners[i][j] == []:
                            Winners[i][j].append("player1 and player2 and player3")
        # player2
        if Values[i][j][1] == 3:
            if Strategies[i][j][1] == "V":
                if Values[i][j][0] != 3 and Values[i][j][2] != 3:
                    if Winners[i][j] == []:
                        Winners[i][j].append("player2")
                else:
                    if Strategies[i][j][0] == "V":
                        if Winners[i][j] == []:
                            Winners[i][j].append("player1")
                    elif Strategies[i][j][0] == "C":
                        if n1 + n3 <= n2:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player2")
                        else:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player1 and player3")
            elif Strategies[i][j][1] == "C":
                if Strategies[i][j][0] == "C":
                    if Strategies[i][j][2] == "V":
                        if n1 + n2 < n3:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player3")
                        else:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player1 and player2")
                    else:
                        if Winners[i][j] == []:
                            Winners[i][j].append("player1 and player2 and player3")
                if Strategies[i][j][2] == "C":
                    if Strategies[i][j][0] == "V":
                        if n2 + n3 < n1:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player1")
                        else:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player2 and player3")
                    else:
                        if Winners[i][j] == []:
                            Winners[i][j].append("player1 and player2 and player3")
        # player3
        if Values[i][j][2] == 3:
            if Strategies[i][j][2] == "V":
                if Values[i][j][0] != 3 and Values[i][j][1] != 3:
                    if Winners[i][j] == []:
                        Winners[i][j].append("player3")
                else:
                    if Strategies[i][j][0] == "V":
                        if Winners[i][j] == []:
                            Winners[i][j].append("player1")
                    elif Strategies[i][j][1] == "V":
                        if Winners[i][j] == []:
                            Winners[i][j].append("player2")
                    elif Strategies[i][j][0] == "C":
                        if n1 + n2 <= n3:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player3")
                        else:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player1 and player2")
            elif Strategies[i][j][2] == "C":
                if Strategies[i][j][0] == "C":
                    if Strategies[i][j][1] == "V":
                        if n1 + n3 < n2:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player2")
                        else:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player1 and player3")
                    else:
                        if Winners[i][j] == []:
                            Winners[i][j].append("player1 and player2 and player3")
                if Strategies[i][j][1] == "C":
                    if Strategies[i][j][0] == "V":
                        if n2 + n3 < n1:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player1")
                        else:
                            if Winners[i][j] == []:
                                Winners[i][j].append("player2 and player3")
                    else:
                        if Winners[i][j] == []:
                            Winners[i][j].append("player1 and player2 and player3")

for i in range(9):
    for j in range(3):
        if Winners[i][j] == []:
            Winners[i][j].append("No one Wins")
                    
for the_row in range(9):
    for the_col in range(3):
        if Label[the_row][the_col] == 1:
            Str = ','.join(Strategies[the_row][the_col])
            print("Nash equilibrium is:",Str, Values[the_row][the_col], "Winner is/are:", Winners[the_row][the_col])