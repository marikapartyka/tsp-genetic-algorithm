import numpy as np
import random


class Route:

    def __init__(self, len):
        self.len = len
        self.route = list(np.random.permutation(len))

    def __str__(self):
        return f"Route: {self.route}, has length: {self.len}"

    def get_vertices(self):
        """
        Return a tuple of tuples
        """
        r1 = self.route
        r2 = self.route[1:]
        r2.append(self.route[0])
        return tuple(zip(r1, r2))

    def born_child(self, r2, mutationRate):
        l = self.len

        child = Route(len=l)

        lenSeq = random.randint(2, l - 1)

        idx = random.randint(0, l - lenSeq)

        child.route[idx:(idx + lenSeq)] = self.route[idx:(idx + lenSeq)]

        childInx = (idx + lenSeq) % l

        parentInx = childInx

        while sum(child.route) != sum(self.route):
            if r2.route[parentInx] not in child.route:
                child.route[childInx] = r2.route[parentInx]
                childInx = (childInx + 1) % l
                parentInx = (parentInx + 1) % l
            else:
                parentInx = (parentInx + 1) % l
        mutation = random.random()
        if mutation < mutationRate:
            indexToMutate1 = random.randint(0, len(child.len) - 1)
            indexToMutate2 = random.randint(0, len(child.len) - 1)
            child.route[indexToMutate1], child.route[indexToMutate2] = child.route[indexToMutate2], child.route[
                indexToMutate1]
        return child



    def fitness_function(self,  x, y):
        dist = 0
        r1 = self.route
        r2 = self.route[1:]
        r2.append(self.route[0])
        r = tuple(zip(r1, r2))

        for i, j in r:
            dist = dist + ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5

        return dist





