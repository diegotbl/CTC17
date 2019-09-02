from Tarefa2.tile import Tile
import Tarefa2.presentation as p
import Tarefa2.movement as mvmt
import math
import copy


def greedy(tile):
    """ Solves problem using greedy algorithm. Prints each step. """
    expanded_tiles = [tile]
    current_tile = 0
    cont = 0
    list_expanded_tiles_positions = []
    while not expanded_tiles[current_tile].check_correctness():
        # print("\n\nList of boards on graph: ")
        # for i in range(len(expanded_tiles)):
        #     print("expanded_tiles ", i, ". Manhattan: ", expanded_tiles[i].h, ". Expanded: ", expanded_tiles[i].expanded)
        #     p.present(expanded_tiles[i])
        #     print()
        # print("\n\n")
        print("manhattan current: ", expanded_tiles[current_tile].h, ". Id:", current_tile, "Pai: ", expanded_tiles[current_tile].parent)
<<<<<<< Updated upstream
        # p.present(expanded_tiles[current_tile])
=======
        #p.present(expanded_tiles[current_tile])
>>>>>>> Stashed changes
        expanded_tiles[current_tile].expanded = True
        expanded_tiles = append_neighbors(current_tile, expanded_tiles)
        # for t in range(len(expanded_tiles)):
        #     # Find the first element in expanded_tiles with the same "positions" as current_tile
        #     first_occurrence = next(a for a in expanded_tiles if a.positions == expanded_tiles[current_tile].positions)
        #     if expanded_tiles[t].h < expanded_tiles[current_tile].h or first_occurrence.expanded is True:
        #         if expanded_tiles[t].expanded is False:
        #             current_tile = t

        aux = current_tile
        for i in range(len(expanded_tiles) -1, 1, -1):
            if expanded_tiles[i].expanded is False:
                if expanded_tiles[i].h < expanded_tiles[aux].h or expanded_tiles[aux].expanded is True:
                    if not (expanded_tiles[i].positions in list_expanded_tiles_positions):
                        aux = i
        current_tile = aux
        list_expanded_tiles_positions.append(expanded_tiles[current_tile].positions)

        expanded_tiles[current_tile].update_h()

        cont = cont + 1

    print("---------- End of search ---------")
    print("current_tile: ", current_tile, "Manhattan: ", expanded_tiles[current_tile].h)
    p.present(expanded_tiles[current_tile])


def A_star(tile):
    """ Solves problem using greedy algorithm. Prints each step. """
    expanded_tiles = [tile]
    current_tile = 0
    cont = 0
    list_expanded_tiles_positions = []
    while not expanded_tiles[current_tile].check_correctness():
        print("f current: ", expanded_tiles[current_tile].f, ". Id:", current_tile, "Pai: ", expanded_tiles[current_tile].parent)
        # p.present(expanded_tiles[current_tile])
        expanded_tiles[current_tile].expanded = True
        expanded_tiles = append_neighbors(current_tile, expanded_tiles)

        aux = current_tile
        for i in range(len(expanded_tiles)):
            if expanded_tiles[i].expanded is False:
                if expanded_tiles[i].f < expanded_tiles[aux].f or expanded_tiles[aux].expanded is True:
                    if not (expanded_tiles[i].positions in list_expanded_tiles_positions):
                        aux = i
        current_tile = aux
        list_expanded_tiles_positions.append(expanded_tiles[current_tile].positions)

        expanded_tiles[current_tile].update_h()

        cont = cont + 1

    print("---------- End of search ---------")
    print("current_tile: ", current_tile, "Manhattan: ", expanded_tiles[current_tile].h)
    p.present(expanded_tiles[current_tile])


def append_neighbors(current_tile, expanded_tiles):
    for i in range(4):          # possible moves
        if mvmt.can_move(expanded_tiles[current_tile], i):
            aux_tile = copy.deepcopy(expanded_tiles[current_tile])
            aux_tile.expanded = False
            aux_tile.parent = current_tile
            aux_tile = mvmt.move(aux_tile, i)
            aux_tile.update_h()
            aux_tile.update_g()
            expanded_tiles.append(aux_tile)
<<<<<<< Updated upstream
            # print("Id: ", len(expanded_tiles)-1, "Manhattan aux_tile: ", aux_tile.h)
=======
            #print("Id: ", len(expanded_tiles)-1, "Manhattan aux_tile: ", aux_tile.h)
>>>>>>> Stashed changes

    return expanded_tiles
