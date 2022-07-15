from enum import Enum
from typing import List


class GameStatus(Enum):
    EMPTY = 0
    IN_PROGRESS = 1
    X_WIN = 2
    O_WIN = 3
    NOBODY = 4


class CellStatus(Enum):
    EMPTY = 0
    X = 1
    O = 2


class GameUtils:

    @staticmethod
    def transpose_matrix(matrix: List[List[CellStatus]]) -> List[List[CellStatus]]:
        return [[matrix[col][row] for col in range(len(matrix[row]))] for row in range(len(matrix))]

    @staticmethod
    def check_rows(board: List[List[CellStatus]]) -> CellStatus:
        for row in board:
            if len(set(row)) == 1:
                return CellStatus(row[0])
        return CellStatus.EMPTY

    @staticmethod
    def check_diagonals(board: List[List[CellStatus]]) -> CellStatus:
        diagonal_1 = [board[i][i] for i in range(3)]
        diagonal_2 = [board[i][3-i-1] for i in range(3)]
        if len(set(diagonal_1)) == 1 or len(set(diagonal_2)) == 1:
            return CellStatus(board[1][1])
        return CellStatus.EMPTY

    def check_board(self, board: List[List[CellStatus]] = None) -> CellStatus:
        for newBoard in [board, self.transpose_matrix(board)]:
            result = self.check_rows(newBoard)
            if result:
                return result
        return self.check_diagonals(board)

    @staticmethod
    def is_empty(board: List[List[CellStatus]]) -> bool:
        return len(set(sum(board, []))) == 1


class Game:
    board: List[List[CellStatus]]
    game_state: GameStatus = GameStatus.EMPTY

    def __init__(self, board) -> None:
        if not board:
            self.board = [[CellStatus.EMPTY for _ in range(3)] for __ in range(3)]
        else:
            self.board = board

    def check_winner(self) -> None:
        utils = GameUtils()
        winner = utils.check_board(self.board)

        is_empty = utils.is_empty(self.board)
        if is_empty:
            print(f"Game is Empty")
            self.game_state = GameStatus.EMPTY
            return

        if winner != CellStatus.EMPTY:
            # TODO fix bug
            print(f"Winner is {winner}!!")
            self.game_state = GameStatus.X_WIN if winner == CellStatus.X else GameStatus.O_WIN
            return

        print("Nobody win((")
        self.game_state = GameStatus.NOBODY


game = Game(
    [
        [CellStatus.O, CellStatus.X, CellStatus.X],
        [CellStatus.O, CellStatus.X, CellStatus.X],
        [CellStatus.X, CellStatus.X, CellStatus.X]
    ]
)
game.check_winner()
