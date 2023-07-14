from display.board import Board
from logic.gameplay import safe_move, check_winner
import os

class TicTacToe:
    def __init__(self):
        self.__board = Board()
        self.__turns = 9
        self.__turn = "X"
    
    def start(self):
        while self.__turns > 0:
            print(f"Player {self.__turn}'s turn:")
            self.__board.show()
            inp = input("Enter the row and column of your move (e.g. 1 1): ").split(" ")
            if not safe_move(self.__turn, self.__board.grid, inp):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Enter a valid move: ")
                continue
            won = check_winner(self.__turn, self.__board.grid)
            
            if won[0]:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.__board.show()
                print(f"Player {won[1]} won the game with a move on {won[3]} {won[2]}")
                return

            self.__turns -= 1
            self.__turn = "O" if self.__turn == "X" else "X"

            os.system('cls' if os.name == 'nt' else 'clear')
        print("Nobody won the game. Its a draw !!")

tic_tac_toe = TicTacToe()
tic_tac_toe.start()