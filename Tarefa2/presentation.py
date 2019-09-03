def present(tile):
    for i in range(len(tile.positions)):
        print(tile.positions[i], "\t", end='')
        if i % 9 - 8 == 0:
            print()
    print()


def print_tiles_list(tiles):
    for i in range(len(tiles)):
        print(i, end='\t')
    print()
