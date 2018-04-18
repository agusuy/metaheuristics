""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from math import sin, sqrt
from .problem import OptimizationProblem

def hello_world(target_str="Hello World!"):
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


def __bukin_N6__(elem):
    (x,y) = elem
    return (100 * sqrt(abs(y - 0.01*(x**2)))) + (0.01 * abs(x+10))

def __sum_squares__(elem):
    (x,y) = elem
    
    suma = 0
    for i in range(2):
        suma += i*x**2+i*y**2
        
    return suma

SCHAFFER_N2 = OptimizationProblem(domains= ((-100,+100),)*2, objective=__schaffer_N2__)
BUKIN_N6 = OptimizationProblem(domains= ((-15,-5), (-3, 3)), objective=__bukin_N6__)
SUM_SQUARES = OptimizationProblem(domains= ((-10,+10),)*2, objective=__sum_squares__)
