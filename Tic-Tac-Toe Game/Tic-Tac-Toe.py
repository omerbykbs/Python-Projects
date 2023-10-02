from IPython.display import clear_output

line1 = ['_', '_', '_']
line2 = ['_', '_', '_']
line3 = ['_', '_', '_']
lines = [line1, line2, line3]
def display_game(lines):
    game_board = f"{'|'.join(lines[0])}\n{'|'.join(lines[1])}\n{'|'.join(lines[2])}\n"
    return print(game_board)


def is_game_on(player):
    if win(player) == True:
        return 'WIN'
    elif sum([len(x) for x in lines if '_' in x]) == 0:
        return 'DRAW'
    else:
        return True

def win(player):
    if line1[0] == line2[0] == line3[0] == player or line1[1] == line2[1] == line3[1] == player or line1[2] == line2[2] == line3[2] == player or line1[0] == line2[1] == line3[2] == player or line1[2] == line2[1] == line3[0] == player:
        return True
    elif len([o for o in line1 if o == player]) == 3 or len([o for o in line2 if o == player]) == 3 or len(
            [o for o in line3 if o == player]) == 3:
        return True
    else:
        return False

def player_move(player):
    r = 'a'
    c = 'b'
    row = 0
    column = 0
    taken = False

    while r.isdigit() == False or c.isdigit() == False or (row not in [1, 2, 3]) or (column not in [1, 2, 3]) or taken:
        r, c = input(f"Enter the row (1,2,3) and the column (1,2,3) for your move ({playing}): ").split()
        
        if r.isdigit() == False or c.isdigit() == False:
            if r.isdigit() == c.isdigit() == False:
                clear_output()
                display_game(lines)
                print("Not valid row and column! Please enter a number (1,2,3) for row and column")
            elif r.isdigit() == False:
                clear_output()
                display_game(lines)
                print("Not valid row! Please enter a number (1,2,3) for row")
            elif c.isdigit() == False:
                clear_output()
                display_game(lines)
                print("Not valid column! Please enter a number (1,2,3) for column")
            continue
        else:
            row = int(r)           
            column = int(c)    
            if (row not in [1, 2, 3]) or (column not in [1, 2, 3]):
                if row not in [1, 2, 3] and column not in [1, 2, 3]:
                    clear_output()
                    display_game(lines)
                    print("Not valid row and column! Please enter a valid row (1,2,3) and a valid column (1,2,3)")
                elif row not in [1, 2, 3]:
                    clear_output()
                    display_game(lines)
                    print("Not valid row! Please enter a valid row (1,2,3)")
                elif column not in [1, 2, 3]:
                    clear_output()
                    display_game(lines)
                    print("Not valid column! Please enter a valid column (1,2,3)")
            else:
                if lines[row - 1][column - 1] != '_':
                    clear_output()
                    display_game(lines)
                    print("This position is already chosen. Choose another position")
                    taken = True
                else:
                    taken = False
    
    
    move = [row, column]        
    return (update_board(player, move, lines))


def update_board(player, move, lines):
    lines[move[0] - 1][move[1] - 1] = player
    return lines

def game_on_choice():
    choice = 'wrong'
    while choice not in ['Yes', 'No']:
        choice = input("Would you like to keep playing? Yes or No: ")
        if choice not in ['Yes', 'No']:
            print("Sorry, I didn't understand. Please make sure to choose Yes or No.")
    if choice == 'Yes':
        return True
    else:
        return False


game_on = True
player1 = 'X'
player2 = 'O'
playing = player1
winner = ''
    
while game_on:
    clear_output()
    if sum([lines[0].count('_'),lines[1].count('_'),lines[2].count('_')]) == 9:
        print("Welcome to TicTacToe Game!\nPlayer 1 plays as 'X' and Player 2 plays as 'O'.\nPlayer 1 starts game.\nHave fun! :)")
    display_game(lines)

    # player move
    lines = player_move(playing)

    if is_game_on(playing) == True:
        if playing == player1:
            playing = player2
        else:
            playing = player1
    else:
        if is_game_on(playing) == 'WIN':
            clear_output()
            if playing == 'X':
                winner = 'Player 1'
            else:
                winner = 'Player 2'
            print(f"{winner} has WON!")
            display_game(lines)
        if is_game_on(playing) == 'DRAW': 
            clear_output()
            print("DRAW!")
            display_game(lines)
        game_on = game_on_choice()
        if game_on:
            line1 = ['_', '_', '_']
            line2 = ['_', '_', '_']
            line3 = ['_', '_', '_']
            lines = [line1, line2, line3]
