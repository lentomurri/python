import random

# SESSION WITH BOARD AND POSITIONS TO UPDATE

class Manager():
    #class instances available to be modified
    positions = [1,2,3,4,5,6,7,8,9]
    moves = 0
    win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    #creates board
    def __init__(self):
        top = "+-----+-----+-----+"
        side = "|     |     |     |"
        self.board = f"""
{top}
{side}
|  {Manager.positions[0]}  |  {Manager.positions[1]}  |  {Manager.positions[2]}  |
{side}
{top}
{side}
|  {Manager.positions[3]}  |  {Manager.positions[4]}  |  {Manager.positions[5]}  |
{side}
{top}
{side}
|  {Manager.positions[6]}  |  {Manager.positions[7]}  |  {Manager.positions[8]}  |
{side}
{top}
"""

#PLAYER MOVE

def enter_move(positions):
    # handles user inputs higher than 9 and not-integer
    while True:
        try:
            user = int(input("Enter your number from 1 to 9 > "))
            ind = positions.index(user)
            positions[ind] = "O"
            break
        except ValueError:
            print("Please enter a valid number")

#PRINTS AVAILABLE SPACES

def make_list_of_free_fields(positions):
    print("Available Positions: ")
    for i in positions:
        if type(i) == int:
            print(i, end=" ")

#CHECKS IF PLAYER OR CPU WON

def victory_for(positions, win):
    # The function analyzes the board status compared to the win options
    for i in range(0,8):
        counterO = 0
        counterX = 0
        for j in range(0,3):
            if  positions[win[i][j]]== "O":
                counterO += 1
            elif positions[win[i][j]] == "X":
                counterX +=1
        if counterO == 3:
            return "Player wins!"
        if counterX == 3:
            return "Computer wins!"
    return False

def draw_move(moves, positions):
    # CPU moves randomly and updates the board.
    while True:
        comp = random.randint(1,9)
        if comp in positions:
            ind = positions.index(comp)
            positions[ind] = "X"
            moves += 1
            break

while True:
    #the class variables used to perform the checks 
    board = Manager().board
    positions = Manager().positions
    win = Manager().win
    moves = Manager().moves
    print(board)
    make_list_of_free_fields(positions)
    enter_move(positions)
    print(board)
    if moves == 9:
        print("It's a tie!")
        break
    check = victory_for(positions, win)
    if check:
        print(check)
        break
    draw_move(moves, positions)