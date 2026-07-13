def display_board(board):
    """Displays the current state of the Tic-Tac-Toe board."""
    # Print the 1D list in rows of 3
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")

def is_winner(board, player):
    """Checks if a player has won."""
    win_conditions = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)
    )
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    """Checks if all cells are occupied."""
    return all(cell != ' ' for cell in board)

def get_player_move(board):
    """Gets a valid move from the current player."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

def play_tic_tac_toe():
    """Main function to play the Tic-Tac-Toe game."""
    board = [' '] * 9
    current_player = 'X'
    
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn.")
        move = get_player_move(board)
        board[move] = current_player
        
        if is_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
            
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break
            
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_tic_tac_toe()