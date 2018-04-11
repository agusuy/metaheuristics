""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from .problem import OptimizationProblem

def hello_world(target_str="Hello world!"):
    target_chars = tuple(map(ord, target_str))
    return OptimizationProblem(
        domains = ((32, 126),) * len(target_str),
        objective = lambda chars: sum(abs(c - t) for (c, t) in zip(chars, target_chars))
    )

# From <https://en.wikipedia.org/wiki/Test_functions_for_optimization> ##############################

def __schaffer_N2__(elem):
    (x,y) = elem
    return 0.5 + (sin(sin(x*x - y*y)) - 0.5)/((1 + 0.001 * (x*x + y*y)) ** 2)

SCHAFFER_N2 = OptimizationProblem(((-100,+100),)*2, __schaffer_N2__)