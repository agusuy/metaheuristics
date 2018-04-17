# -*- coding: utf-8 -*-

def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius) 
               if center[i] - radius >= domains[i][0] and center[i] + radius <= domains[i][1]
           ]

def hill_climbing(problem, steps=100, delta=1, initial=None):
    """ Hill climbing optimization implemented as a generator function. 
    """
    current = initial or problem.randomElement()
    lastEval = problem.objective(current)
    current = (current, lastEval)
    yield current
    for step in range(steps):
        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
        if(len(nexts) >= 1):
            current = nexts[0]
        if problem.compareEvaluations(lastEval, current[1]) > 0:
            lastEval = current[1]
        else:
            break # local optimum has been reached
        yield current

def hill_climbing_restart(problem, steps=100, delta=1, initial=None, iterations=1):
    """ Hill climbing with restart optimization implemented as a generator function.
        Returns the optimal result
    """
    optimal = (None, None)
    for iter in range(iterations):
        for step in hill_climbing(problem=problem, steps=steps, delta=delta, initial=initial):
            current = step
        if optimal[0] is None:
            optimal = current
        elif problem.compareEvaluations(optimal[1], current[1]) > 0:
            optimal = current
    return optimal

