import math


class Tile:
    def __init__(self):
        self.positions = list(range(1, 81))         # creation of initial board. It will be randomly modified later
        self.positions.append(0)
        self.parent = -1
        self.f = -1
        self.g = -1
        self.h = self.manhattan()
        self.expanded = False

    def check_correctness(self):                    # verifies if h is 0
        if self.h == 0:
            return True
        else:
            return False

    def set_positions(self, pos):
        self.positions = pos

    def manhattan(self):
        m = 0

        for i in range(1, len(self.positions)):
            idx = self.positions.index(i)
            # finding current position of i in matrix
            x1, y1 = index_conversion(idx)

            # finding where it should be
            x2, y2 = index_conversion(i - 1)

            m = m + abs(x2 - x1) + abs(y2 - y1)

        idx = self.positions.index(0)
        x1, y1 = index_conversion(idx)
        x2 = 8
        y2 = 8

        m = m + abs(x2 - x1) + abs(y2 - y1)

        return m

    def update_h(self):
        self.h = self.manhattan()
        self.f = self.g + self.h

    def update_g(self):
        self.g = self.g + 1
        self.f = self.g + self.h


def index_conversion(idx):
    """
    Converts list index to matrix (9x9) index.
    Example: index_conversion(0) -> (0, 0)
             index_conversion(50) -> (5, 5)
    """
    x1 = idx % 9
    y1 = math.floor(idx / 9)

    return x1, y1

