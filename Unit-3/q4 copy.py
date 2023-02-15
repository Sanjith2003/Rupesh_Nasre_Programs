import tkinter as tk
import tictactoe.logic
import tictactoe.display.text

board = tictactoe.logic.board # shorthand data
show = tictactoe.display.text.show # shorthand function

# Set up GUI
root = tk.Tk()
root.title("Tic Tac Toe")


buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text="", width=3, height=1)
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)


player = "X"
game_over = False


def handle_click(row, col):
    global player, game_over
    if not game_over and board[row][col] == "":
        board[row][col] = player
        buttons[row][col].config(text=player)
        if tictactoe.logic.check_win(board, player):
            show()
            print(f"{player} wins!")
            game_over = True
        elif tictactoe.logic.check_tie(board):
            show()
            print("Tie game!")
            game_over = True
        else:
            player = "O"
            computer_move()


def computer_move():
    global player, game_over
    row, col = tictactoe.logic.get_computer_move(board, player)
    board[row][col] = player
    buttons[row][col].config(text=player)
    if tictactoe.logic.check_win(board, player):
        show()
        print(f"{player} wins!")
        game_over = True
    elif tictactoe.logic.check_tie(board):
        show()
        print("Tie game!")
        game_over = True
    else:
        player = "X"

for row in range(3):
    for col in range(3):
        buttons[row][col].config(command=lambda r=row, c=col: handle_click(r, c))


show()
root.mainloop()
