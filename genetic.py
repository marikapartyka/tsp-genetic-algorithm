import matplotlib.pyplot as plt
import matplotlib
import random
import numpy as np
import route
from numpy.core.arrayprint import _formatArray
import ploter

matplotlib.use('TkAgg')


def connect_points(x, y, p1, p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], 'k-')


def fitness_function(route, x, y):
    dist = 0
    r1 = route
    r2 = route[1:]
    r2.append(route[0])
    r = tuple(zip(r1, r2))

    for i, j in r:
        dist = dist + ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5

    return dist


def get_vertices(route):
    """
    Return a tuple of tuples
    """
    r1 = route
    r2 = route[1:]
    r2.append(route[0])
    return tuple(zip(r1, r2))


def draw_route(x, y, route):
    plt.scatter(x, y)
    for i, j in get_vertices(route):
        connect_points(x, y, i, j)
    plt.show()


def new_route(route):
    x = route[:]
    random.shuffle(x)
    return x


def born_child(r1, r2, mutationRate):
    l = len(r1)

    child = [l for i in range(l)]

    lenSeq = random.randint(2, l - 1)

    idx = random.randint(0, l - lenSeq)

    child[idx:(idx + lenSeq)] = r1[idx:(idx + lenSeq)]

    childInx = (idx + lenSeq) % l

    parentInx = childInx

    while sum(child) != sum(r1):
        if r2[parentInx] not in child:
            child[childInx] = r2[parentInx]
            childInx = (childInx + 1) % l
            parentInx = (parentInx + 1) % l
        else:
            parentInx = (parentInx + 1) % l
    mutation = random.random()
    if mutation < mutationRate:
        indexToMutate1 = random.randint(0, len(child) - 1)
        indexToMutate2 = random.randint(0, len(child) - 1)
        child[indexToMutate1], child[indexToMutate2] = child[indexToMutate2], child[indexToMutate1]
    return child


def generate_population_0(count, route):
    gen = []
    for i in range(count):
        gen.append(new_route(route))
    return gen


def fitness_function_generation(x, y, gen):
    listOfValues = []
    for i in range(len(gen)):
        listOfValues.append(fitness_function(gen[i], x, y))

    return listOfValues


def generate_children(genParents, mutationRate):
    l = len(genParents)  # must be an even number
    v, pos = which_min_distance(fitness_function_generation(x, y, genParents), 2)
    pos_copy = pos.copy()

    random.shuffle(pos)

    pairs = tuple(zip(pos, pos_copy))

    listOfChildren = []

    for i, j in pairs:
        listOfChildren.append(born_child(genParents[i], genParents[j], mutationRate))

    listOfChildren.append(genParents[pos[0]])
    listOfChildren.append(genParents[pos[1]])

    return listOfChildren


def which_min_distance(distances, n):
    minDist = np.sort(distances)
    argDist = np.argsort(distances)
    return minDist[:n], argDist[:n]


def new_population_imp(population):
    l = len(population)

    # childDist = fitnessFunctionGeneration(x,y,population)
    # dist,pos = whichMinDistance(childDist,n)
    newGen = population

    for i in range(10 - len(newGen)):
        newGen.append(new_route(newGen[0]))

    return newGen


def simulation(n, mutationRate, x, y):
    ffValues = []
    gen0 = generate_population_0(10, list(range(len(x))))
    recentPop = gen0
    v, _ = which_min_distance(fitness_function_generation(x, y, gen0), 1)
    ffValues.append(v)
    for i in range(n):

        impPop = new_population_imp(generate_children(recentPop, mutationRate))
        v, _ = which_min_distance(fitness_function_generation(x, y, recentPop), 1)
        ffValues.append(v)
        recentPop = impPop
        if i % 100 == 0:
            print(i)

    return impPop, ffValues


x = route.Route(10)
print(x)
vert = x.get_vertices()
print(vert)