# -*- coding: utf-8 -*-
import random
import math
from .hill_climbing import surroundings

def temp_function(T,k,t):
    return T*(k**t)

def simulated_annealing(problem, T0=1000, k=0.999, delta=1, initial=None):
    current = problem.randomElement()
    lastEval = problem.objective(current)
    current = (current, lastEval)
    yield current

    T = T0
    t=1
    while T > 0.05:
        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
        if(nexts):
            siguiente = nexts[random.randint(0, len(nexts) - 1)]
            evaluate = problem.compareEvaluations(current[1], siguiente[1]) > 0

            if evaluate > 0:
                current = siguiente
            else:
                deltaE = siguiente[1] - current[1]
                prob = math.e ** ( - deltaE / T)
                
                if(random.random() <= prob):
                    current = siguiente

        T = temp_function(T0,k,t)
        t+=1
        yield current

def schaffer_n2():
    from .test_problems import SCHAFFER_N2
    problem = SCHAFFER_N2
    finalStep = list(simulated_annealing(problem, k=0.999))[-1]
    print(finalStep)
    
def bukin_n6():
    from .test_problems import BUKIN_N6
    problem = BUKIN_N6
    finalStep = list(simulated_annealing(problem, k=0.999))[-1]
    print(finalStep)

def sum_squares():
    from .test_problems import SUM_SQUARES
    problem = SUM_SQUARES
    finalStep = list(simulated_annealing(problem, k=0.9))[-1]
    print(finalStep)
    
def hello_world():
    from .test_problems import hello_world
    problem = hello_world()
    finalStep = list(simulated_annealing(problem, k=0.999))[-1]
    print("".join(map(chr,finalStep[0])), finalStep[1])
    