""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from math import sin, sqrt, inf
from problem import OptimizationProblem

def hello_world(target_str="Hello world!"):
    target_chars = tuple(map(ord, target_str))
    return OptimizationProblem(
        domains = ((32, 126),) * len(target_str),
        objective = lambda chars: sum(abs(c - t) for (c, t) in zip(chars, target_chars))
    )

# References:
# + [Test functions for optimization @ Wikipedia](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
# + [Test functions and datasets @ Virtual Library of Simulation Experiments](https://www.sfu.ca/~ssurjano/optimization.html)

def __schaffer_N2__(elem):
    (x,y) = elem
    return 0.5 + (sin(x*x - y*y) ** 2 - 0.5)/((1 + 0.001 * (x*x + y*y)) ** 2)

SCHAFFER_N2 = OptimizationProblem(domains= ((-100,+100),)*2, objective=__schaffer_N2__)

def eggholder():
    return OptimizationProblem(
        domains = ((-512,512),) * 2,
        objective = lambda elem : - (elem[1] + 47) * sin( sqrt( abs( elem[1] + elem[0]/2 + 47) ) ) - elem[0] * sin( sqrt( abs( elem[0] - ( elem[1] + 47 ) ) ) )
    )

board = [1,2,3,2,6,8,7,2,8,6,2,5,1,3,1,4,7,1,5,4,2,5,6,8,2,
         8,4,7,5,1,4,3,4,3,7,2,3,8,5,1,6,5,6,3,4,7,8,3,3,7,
         1,8,6,2,4,6,8,4,5,6,7,5,1,7]

def objective_function(elem):
    alfilesAtacandose = 0
    sumaTotal = 0
    for i in range(0, len(elem)):
        ya = int( elem[i] / len(elem))
        xa = elem[i] % len(elem)
        sumaTotal += board[i]
        for k in range(0, len(elem)):
            if k == i:
                continue
            alfil = elem[k]
            yc = int( alfil / len(elem))
            xc = alfil % len(elem)
            for j in range (0, 8):
                if (xc == xa + j) and (yc == ya + j):
                    alfilesAtacandose -= len(elem) + 1 - board[k]
                elif (xc == xa + j) and (yc == ya - j):
                    alfilesAtacandose -= len(elem) + 1 - board[k]
                elif (xc == xa - j) and (yc == ya + j):
                    alfilesAtacandose -= len(elem) + 1 - board[k]
                elif (xc == xa - j) and (yc == ya - j):
                    alfilesAtacandose -= len(elem) + 1 - board[k]
    if alfilesAtacandose:
        return alfilesAtacandose
    else:
        return sumaTotal
    
            
            


def alfiles():
    return OptimizationProblem(
       domains = ((0,63),) * 8,
       objective = objective_function,
       target=inf,
       )