import Tarefa2.presentation as p
import Tarefa2.algorithms as algorithms
import Tarefa2.example as example


def main():
    tile = example.example2()   # choose your initial board here

    tile.update_h()
    print("Initial Manhattan distance: ", tile.h)
    print("-------- Initial position --------")
    p.present(tile)
    greedy_cost = algorithms.greedy(tile)
    a_star_cost = algorithms.a_star(tile)
    print("Number of moves using Greedy: ", greedy_cost)
    print("Number of moves using A-star: ", a_star_cost)


if __name__ == "__main__":
    main()
