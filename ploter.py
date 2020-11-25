import route
import matplotlib.pyplot as plt
class Ploter:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self):
        plt.scatter(self.x, self.y)
        plt.show()

    def connect_points(self, p1, p2):
        x1, x2 = self.x[p1], self.x[p2]
        y1, y2 = self.y[p1], self.y[p2]
        plt.plot([x1, x2], [y1, y2], 'k-')

    def draw_route(self, route):
        for i, j in route.get_vertices():
            self.connect_points(i, j)
        plt.show()




