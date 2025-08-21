# Tic-Tac-Toe with Unbeatable AI using Minimax
import math
board = [' ' for _ in range(9)]
def print_board():
    print()
    for i in range(3):
        print(board[3*i] + " | " + board[3*i+1] + " | " + board[3*i+2])
        if i < 2:
            print("--+---+--")
    print()
def check_winner(b, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for combo in win_combos:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
            return True
    return False
def is_board_full(b):
    return ' ' not in b
def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):
        return 1
    elif check_winner(b, 'X'):
        return -1
    elif is_board_full(b):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score
def best_move():
    move = -1
    best_score = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move
print("Welcome to Tic-Tac-Toe!")
print_board()
while True:
    human_move = int(input("Enter your move (0-8): "))
    if board[human_move] != ' ':
        print("Invalid move! Try again.")
        continue
    board[human_move] = 'X'
    print_board()
    if check_winner(board, 'X'):
        print("You win!")
        break
    elif is_board_full(board):
        print("It's a draw!")
        break
    ai_move = best_move()
    board[ai_move] = 'O'
    print("AI plays at position:", ai_move)
    print_board()
    if check_winner(board, 'O'):
        print("AI wins!")
        break
    elif is_board_full(board):
        print("It's a draw!")
        break
