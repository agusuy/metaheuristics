""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from math import sin, sqrt
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