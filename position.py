class Position:
    def __init__(self, x_pos: str, y_pos: int):
        self.x = x_pos
        self.y = y_pos

    def get_position(self):
        return self.x + str(self.y)

