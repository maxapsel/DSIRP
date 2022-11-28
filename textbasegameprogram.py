#Tic Tac Toe
#This is where we will being doing our project


board = ["1","2","3"],["4","5","6"],["7","8","9"]               # this creates the board


turn = True             #this keeps track of the turn           

dic = {
 '1':[0,0],
 '2':[0,1],
 '3':[0,2],
 '4':[1,0],
 '5':[1,1],
 '6':[1,2],
 '7':[2,0],
 '8':[2,1],
 '9':[2,2]
 }              #creates a dictionary to convert single ints into coordinates

def printBoard(currentBoard):           #this prints the current board
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            print(board[i][j], end=" ")
        print()
    print("\n")

def isXTurn():             #finds which turn it is and out puts the string to print out
    if (turn):
        return "x"
    else:
        return "o"

def isWinner():                   #Determines if a win condition exists
    if board[0][0]+board[0][1]+board[0][2] == "xxx":
        ifWin(True)
        return True
    if board[0][0]+board[0][1]+board[0][2] == "ooo":
        ifWin(False)
        return True
    if board[1][0]+board[1][1]+board[1][2] == "xxx":
        ifWin(True)
        return True
    if board[1][0]+board[1][1]+board[1][2] == "ooo":
        ifWin(False)
        return True
    if board[2][0]+board[2][1]+board[2][2] == "xxx":
        ifWin(True)
        return True
    if board[2][0]+board[2][1]+board[2][2] == "ooo":
        ifWin(False)
        return True
    if board[0][0]+board[1][0]+board[2][0] == "xxx":
        ifWin(True)
        return True
    if board[0][0]+board[1][0]+board[2][0] == "ooo":
        ifWin(False)
        return True
    if board[0][1]+board[1][1]+board[2][1] == "xxx":
        ifWin(True)
        return True
    if board[0][1]+board[1][1]+board[2][1] == "ooo":
        ifWin(False)
        return True
    if board[0][2]+board[1][2]+board[2][2] == "xxx":
        ifWin(True)
        return True
    if board[0][2]+board[1][2]+board[2][2] == "ooo":
        ifWin(False)
        return True
    if board[0][0]+board[1][1]+board[2][2] == "xxx":
        ifWin(True)
        return True
    if board[0][0]+board[1][1]+board[2][2] == "ooo":
        ifWin(False)
        return True
    if board[2][0]+board[1][1]+board[0][2] == "xxx":
        ifWin(True)
        return True
    if board[2][0]+board[1][1]+board[0][2] == "ooo":
        ifWin(False)
        return True


def ifWin(win_1): #Prints who wins
    if win_1 == True:
        print("X wins")
            

    if win_1 == False:
        print("O wins")

            
for i in range(0,9):    #Repeats the turns 9 times
    printBoard(board)
    newSpot = input("Chose an open square: ")    #gets the players move
    cd_index = dic.get(newSpot)    #checks the dictionary for the coordinates
    in1 = cd_index[0]
    in2 = cd_index[1]              #converts the out put of the dictionary from 1 list to to ints
    if (board[in1][in2] == 'x') or (board[in1][in2] == "o"):    #Checks if the move is invalid
        print("Invalid Move")
        newSpot = input("Chose an open square: ")
        cd_index = dic.get(newSpot)    #checks the dictionary for the coordinates
        in1 = cd_index[0]
        in2 = cd_index[1]              #converts the out put of the dictionary from 1 list to to ints
    board[in1][in2] = isXTurn()             #prints the correct string onto the board
    turn = not turn
    if (isWinner() == True):
        break
    elif i == 8: 
        print("The game is tied, nobody wins.")
        break

printBoard(board)
