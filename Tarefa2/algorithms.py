import Tarefa2.presentation as p
import Tarefa2.movement as mvmt
import copy


def greedy(tile):
    """ Solves problem using greedy algorithm. """
    expanded_tiles = [tile]
    current_tile = 0
    cont = 0
    list_expanded_tiles_positions = []
    print("-------- Starting Greedy ---------\n..................................")
    while not expanded_tiles[current_tile].check_correctness():
        # print("\n\nList of boards on graph: ")
        # for i in range(len(expanded_tiles)):
        #     print("expanded_tiles ", i, ". Manhattan: ", expanded_tiles[i].h, ". Expanded: ", expanded_tiles[i].expanded)
        #     p.present(expanded_tiles[i])
        #     print()
        # print("\n\n")
        # print("manhattan current: ", expanded_tiles[current_tile].h, ". Id:", current_tile, "Pai: ", expanded_tiles[current_tile].parent)
        # p.present(expanded_tiles[current_tile])
        #p.present(expanded_tiles[current_tile])
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
    print("Answer found")
    print("------------ Traceback -----------")
    print("The following moves solve the problem: ")
    cost = backtrack(expanded_tiles, current_tile)
    return cost


def a_star(tile):
    """ Solves problem using greedy algorithm. Prints each step. """
    expanded_tiles = [tile]
    current_tile = 0
    cont = 0
    list_expanded_tiles_positions = []
    print("-------- Starting A-star ---------\n..................................")
    while not expanded_tiles[current_tile].check_correctness():
        # print("f current: ", expanded_tiles[current_tile].f, ". Id:", current_tile, "Pai: ", expanded_tiles[current_tile].parent)
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
    print("Answer found")
    print("------------ Traceback -----------")
    print("The following moves solve the problem: ")
    cost = backtrack(expanded_tiles, current_tile)
    return cost


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
            # print("Id: ", len(expanded_tiles)-1, "Manhattan aux_tile: ", aux_tile.h)

    return expanded_tiles


def backtrack(expanded_tiles, current_tile):
    path = [expanded_tiles[current_tile]]

    while path[-1].parent != -1:
        path.append(expanded_tiles[path[-1].parent])

    for i in range(len(path)-1, -1, -1):
        p.present(path[i])

    return len(path)-1
