# -*- coding: utf-8 -*-
import math
import random
from .hill_climbing import surroundings

def sim_annealing(problem):
    """ Hill climbing optimization implemented as a generator function.
    """
    current = problem.randomElement()
    lastEval = problem.objective(current)
    current = (current, lastEval)
    target = problem.target
    t_big = 1.0
    t_min = 0.00001
    alpha = 0.9
    while t_big > t_min:
        nexts = problem.evaluated(surroundings(current[0], 1, problem.domains), sorted=False)
        if len(nexts) >= 1:
            current = nexts[random.randint(0, len(nexts)-1)]
        try:
            prob = math.exp((lastEval-current[1])/t_big)
            if target == math.inf:
                prob = math.exp((current[1]-lastEval)/t_big)
        except OverflowError:
            continue
        if problem.compareEvaluations(lastEval, current[1]) > 0 or prob > random.uniform(0, 1):
            lastEval = current[1]
        t_big *= alpha
    return current