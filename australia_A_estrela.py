class City:
    def __init__(self, ident, name, x, y):
        self.ident = ident
        self.name = name
        self.x = x
        self.y = y


def find_city(all_cities, city):
    return next(x for x in all_cities if x.name == city)


def insert_neighbors(cities, all_cities, ident):
    if ident % 2 == 1:
        pass
    if ident % 2 == 0:
        pass


def main():
    file = open("australia.csv", "r")

    all_cities = []

    for line in file:
        info = line.split(",")
        all_cities.append(City(info[0], info[1], info[2], info[3]))

    all_cities = all_cities[1:]

    for i in range(len(all_cities)):
        print(all_cities[i].name)

    cities = [find_city(all_cities, "Alice Springs")]

    insert_neighbors(cities, all_cities, cities[-1].ident)

    print(cities[0].ident)

    file.close()


if __name__ == "__main__":
    main()
