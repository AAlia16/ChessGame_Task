from position import Position
from chess_board import ChessBoard


class ChessFigure():

    def __init__(self, color, title, position: Position):
        self.fig_color = color
        self.fig_title = title
        self.fig_position = position

    def move(self, new_position: Position):
        ChessBoard()
        if new_position.x in ChessBoard.x_positions and new_position.y in ChessBoard.y_positions:
            self.fig_position = new_position.get_position()
        else:
            raise ValueError("Position not valid! Please insert a valid position in the board.")


class Rook(ChessFigure):

    def __init__(self, color, position: Position):
        super().__init__(color, Rook.__name__, position.get_position())

    def move(self, position):
        super().move(position)

    def beat(self, is_beaten: bool):
        self.beaten = is_beaten


class Knight(ChessFigure):
    def __init__(self, color, position: Position):
        super().__init__(color, Knight.__name__, position.get_position())

    def move(self, position):
        super().move(position)

    def beat(self, is_beaten: bool):
        self.beaten = is_beaten


class Bishop(ChessFigure):
    def __init__(self, color, position: Position):
        super().__init__(color, Bishop.__name__, position.get_position())

    def move(self, position):
        super().move(position)

    def beat(self, is_beaten: bool):
        self.beaten = is_beaten


class Queen(ChessFigure):
    def __init__(self, color, position: Position):
        super().__init__(color, Queen.__name__, position.get_position())

    def move(self, position):
        super().move(position)

    def beat(self, is_beaten: bool):
        self.beaten = is_beaten


class King(ChessFigure):
    def __init__(self, color, position: Position):
        super().__init__(color, King.__name__, position.get_position())
        self.castling_done = False
        self.side_of_board = 'right'

    def move(self, position):
        super().move(position)

    def beat(self, is_beaten: bool):
        self.beaten = is_beaten


class Pawn(ChessFigure):
    def __init__(self, color, position: Position):
        super().__init__(color, Pawn.__name__, position.get_position())

    def move(self, position):
        super().move(position)

    def beat(self, is_beaten: bool):
        self.beaten = is_beaten


