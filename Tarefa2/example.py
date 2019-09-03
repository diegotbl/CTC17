import Tarefa2.movement as mvmt
from Tarefa2.tile import Tile


tile = Tile()


def example1():
    return mvmt.move_and_update(tile, 0)


def example2():
    a = list(range(1, 60)) + [0] + list(range(61, 69)) + [60, 71, 79] + list(range(72, 78)) + [69, 78, 70, 80]
    tile.set_positions(a)
    return tile


def example3():         # very hard
    a = [1,  2,  3,  4,  5,  6,  7,  8,  9,
         10, 11, 12, 13, 14, 15, 16, 17, 18,
         19, 20, 21, 22, 23, 24, 25, 26, 27,
         28, 29, 30, 31, 32, 33, 34, 35, 36,
         37, 38, 39, 40, 41, 42, 43, 44, 45,
         46, 47, 48, 58, 50, 51, 52, 53, 54,
         55, 56, 57, 59, 49, 60, 61, 62, 63,
         64, 65, 66, 67, 68, 69, 70, 71, 72,
         73, 74, 75, 76, 77, 78, 79, 80, 0]
    tile.set_positions(a)
    return tile


def example4():
    a = [1,  2,  3,  4,  5,  6,  7,  8,  9,
         10, 11, 12, 13, 14, 15, 16, 17, 18,
         19, 20, 21, 22, 23, 24, 25, 26, 27,
         28, 29, 30, 31, 32, 33, 34, 35, 36,
         37, 38, 39, 40, 41, 42, 43, 44, 45,
         46, 47, 48, 49, 50, 51, 52, 53, 54,
         55, 56, 57, 58, 59, 60, 70, 61, 63,
         64, 65, 66, 67, 68, 69, 62, 71, 72,
         73, 74, 75, 76, 77, 78, 79, 80, 0]
    tile.set_positions(a)
    return tile


def example5():
    a = [1,  2,  3,  4,  5,  6,  7,  8,  9,
         10, 11, 12, 13, 14, 15, 16, 17, 18,
         19, 20, 21, 22, 23, 24, 25, 26, 27,
         28, 29, 30, 31, 32, 33, 34, 35, 36,
         37, 38, 39, 40, 41, 42, 52, 43, 45,
         46, 47, 48, 49, 50, 51, 44, 53, 54,
         55, 56, 57, 58, 59, 60, 61, 62, 63,
         64, 65, 66, 67, 68, 69, 70, 71, 72,
         73, 74, 75, 76, 77, 78, 79, 80, 0]
    tile.set_positions(a)
    return tile


def example6():
    a = [10, 44, 27, 28, 61, 8, 14, 17, 0,
         22, 6, 16, 43, 48, 51, 36, 2, 68,
         24, 38, 37, 45, 18, 41, 70, 34, 46,
         55, 4, 1, 30, 50, 58, 32, 12, 9,
         3, 23, 60, 56, 40, 15, 72, 54, 20,
         7, 25, 11, 47, 5, 74, 29, 35, 26,
         52, 57, 73, 65, 49, 42, 77, 78, 21,
         31, 67, 13, 53, 62, 66, 80, 33, 69,
         39, 75, 64, 19, 59, 76, 63, 79, 71]
    tile.set_positions(a)
    return tile


def example7(n):
    """
    Generates a random board. n is the number of random moves form initial position. If n == 0, the number of moves
    will be randomly chosen from 10 to 100
    """
    return mvmt.randomize(tile, n)
