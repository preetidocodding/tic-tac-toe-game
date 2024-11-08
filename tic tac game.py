import random
#printing the game board

board = ["-","-" ,"-"
         ,"-","-","-",
         "-","-","-"
         ]
currentplayer = "x"
winner = None
gamerunning=True
def printboard(board):
    print(board[0]+' | '+board[1]+' | '+board[2])
    print("---------")
    print(board[3]+' | '+board[4]+' | '+board[5])
    print("----------")
    print(board[6]+' | '+board[7]+' | '+board[8])

    # take player input
def playerinput(board):
    inp =int(input("enter the number 1-9: "))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1] = currentplayer
    else:
        print("oops you choosing the wrong spot!")
 


    # check win or tie
def checkhorizontle(borad):
        global winner
        if board[0]==board[1]==board[2]and board[1]!="-":
            winner=board[0]
            return True
        elif board[3]==board[4]==board[5] and board[3]!="-":
             winner=board[3]
             return True
        elif board[6]==board[7]==board[8] and board[6]!="-":
            winner=board[6]
            return True
def checkraw(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner= board[2]
        return True
def checkdiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[2]
        return True
def checktie(board):
    global gamerunning
    if"-" not in board:
        printboard(board)
        print("oops tie!")
        gamerunning=False
        
def checkwin():
    if checkdiagonal(board) or checkhorizontle(board) or checkraw(board):
        print(f"the winer is{winner}")
    
    # switch plyaers
def switchplayer():
    global currentplayer
    if currentplayer=="x":
        currentplayer="0"
        
    else:
        currentplayer="x"
 
#check win or tie agian
def computer(board):
    while currentplayer=="0":
        position =random.randint(0,8)
        if board[position]=="-":
            board[position]= "0"
            switchplayer()
    
while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)
    
    
     