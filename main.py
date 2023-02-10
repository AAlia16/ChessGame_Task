from game import Game
from position import Position
from chess_figure import ChessFigure, Rook, Knight, Bishop, Queen, King, Pawn

chessGame = Game()
print('Black rook 1 original position:')
print(Game.blackRook1.fig_position)
newPos = Position('A', 4)
Game.blackRook1.move(newPos)
print('Black rook new position:')
print(Game.blackRook1.fig_position)

print('White Bishop 1 original position:')
print(Game.whiteBishop1.fig_position)
newPos = Position('A', 2)
Game.whiteBishop1.move(newPos)
print('White Bishop 1 new position:')
print(Game.whiteBishop1.fig_position)

print('White Knight 1 original position:')
print(Game.whiteKnight1.fig_position)
newPos = Position('A', 2)
Game.whiteKnight1.move(newPos)
print('White Knight 1 new position:')
print(Game.whiteKnight1.fig_position)

print('Black King original position:')
print(Game.blackKing.fig_position)
newPos = Position('E', 6)
Game.blackKing.move(newPos)
print('Black King new position:')
print(Game.blackKing.fig_position)
Game.blackKing.castling_done = True
if Game.blackKing.castling_done:
    print("Castling was done on the " + Game.blackKing.side_of_board)


print('Black Queen original position:')
print(Game.blackQueen.fig_position)
newPos = Position('A', 5)
Game.blackQueen.move(newPos)
print('Black Queen new position:')
print(Game.blackQueen.fig_position)

print('White Pawn original position:')
print(Game.whitePawn.fig_position)
newPos = Position('A', 3)
Game.whitePawn.move(newPos)
print('White Pawn new position:')
print(Game.whitePawn.fig_position)