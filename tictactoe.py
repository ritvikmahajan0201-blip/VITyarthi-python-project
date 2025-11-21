#!/usr/bin/env python3
"""
Tic-Tac-Toe (Console)
---------------------
Features:
- Human vs Human
- Human vs AI (Easy / Medium / Hard)
- Clean prompts and input validation
- Replay option
- Minimax AI with pruning (for Hard), shallow lookahead (for Medium), random (for Easy)

Run:
    python tictactoe.py
"""

import random
from typing import List, Optional, Tuple

Board = List[str]  # 9-length list of 'X', 'O', or ' '


def print_board(board: Board) -> None:
    """Pretty-print the 3x3 board."""
    cells = [c if c != ' ' else str(i+1) for i, c in enumerate(board)]
    print("\n")
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print("\n")


def winning_lines() -> List[Tuple[int, int, int]]:
    return [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]


def check_winner(board: Board) -> Optional[str]:
    """Return 'X' or 'O' if someone wins, 'D' for draw, or None if the game continues."""
    for a, b, c in winning_lines():
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    if ' ' not in board:
        return 'D'
    return None


def available_moves(board: Board) -> List[int]:
    return [i for i, c in enumerate(board) if c == ' ']


def make_move(board: Board, idx: int, player: str) -> Board:
    new_board = board[:]
    new_board[idx] = player
    return new_board


def opponent(player: str) -> str:
    return 'O' if player == 'X' else 'X'


# ---------------------
# Minimax with pruning
# ---------------------
def minimax(board: Board, player: str, ai: str, alpha: int, beta: int, depth: int) -> Tuple[int, Optional[int]]:
    """
    Return (score, move). Score perspective is for AI player.
    Terminal scores:
        win (ai)   => +10 - depth
        win (opp)  => -10 + depth
        draw       => 0
    """
    result = check_winner(board)
    if result is not None:
        if result == ai:
            return 10 - depth, None
        elif result == opponent(ai):
            return depth - 10, None
        else:
            return 0, None

    if player == ai:
        best_score, best_move = -10**9, None
        for m in available_moves(board):
            score, _ = minimax(make_move(board, m, player), opponent(player), ai, alpha, beta, depth + 1)
            if score > best_score:
                best_score, best_move = score, m
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # beta cut-off
        return best_score, best_move
    else:
        best_score, best_move = 10**9, None
        for m in available_moves(board):
            score, _ = minimax(make_move(board, m, player), opponent(player), ai, alpha, beta, depth + 1)
            if score < best_score:
                best_score, best_move = score, m
            beta = min(beta, best_score)
            if beta <= alpha:
                break  # alpha cut-off
        return best_score, best_move


def ai_move_easy(board: Board, ai: str) -> int:
    """Random legal move."""
    return random.choice(available_moves(board))


def ai_move_medium(board: Board, ai: str) -> int:
    """
    Heuristic:
    1) Win if possible
    2) Block opponent win if possible
    3) Center, then corners, then random
    """
    # 1) Try to win
    for m in available_moves(board):
        if check_winner(make_move(board, m, ai)) == ai:
            return m
    # 2) Block
    opp = opponent(ai)
    for m in available_moves(board):
        if check_winner(make_move(board, m, opp)) == opp:
            return m
    # 3) Prefer center
    if 4 in available_moves(board):
        return 4
    # 4) Prefer corners
    corners = [i for i in [0, 2, 6, 8] if i in available_moves(board)]
    if corners:
        return random.choice(corners)
    # 5) Else random
    return ai_move_easy(board, ai)


def ai_move_hard(board: Board, ai: str) -> int:
    """Optimal play via minimax + alpha-beta pruning."""
    _, move = minimax(board, ai, ai, -10**9, 10**9, 0)
    assert move is not None  # there must be a move if game isn't terminal
    return move


def ask_int(prompt: str, valid: List[int]) -> int:
    while True:
        try:
            val = int(input(prompt).strip())
            if val in valid:
                return val
            print(f"Please enter one of {valid}.")
        except ValueError:
            print("Please enter a valid integer.")


def choose_game_mode() -> Tuple[str, Optional[str]]:
    print("Choose game mode:")
    print("1) Human vs Human")
    print("2) Human vs AI")
    mode = ask_int("Enter 1 or 2: ", [1, 2])
    if mode == 1:
        return "HvH", None
    else:
        print("Choose AI difficulty:")
        print("1) Easy")
        print("2) Medium")
        print("3) Hard")
        diff = ask_int("Enter 1/2/3: ", [1, 2, 3])
        if diff == 1:
            return "HvAI", "Easy"
        elif diff == 2:
            return "HvAI", "Medium"
        else:
            return "HvAI", "Hard"


def choose_symbols() -> Tuple[str, str]:
    print("Choose your symbol:")
    print("1) X (goes first)")
    print("2) O (goes second)")
    choice = ask_int("Enter 1 or 2: ", [1, 2])
    if choice == 1:
        return 'X', 'O'
    else:
        return 'O', 'X'


def get_ai_move(board: Board, ai: str, difficulty: str) -> int:
    if difficulty == "Easy":
        return ai_move_easy(board, ai)
    elif difficulty == "Medium":
        return ai_move_medium(board, ai)
    else:
        return ai_move_hard(board, ai)


def human_turn(board: Board, player: str) -> int:
    valid = [i + 1 for i in available_moves(board)]
    return ask_int(f"Player {player}, choose your move {valid}: ", valid) - 1


def play_once(mode: str, difficulty: Optional[str]) -> None:
    """Play one match and print result."""
    board: Board = [' '] * 9

    if mode == "HvH":
        current = 'X'
        while True:
            print_board(board)
            move = human_turn(board, current)
            board = make_move(board, move, current)
            result = check_winner(board)
            if result:
                print_board(board)
                if result == 'D':
                    print("It's a draw!")
                else:
                    print(f"Player {result} wins!")
                break
            current = opponent(current)

    elif mode == "HvAI":
        human, ai = choose_symbols()
        current = 'X'
        while True:
            print_board(board)
            if current == human:
                move = human_turn(board, current)
            else:
                print(f"AI ({difficulty}) is thinking...")
                move = get_ai_move(board, ai, difficulty)  # type: ignore
            board = make_move(board, move, current)
            result = check_winner(board)
            if result:
                print_board(board)
                if result == 'D':
                    print("It's a draw!")
                elif result == human:
                    print("You win! 🎉")
                else:
                    print("AI wins! 🤖")
                break
            current = opponent(current)


def main() -> None:
    print("=== Tic-Tac-Toe ===")
    while True:
        mode, diff = choose_game_mode()
        play_once(mode, diff)
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
