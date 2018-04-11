# -*- coding: utf-8 -*-

MAX_RETRIES = 10

def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius) 
               if center[i] - radius >= domains[i][0] and center[i] + radius <= domains[i][1]
           ]

def hill_climbing(problem, steps=100, delta=1, max_retries=MAX_RETRIES, initial=None):
    """ Hill climbing optimization implemented as a generator function. 
    """
    current = initial or problem.randomElement()
    lastEval = problem.objective(current)
    current = (current, lastEval)
    yield current
    for step in range(steps):
        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
        current = nexts[0]
        if problem.compareEvaluations(lastEval, current[1]) > 0:
            lastEval = current[1]
        else:
            if max_retries > 0:
                print("RESTARTED")
                yield from hill_climbing(problem, steps, delta, max_retries-1)
                break
            else:
                break # local optimum has been reached
        yield current

def test1(problem=None):
    if not problem:
        from .test_problems import hello_world
        problem = hello_world()
    for step in hill_climbing(problem, steps=10000):
        print(step)