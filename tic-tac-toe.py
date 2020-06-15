# PLAYER SELECTION SECTION

import random

player1 = ""
cpu = ""
startGame = False

while True:
    options = ["X", "O"]
    result = random.randint(0,1)
    player1 = options[result]
    if player1 == "X":
        print("Welcome, Player 1! You'll be the " + player1)
        cpu = "O"
    elif player1 == "O":
        print("Welcome, Player 1! You'll be the " + player1)
        cpu = "X"
    startGame = True
    break
    

# BOARD FUNCTION SECTION

board = {
    "TL": " ", "TM" : " ", "TR" : " ",
    "ML": " ", "MM" : " ", "MR" : " ",
    "BL": " ", "BM" : " ", "BR" : " "
}

def boarding(currentBoard):
    print(currentBoard["TL"] + "|" + currentBoard["TM"] + "|" + currentBoard["TR"])
    print("-+-+-")
    print(currentBoard["ML"] + "|" + currentBoard["MM"] + "|" + currentBoard["MR"])
    print("-+-+-")
    print(currentBoard["BL"] + "|" + currentBoard["BM"] + "|" + currentBoard["BR"])

# ------MOVE SECTION-------

#CPU SECTION

def cpuMove():
    if startGame == True:
        corners = ["TL", "TR", "BL", "BR"]
        others = ["TM", "ML", "MR", "BM"]
        # first move: center
        if board["MM"] == " ":
            board["MM"] = cpu
            print(boarding(board))
        else:
            for i in range(len(corners)):
                if board[corners[i]] == " ":
                    board[corners[i]] = cpu
                    print(boarding(board))
                    return
            for i in range(len(others)):
                if board[others[i]] == " ":
                    board[others[i]] = cpu
                    print(boarding(board))
                    return

#PLAYER 1 SECTION

def playerMove():
    if startGame == True:
        boarding(board)
        choice = input("Please select one of the spaces: \n TL(Top Left), TM (Top Middle),TR (Top Right), ML(Middle Left), MM (Middle Middle),MR (Middle Right), BL(Bottom Left), BM (Bottom Middle),BR (Bottom Right): ")
        choice = choice.upper();   
        if choice not in list(board.keys()):
            print("Please enter one of the available moves.")
            playerMove()
        elif board[choice] == " ":
            board[choice] = player1
            boarding(board)
        else:
            print("Please select an empty space")

# VICTORY CASES
def checkVictory():
    global startGame
    if (board["TL"] == board["TM"] and board["TL"] == board["TR"] and board["TL"] != " "):
        if player1 == board["TL"]:
            print("You Win!")
            startGame = False
        else:
            print("Oh no! You lose!")
            startGame = False

    elif (board["ML"] == board["MM"] and board["ML"] == board["MR"] and board["ML"] != " "):
        if player1 == board["ML"]:
            print("You Win!")
            startGame = False
        else:
            print("Oh no! You lose!")
            startGame = False

    elif (board["BL"] == board["BM"] and board["BL"] == board["BR"] and board["BL"] != " "):
        if player1 == board["BL"]:
            print("You Win!")
            startGame = False
        else:
            print("Oh no! You lose!")
            startGame = False

    elif (board["TL"] == board["MM"] and board["TL"] == board["BR"] and board["TL"] != " "):
        if player1 == board["TL"]:
            print("You Win!")
            startGame = False
        else:
            print("Oh no! You lose!")
            startGame = False

    elif (board["TR"] == board["MM"] and board["TR"] == board["BL"] and board["TR"] != " "):
        if player1 == board["TR"]:
            print("You Win!")
            startGame = False
        else:
            print("Oh no! You lose!")
            startGame = False

    elif (board["TM"] == board["MM"] and board["TM"] == board["BM"] and board["TM"] != " "):
        if player1 == board["TM"]:
            print("You Win!")
            startGame = False
        else:
            print("Oh no! You lose!")
            startGame = False

    elif (board["TL"] == board["ML"] and board["TL"] == board["BL"] and board["TL"] != " "):
        if player1 == board["TL"]:
            print("You Win!")
            startGame = False
        else:
            print("Oh no! You lose!")
            startGame = False

    elif (board["TR"] == board["MR"] and board["TR"] == board["BR"] and board["TR"] != " "):
        if player1 == board["TR"]:
            print("You Win!")
            startGame = False
        else:
            print("Oh no! You lose!")
            startGame = False

#------START GAME TRUE, GAME STARTS-------

def playingGame():
    global startGame
    while startGame == True:
       firstMove = cpuMove
       secondMove = playerMove
       if player1 == "X":
           firstMove = playerMove
           secondMove = cpuMove
       firstMove()
       checkVictory()
       secondMove()
       checkVictory()
    else: 
        while True:
            choice = input("Play again? Please enter Y to replay or N to stop: ")
            choice = choice.upper()
            print(choice)
            if choice != "Y" and choice != "N":
                print("Please enter one of the options")       
                pass
            elif choice == "Y":
                global board
                board = {
    "TL": " ", "TM" : " ", "TR" : " ",
    "ML": " ", "MM" : " ", "MR" : " ",
    "BL": " ", "BM" : " ", "BR" : " "
}
                startGame = True
                playingGame()
            else:
                print("Thanks for playing!")
                break

playingGame()