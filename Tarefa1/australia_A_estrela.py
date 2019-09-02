import copy
from prettytable import PrettyTable

class City:
    def __init__(self, ident, name, x, y, pai, h, g, f, expand ):
        self.ident = ident
        self.name = name
        self.x = x
        self.y = y
        self.expand = expand
        self.pai = pai
        self.h = h
        self.g = g
        self.f = f


def find_city(all_cities, city):
    """
    search for a city in vector
    :param all_cities: list containing all cities objects
           city: city want to find
    :return: city finded
    """
    return next(x for x in all_cities if x.name == city)

def verify_neighbors(all_cities):
    """
    Evaluates neighbors of each city
    :param all_cities: list containing all cities objects
    :return: list of lists containing neighbors id's
    """
    n = len(all_cities)
    # Neighbors of first and second cities (id = 1 and 2). Position 0 and 1 in list neighbors.
    neighbors = [[2, 3], [1, 4]]

    for i in range(2, n-2):
        ident = int(all_cities[i].ident)
        if ident % 2 == 0:
            neighbors.append([ident - 2, ident - 1, ident + 2])
        else:
            neighbors.append([ident - 2, ident + 1, ident + 2])

    neighbors.append([n - 3, n - 2])            # neighbors of city with id n-1 (position n-2 of list)
    if n % 2 == 0:                              # neighbors of city with id n   (position n-1 of list)
        neighbors.append([n - 3, n])
    else:
        neighbors.append([n - 2])

    return neighbors



def insert_neighbors(cities, all_cities, neighbors, actual_city, destiny):
    """
    Inserts all the neighbors of the actual city
    :param all_cities: list containing all cities objects
           cities: list containing all cities already visited
           neighbors: list containing all cities and your neighbors
           actual_city:
           destiny: final city, the goal
    """
    all_cities[int(cities[actual_city].ident)-1].expand = 1
    #for each neighbor for the currenty city
    for i in neighbors[int(cities[actual_city].ident)-1]:
        a = copy.deepcopy(all_cities[i-1])
        # the distance g will be the distance g of the current city plus
        # the distance between the current city and the next city
        a.g = cities[actual_city].g + g_distance(a, cities[actual_city])
        a.h = h_distance(a, destiny[0])
        a.f = a.g + a.h
        a.pai = actual_city
        cities.append(City(a.ident, a.name, a.x, a.y, a.pai, a.h, a.g, a.f, 0))

def g_distance (a,b):
    """
    calculate the real distance between two cities
    :param a: initial city
           b: destination city
    :return distance between two cities
    """
    return 1.1*h_distance(a,b)

def h_distance (a,b):
    """
    calculate estamimate distance between two cities
    :param a: initial city
           b: destination city
    :return distance between two cities
    """
    return ((float(a.x) - float(b.x))**2 + (float(a.y) - float(b.y))**2)**0.5

def a_estrela (cities, all_cities, neighbors, actual_city, destiny):
    """
    Algorithm A*
    :param all_cities: list containing all cities objects
           cities: list containing all cities already visited
           neighbors: list containing all cities and your neighbors
           actual_city:
           destiny: final city, the goal
    :return the next city to visit
    """
    #mark city as visited
    cities[actual_city].expand = 1

    # insert all the neighbors of the current city in the vector cities
    insert_neighbors(cities, all_cities, neighbors, actual_city, destiny)
    n = len(cities)

    # search for the next city to visit, ie, the city with the smallest f
    aux = actual_city
    for j in range(n):
        if cities[j].expand == 0:
            if (cities[j].f < cities[aux].f or cities[aux].expand == 1) and cities[j].ident != cities[0].ident:
                if all_cities[int(cities[j].ident)-1].expand == 0:
                    aux = j
    actual_city = aux

    return actual_city


def greedy(cities, all_cities, neighbors, actual_city, destiny):
    """
    Algorithm Greedy*
    :param all_cities: list containing all cities objects
           cities: list containing all cities already visited
           neighbors: list containing all cities and your neighbors
           actual_city:
           destiny: final city, the goal
    :return the next city to visit
    """
    cities[actual_city].expand = 1

    # insert all the neighbors of the current city in the vector cities
    insert_neighbors(cities, all_cities, neighbors, actual_city, destiny)
    n = len(cities)


    # search for the next city to visit, ie, the city with the smallest h
    aux = actual_city
    for j in range(n):
        if cities[j].expand == 0:
            if (cities[j].h < cities[aux].h or cities[aux].expand == 1) and cities[j].ident != cities[0].ident:
                if all_cities[int(cities[j].ident) - 1].expand == 0:
                    aux = j

    actual_city = aux


    return actual_city

def find_route (cities, actual_city):
    """
    search for the cities that will be part of the route
    :param all_cities: list containing all cities objects
           cities: list containing all cities already visited
    :return list of cities that will be part of the route
    """
    i = cities[actual_city]
    route = []
    route.append(i)
    while i.pai != -1:
        i = cities[i.pai]
        route.append(i)
    return route

def print_route (route, nome):
    """
     Print the route
     :param route: list of cities that will be part of the route
            nome: name of file where route will be printed
     """
    cont = 1
    route.reverse()
    traject = open(nome, "w")
    x = PrettyTable()
    x.field_names = ["Ordem","id", "Nome", "Distancia ate a cidade"]
    for i in route:
        x.add_row([cont,i.ident, i.name, i.g])
        cont = cont+1
    traject.write(str(x))
    traject.close()

def main():
    file = open("australia.csv", "r")

    all_cities = []

    # read all cities and their coordinates from de file
    for line in file:
        info = line.split(",")
        all_cities.append(City(info[0], info[1], info[2], info[3], -1, 0, 0, 0, 0))

    # Remove the first line
    all_cities = all_cities[1:]

    # get list of all cities and their neighbors
    neighbors = verify_neighbors(all_cities)

    # find de final city (Yulara)
    destiny = [find_city(all_cities, "Yulara")]

    # Insere a primeira cidade (Alice Springs) no vetor e preenche seus atributos
    cities = [find_city(all_cities, "Alice Springs")]
    cities[0].pai = -1
    cities[0].expand = 0
    cities[0].g = 0
    cities[0].h = h_distance(cities[0], destiny[0])
    cities[0].f = cities[0].g + cities[0].h

    # A cidade de origem aponta para posicao 0 do vetor cities
    actual_city = 0
    # Algoritmo A*
    while (cities[actual_city].ident != destiny[0].ident):
        actual_city = a_estrela(cities, all_cities, neighbors, actual_city, destiny)

    route = find_route(cities, actual_city)

    print_route (route, "route_a_estrela.txt")


    file.close()




if __name__ == "__main__":
    main()
