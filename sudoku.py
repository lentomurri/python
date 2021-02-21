#create empty row to store numbers. NO NEED TO CONVERT
def sudokuNow():
    sudoku = []
    # insert 9 time the rows. Check everytime if the row is made of numbers. Remove spaces, Try/except
    for i in range(10):
        row = input(" Enter 9 numbers of the row > ").replace(" ","")
        if len(row) != 9:
            return "Please enter a 9-numbers row"
        try:
            row_check = int(row)
        except:
            return "Please enter a valid row"
        sudoku.append(row)
    #row check
    for row in sudoku:
        for digit in row:
            if row.count(digit) > 1:
                return f"Mistake in {sudoku[sudoku.index(row)]}: {digit} repeated {row.count(digit)} times"
    #check column
    for i in range(9):
        col = []
        for j in range(9):
            if sudoku[j][i] not in col:
                col.append(sudoku[j][i])
            else:
                return f"Mistake in {sudoku[j]}: {sudoku[j][i]} repeated in column {i +1}"
    return "Yes"
    
    

print(sudokuNow())

