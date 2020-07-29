board=["-","-","-",
       "-","-","-",
       "-","-","-"]

game_still_going=True
#who win
winner=None
#turn of player
current_player="X"
def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

def play_game():
    #initail board display
    display_board()
    while game_still_going:
        player_turn(current_player)

        check_if_game_over()

        flip_player()
    if winner=="X" or winner=="O":
        print(winner+" won")
    elif winner==None:
        print("Tie!!")

def player_turn(player):
    print(player+"'s turn")
    position=input("Enter the number from 1 to 9:")

    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
          position=input("Enter the number from 1 to 9:")

        position=int(position)-1
        if board[position]=="-":
            valid=True
        else:
            print("Already occupied")
    board[position]=player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    if row_winner():
        winner=row_winner()
    elif col_winner():
        winner=col_winner()
    elif dgnal_winner():
        winner=dgnal_winner()
    else:
        winner=None

    return
def row_winner():
    global game_still_going
    row_1=board[0]==board[1]==board[2]!="-"
    row_2=board[3]==board[4]==board[5]!="-"
    row_3=board[6]==board[7]==board[8]!="-"
    if row_1 or row_2 or row_3:
        game_still_going=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def col_winner():
  global game_still_going
  col_1=board[0]==board[3]==board[6]!="-"
  col_2=board[1]==board[4]==board[7]!="-"
  col_3=board[2]==board[5]==board[8]!="-"
  if col_1 or col_2 or col_3:
        game_still_going=False
  if col_1:
        return board[0]
  elif col_2:
        return board[1]
  elif col_3:
        return board[2]
  return

def dgnal_winner():
  global game_still_going
  diag_1=board[0]==board[4]==board[8]!="-"
  diag_2=board[6]==board[4]==board[2]!="-"
  if diag_1 or diag_2:
        game_still_going=False
  if diag_1:
        return board[0]
  elif diag_2:
        return board[2]
  return

def check_if_tie():
    global game_still_going
    if "-" not in board:
          game_still_going=False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player="O"
    elif current_player == "O":
        current_player="X"
    return
play_game()

