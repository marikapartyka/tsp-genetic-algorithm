import route
import ploter
import generation

def new_route(route):
    x = route[:]
    random.shuffle(x)
    return x

def new_population_imp(population):
    l = len(population)

    # childDist = fitnessFunctionGeneration(x,y,population)
    # dist,pos = whichMinDistance(childDist,n)
    newGen = population

    for i in range(10 - l):
        newGen.append(new_route(newGen[0]))

    return newGen


class Simulation:
    def __init__(self, n, number,len, mutationRate, x, y):
        self.n = n
        self.number = number
        self.len = len
        self.mutationRate = mutationRate
        self.x = x
        self.y = y



    def make_simulation(self):

        ffValues = []
        gen0 = generation.Generation(self.number, self.len, self.x, self.y).generate_population_0()
        recentPop = gen0
        v, _ = generation.which_min_distance(gen0.fitness_function_generation(), 1)
        ffValues.append(v)
        for i in range(n):

            impPop = new_population_imp(recentPop.generate_children(mutationRate))
            v, _ = which_min_distance(recentPop.fitness_function_generation(), 1)
            ffValues.append(v)
            recentPop = impPop
            if i % 100 == 0:
                print(i)

        return impPop, ffValues
