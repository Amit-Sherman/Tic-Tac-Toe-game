# definding the board, position list and empty
board = "   |   |   \n" + \
        "___|___|___\n" + \
        "   |   |   \n" + \
        "___|___|___\n" + \
        "   |   |   \n" + \
        "   |   |   " # creating the board
empty = ' ' # I will later use it to check if the spot is empty
position_list = [-10,-6,-2,25,29,33,1,5,9] # the position of the places you can put a symbol in

# creating a function which gets a user symbol and position and returning the board after edit
def player_turn(symbol, position): # getting the user symbol and positon
    global board
    if board[position_list[position - 1]] == empty: #cheking if the spot is empty
        if position <= 9 and position >= 1: #cheking if the postion is valid
            if symbol == 'o' or symbol == 'x' or symbol == 'X' or symbol == 'O': #cheking if the symbol is valid
                board = board[:position_list[position - 1]] + symbol + board[position_list[position - 1] + 1:] #putting the symbol in the position the user asked for
                return board
            else:
                print("The symbol is invalid")
                return board
        else:
            print("The position is invalid")
            return board
    else:
        print("This spot is already full...")
        return board

# This is a functinon which check for a win condition by looking for groups of 3 x's or 3 o's
def win_condition(board): #checking if the board has a win condition
    rows = [board[-10:-1], board[25:34], board[1:10]]
    columns = [[board[-10], board[25], board[1]], [board[-6], board[29], board[5]], [board[-2], board[33], board[9]]]
    diagonals = [[board[-10], board[29], board[9]], [board[-2], board[29], board[1]]]
    for row in rows:
        if looking_for_three(row) == True:
            return True
    for column in columns:
        if looking_for_three(column) == True:
            return True
    for diagonal in diagonals:
        if looking_for_three(diagonal) == True:
            return True

# this is a function which check if a list have 3 x's or 3 o's
def looking_for_three(list_name):
    total_xs = 0
    total_os = 0
    for i in list_name:
        if i == "x" or i == "X":
            total_xs += 1
            if total_xs == 3:
                return True
        elif i == "o" or i == "O":
            total_os += 1
            if total_os == 3:
                return True
    return False

previous_pick = 0
play_again = True
while play_again == True:
    print(board)
    symbol = str(input("Who would you like to start, o/x:"))
    if symbol == 'o' or symbol == 'O':
        previous_pick = 0
    elif symbol == 'x' or symbol == 'X':
        previous_pick = 1
    for i in range(9):
        print(board)
        if previous_pick == 1:
            symbol = 'x'
            position = int(input("Enter The Position Of x:"))
            previous_pick = 0
        elif previous_pick == 0:
            symbol = 'o'
            position = int(input("Enter The Position Of o:"))
            previous_pick = 1
        if win_condition(player_turn(symbol, position)) == True:
            print(player_turn(symbol, position))
            print("Well done!, I was a fun game!!")
            want_to_play_again = str(input("Do You Want To Play Again? Y/N:"))
            if want_to_play_again == 'y' or want_to_play_again == 'Y':
                print("Your a beast!")
                board = "   |   |   \n" + \
                        "___|___|___\n" + \
                        "   |   |   \n" + \
                        "___|___|___\n" + \
                        "   |   |   \n" + \
                        "   |   |   "
                break
            elif want_to_play_again == 'n' or want_to_play_again == 'N':
                print("That was fun :), cya!")
                break
    break