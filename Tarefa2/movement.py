import random


def move(tile, direction):
    """
    :param tile: object tile to be updated
    :param direction: direction to move the tile (0: up, 1: right, 2: down, 3: left)
    :return: modified tile object
    """
    if can_move(tile, direction) is False:
        # print("impossible move")
        return tile

    # print("Movement: ", end='')
    # if direction == 0:
    #     print("up")
    # if direction == 1:
    #     print("right")
    # if direction == 2:
    #     print("down")
    # if direction == 3:
    #     print("left")

    idx = tile.positions.index(0)

    if direction == 0:          # move tile up
        aux = tile.positions[idx]
        tile.positions[idx] = tile.positions[idx-9]
        tile.positions[idx-9] = aux
    elif direction == 1:        # move tile to the right
        aux = tile.positions[idx]
        tile.positions[idx] = tile.positions[idx + 1]
        tile.positions[idx + 1] = aux
    elif direction == 2:        # move tile down
        aux = tile.positions[idx]
        tile.positions[idx] = tile.positions[idx + 9]
        tile.positions[idx + 9] = aux
    elif direction == 3:        # move tile to the left
        aux = tile.positions[idx]
        tile.positions[idx] = tile.positions[idx - 1]
        tile.positions[idx - 1] = aux

    return tile


def move_and_update(tile, direction):
    move(tile, direction)
    tile.update_h()

    return tile


def can_move(tile, direction):
    """ Checks if movement is possible or not """
    idx = tile.positions.index(0)

    # edge elements
    if idx == 0 and (direction == 0 or direction == 3):
        return False            # impossible move
    elif idx == 8 and (direction == 0 or direction == 1):
        return False            # impossible move
    elif idx == 72 and (direction == 2 or direction == 3):
        return False            # impossible move
    elif idx == 80 and (direction == 1 or direction == 2):
        return False            # impossible move

    # border elements
    elif idx in range(1, 8) and direction == 0:         # top border
        return False            # impossible move
    elif idx in range(17, 72, 9) and direction == 1:    # right border
        return False            # impossible move
    elif idx in range(73, 80) and direction == 2:       # bottom border
        return False            # impossible move
    elif idx in range(9, 64, 9) and direction == 3:     # left border
        return False            # impossible move

    else:
        return True


def randomize(tile):
    """ Generates random moves """
    number_of_moves = random.randrange(1000, 5001, 1000)  # random.randrange(10000, 50001, 10000)
    print(number_of_moves)
    for i in range(number_of_moves):
        random_direction = random.randrange(0, 4)
        tile = move(tile, random_direction)

    tile.update_h()

    return tile
