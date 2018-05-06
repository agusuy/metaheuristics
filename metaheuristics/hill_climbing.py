# -*- coding: utf-8 -*-
import math

from metaheuristics.test_problems import hello_world, SCHAFFER_N2, ocho_alfiles, boda, is_valid_boda

MAX_RETRIES = 10

def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius)
               if center[i] + d >= domains[i][0] and center[i] + d <= domains[i][1]
           ]

def hill_climbing(problem, steps=100, delta=1, max_retries=MAX_RETRIES, best_elem_array=None, initial=None):
    """ Hill climbing optimization implemented as a generator function.
    """
    current = initial or problem.randomElement()
    lastEval = problem.objective(current)
    current = (current, lastEval)
    yield current
    if (best_elem_array != None) and (len(best_elem_array) == 0):
        best_elem_array.append(current)
    for step in range(steps):
        prev = current
        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
        current = nexts[0]
        if problem.compareEvaluations(lastEval, current[1]) > 0:
            lastEval = current[1]
        else:
            if max_retries > 0:
                if (best_elem_array != None) and (problem.compareEvaluations(prev[1], best_elem_array[0][1]) < 0):
                    best_elem_array[0] = prev
                print("RESTARTED")
                yield from hill_climbing(problem, steps, delta, max_retries-1, best_elem_array)
                break
            else:
                break # local optimum has been reached
        yield current

def simulated_annealing(problem, temperature_func, steps=100, delta=1, initial=None):
    """ Simmulated annealing optimization implemented as a generator function.
    """

    current = initial or problem.randomElement()
    lastEval = problem.objective(current)
    current = (current, lastEval)
    yield current

    for step in range(2, steps):
        temperature = temperature_func(step)
        if temperature <= 0:
            break

        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
        possible_next = problem.randgen.choice(nexts)
        if problem.compareEvaluations(lastEval, possible_next[1]) > 0:
            lastEval = possible_next[1]
            current = possible_next
        else:
            probability = math.exp(- math.fabs(possible_next[1] - lastEval) / temperature)
            if problem.randgen.random() < probability:
                lastEval = possible_next[1]
                current = possible_next

        yield current

def test1(problem=None):
    if not problem:
        problem = ocho_alfiles()

    for step in hill_climbing(problem, steps=100, max_retries=0):
        print(step)

def test2(problem=None):
    if not problem:
        problem = ocho_alfiles()

    best_ref = []
    for step in hill_climbing(problem, steps=100, best_elem_array=best_ref):
        print(step)

    print("Best run:")
    print(best_ref)

def test3(problem=None):
    if not problem:
        problem = ocho_alfiles()

    temperature_func = lambda k: 1000*0.95**k
    # temperature_func = lambda k: 100 - k
    for step in simulated_annealing(problem, temperature_func, steps=100):
        print(step)

def test_boda():
    problem = boda()

    temperature_func = lambda k: 1000 * 0.95 ** k
    for step in simulated_annealing(problem, temperature_func, steps=100):
        print(step, is_valid_boda(step[0]))