# -*- coding: utf-8 -*-

def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius) 
               if center[i] - radius >= domains[i][0] and center[i] + radius <= domains[i][1]
           ]

def hill_climbing(problem, steps=100, delta=1, initial=None, restarts=0):
    """ Hill climbing optimization implemented as a generator function. 
    """
    result = None

    bests = []
    for i in range(restarts + 1):
        actuals = []
        current = initial or problem.randomElement()
        lastEval = problem.objective(current)
        current = (current, lastEval)
        actuals.append(current)
    
        for step in range(steps):
            nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
            current = nexts[0]
            if problem.compareEvaluations(lastEval, current[1]) > 0:
                lastEval = current[1]
            else:
                break # local optimum has been reached
            actuals.append(current)

        if (result):
            if problem.compareEvaluations(result, lastEval) > 0:
                result = lastEval
                bests = actuals
        else:
            result = lastEval
            bests = actuals
    return bests

    

def test1(problem=None):
    if not problem:
        from .test_problems import hello_world
        problem = hello_world()
    for step in hill_climbing(problem, steps=10000):
        print(step, ''.join(map(chr, step[0])))
