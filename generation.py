import route
import random
import numpy as np


class Generation:

    def __init__(self, number, len, x, y):
        self.number = number
        self.len = len
        self.x = x
        self.y = y

    def generate_population_0(self):
        gen = []
        for i in range(self.number):
            gen.append(route.Route(len=self.len))

        self.gen = gen

    def which_min_distance(self, distances, n):
        minDist = np.sort(distances)
        argDist = np.argsort(distances)
        return minDist[:n], argDist[:n]

    def fitness_function_generation(self):
        listOfValues = []
        for i in range(len(self.gen)):
            listOfValues.append(self.gen[i].fitness_function(self.x, self.y))

        return listOfValues

    def generate_children(self, mutationRate):
        l = len(self.gen)  # must be an even number
        v, pos = self.which_min_distance(self.fitness_function_generation(), 2)
        pos_copy = pos.copy()

        random.shuffle(pos)

        pairs = tuple(zip(pos, pos_copy))

        listOfChildren = []

        for i, j in pairs:
            listOfChildren.append(self.gen[i].born_child(self.gen[j], mutationRate))

        listOfChildren.append(self.gen[pos[0]])
        listOfChildren.append(self.gen[pos[1]])

        return listOfChildren