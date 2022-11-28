#Tic Tac Toe

board = ["1","2","3","4","5","6","7","8","9"]               # this creates the board         

def printBoard(currentBoard):           #this prints the current board
    for i in range(len(board)) :
        print(board[i], end=" ")
        if i%3==2:
            print()

def isWinner():                   #Determines if a win condition exists and print the winner
    for i in range(0, len(board) - 2):
        #checks for vertical or horizontal winner
        if (board[i] == board[i+1] and board[i+1] == board[i+2]) or (i < 3 and board[i] == board[i+3] and board[i+3] == board[i+6]):
            print(f"{board[i]} wins.")
            return True
        #checks for a diagonal win
        elif (board[0] == board[4] and board[0] == board[8]) or (board[2] == board[4] and board[2] == board[6]):
            print(f"{board[4]} wins.")
            return True
        
    return False    #return false if there is no winner at that time

i = 0       
while True:    #Repeats the turns 9 times
    printBoard(board)
    newSpot = input("Chose an open square: ")    #gets the players move
    index = int(newSpot) - 1    #sets index to the coordinate of the input
    if (board[index] == 'x') or (board[index] == "o"):    #Checks if the move is invalid
        print("Invalid Move")
        continue

    if(i%2==0):     #if it is x's turn, x gets placed on the board
        board[index] = 'x' 
    else:       #if it is o's turn, o gets placed on the board
        board[index] = 'o'
    
    if (isWinner()):
        break
    elif i == 8: 
        print("The game is tied, nobody wins.")
        break

    i += 1

printBoard(board)