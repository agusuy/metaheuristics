# -*- coding: utf-8 -*-

def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius)
               if center[i] + d >= domains[i][0] and center[i] + d <= domains[i][1]
           ]

def random_restart_hill_climbing(problem, steps=100, delta=1, initial=None, restart_count=10):
    final_step = None
    for step in hill_climbing(problem, steps, delta, initial):
        final_step = step
        yield step
    
    i = 1
    while(problem.evaluate(final_step[0]) and restart_count > 0):
        print("-"*10 + "reinicio Nº " + str(i) + "-"*10)
        for step in hill_climbing(problem, steps, delta, initial):
            final_step = step
            yield step
            
        i+=1
        restart_count -= 1

def hill_climbing(problem, steps=100, delta=1, initial=None):
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
            break # local optimum has been reached
        yield current

def test1(problem=None):
    if not problem:
        from .test_problems import hello_world
        problem = hello_world()
    for step in hill_climbing(problem, steps=10000):
        print(''.join(map(chr, step[0])))
        
def test2(problem=None):
    if not problem:
        from .test_problems import hello_world
        problem = hello_world()
    for step in random_restart_hill_climbing(problem, steps=100, restart_count=100):
        print(''.join(map(chr, step[0])))