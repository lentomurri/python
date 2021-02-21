import random

# SESSION WITH BOARD AND POSITIONS TO UPDATE
positions = [1,2,3,4,5,6,7,8,9]
win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
moves = 0
# END SESSION

def display_board():
    top = "+-----+-----+-----+"
    side = "|     |     |     |"
    board = f"""
{top}
{side}
|  {positions[0]}  |  {positions[1]}  |  {positions[2]}  |
{side}
{top}
{side}
|  {positions[3]}  |  {positions[4]}  |  {positions[5]}  |
{side}
{top}
{side}
|  {positions[6]}  |  {positions[7]}  |  {positions[8]}  |
{side}
{top}
"""
    print(board)


def enter_move():
    user = int(input("Enter your number from 1 to 9 > "))
    while True:
        if user not in positions:
            make_list_of_free_fields()
        else:
            ind = positions.index(user)
            positions[ind] = "O"
            break

def make_list_of_free_fields():
    print("Available Positions: ")
    for i in positions:
        if not i == "O" or not i=="X":
            print(i, end=" ")

def win_move():
    for i in range(0,9):
        for j in range(0,3):
            counterO = 0
            counterX = 0
            if counterO == 3:
                return "Player wins!"
            if counterX == 3:
                return "Computer wins!"
            if win[i][j] == "O":
                counterO += 1
            elif win[i][j] == "X":
                counterX +=1
    return "None won! Keep going!"


def victory_for():
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
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
    return "None won! Keep going!"

def draw_move():
    # The function draws the computer's move and updates the board.
    while True:
        global moves
        comp = random.randint(1,9)
        if comp in positions:
            ind = positions.index(comp)
            positions[ind] = "X"
            moves += 1
            break

while True:
    display_board()
    make_list_of_free_fields()
    enter_move()
    display_board()
    if moves == 9:
        print("It's a tie!")
        break
    check = victory_for()
    if check != "None won! Keep going!":
        print(check)
        break
    draw_move()
    display_board()