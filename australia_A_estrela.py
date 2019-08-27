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


#FUNCAO PARA INSERIR AS CIDADES NA VIZINHANCA E CHAMAR CALCULO DE G(N) E H(N)
def insert_neighbors(cities, all_cities, neighbors, actual_city, destiny):
    #APAGAR
    print("FUNCAO EXPANSAO")
    print(actual_city,"name: ", cities[actual_city].name, "id:",  int(cities[actual_city].ident))

    #para todos os vizinhos da cidade atual
    for i in neighbors[int(cities[actual_city].ident)-1]:
        a = all_cities[i-1]
        # a distancia g sera a distancia g da cidade atual mas a distancia real entre as duas cidades
        a.g = cities[actual_city].g + g_distance(a, cities[actual_city])
        #calculo da distancia em linha reta da cidade em questao ate o destino
        a.h = h_distance(a, destiny[0])
        a.f = a.g + a.h
        a.pai = int(cities[actual_city].ident)
        cities.append(City(a.ident, a.name, a.x, a.y, a.pai, a.h, a.g, a.f, 0))
        #APAGAR
        print("id:", a.ident,"name", a.name,"f", a.f,"g", a.g,"h", a.h)




# Funcao para calcular a distancia g
def g_distance (a, b):
    return 1.1*h_distance(a,b)

def h_distance (a,b):
    return ((float(a.x) - float(b.x))**2 + (float(a.y) - float(b.y))**2)**0.5


def main():
    file = open("australia.csv", "r")

    all_cities = []

    # Realizar a leitura das cidades do arquivo e armazenar em um vetor
    for line in file:
        info = line.split(",")
        all_cities.append(City(info[0], info[1], info[2], info[3], -1, 0, 0, 0, 0))

    # Retira a primeira linha (cabeçalho) do vetor
    all_cities = all_cities[1:]

    #APAGAR
    # for i in range(len(all_cities)):
    #     print(all_cities[i].name)

    # Obtem a lista de todos as cidades e seus vizinhos
    neighbors = verify_neighbors(all_cities)

    #APAGAR
    print("DADOS DAS CIDADES")
    for i in range(len(all_cities)):
        print("nome:", all_cities[i].name,"id:", all_cities[i].ident,"vizinhos:", neighbors[i])

    #localizar a cidade de destino (Yulara)
    destiny = [find_city(all_cities, "Yulara")]
    #APAGAR
    print("\nDADOS DESTINO")
    print("id: ",destiny[0].ident,"x: ", destiny[0].x,"y: ", destiny[0].y)

    # Insere a primeira cidade (Alice Springs) no vetor e preenche seus atributos
    cities = [find_city(all_cities, "Alice Springs")]
    cities[0].pai = -1
    cities[0].expand = 0
    cities[0].g = 0
    cities[0].h = h_distance(cities[0], destiny[0])
    cities[0].f = cities[0].g + cities[0].h

    #APAGAR
    print("\nDADOS ORIGEM")
    print("id: ",cities[0].ident,"x: ", cities[0].x,"y: ", cities[0].y)

    # A cidade de origem aponta para posicao 0 do vetor cities
    actual_city = 0
    cont = 0
    #FAZER O LOOP AQUI
    while (cities[actual_city].ident != destiny[0].ident and cont<3):
        #marcar cidade como expandida
        print("-----------------------------------------------------")
        cities[actual_city].expand = 1

        #APAGAR
        print("\nexpandindo ", cities[actual_city].name, "expand", cities[actual_city].expand)

        # Inserir todos os vizinhos da actual_city no vetor cities
        insert_neighbors(cities, all_cities, neighbors, actual_city, destiny)
        n = len(cities)



        for j in range(n):
            if cities[j].expand == 0:
                if cities[j].f < cities[actual_city].f:
                    actual_city = j
                elif cities[actual_city].expand == 1:
                    actual_city = j


        for i in cities:
            print("i:", i.ident, "name:", i.name, "f:", i.f,"g:", i.g,"h:", i.h, "expand:", i.expand )
        cont = cont + 1
    ##ENCERRA O LOOP AQUI

    file.close()




if __name__ == "__main__":
    main()
