from chess_board import ChessBoard
from chess_figure import ChessFigure, Rook, Knight, Bishop, Queen, King, Pawn
from position import Position


class Game:

    whiteRook1 = Rook('White', Position('A', 1))
    whiteRook2 = Rook('White', Position('H', 1))
    whiteKnight1 = Knight('White', Position('B', 1))
    whiteKnight2 = Knight('White', Position('G', 1))
    whiteBishop1 = Bishop('White', Position('C', 1))
    whiteBishop2 = Bishop('White', Position('F', 1))
    whiteQueen = Queen('White', Position('D', 1))
    whiteKing = King('White', Position('E', 1))
    whitePawn = Pawn('White', Position('A', 2))
    blackRook1 = Rook('Black', Position('A', 8))
    blackRook2 = Rook('Black', Position('H', 8))
    blackKnight1 = Knight('Black', Position('B', 8))
    blackKnight2 = Knight('Black', Position('G', 8))
    blackBishop1 = Bishop('Black', Position('C', 8))
    blackBishop2 = Bishop('Black', Position('F', 8))
    blackQueen = Queen('Black', Position('D', 8))
    blackKing = King('Black', Position('E', 8))
    BlackPawn = Pawn('Black', Position('A', 7))

    def __init__(self):
        self.board = ChessBoard()


