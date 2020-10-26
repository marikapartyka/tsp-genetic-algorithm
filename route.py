import numpy as np


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

