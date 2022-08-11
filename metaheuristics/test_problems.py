""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from math import sin, cos, exp, sqrt, pi
from .problem import OptimizationProblem

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

def __levy_N13__(elem):
    (x, y) = elem
    res = sin(3*pi*x)*sin(3*pi*x)+(x-1)*(x-1)*(1+sin(3*pi*y)*sin(3*pi*y)) + \
          (y-1)*(y-1)*(1+sin(2*pi*y)*sin(2*pi*y))
    return res

LEVY_N13 = OptimizationProblem(domains=((-10,+10),)*2, objective=__levy_N13__)