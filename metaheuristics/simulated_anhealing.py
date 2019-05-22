from hill_climbing import surroundings
import math
import random
import math
def heat_function(k, temp):
    return lambda t : temp - math.log(t + 1) 

def simulated_annealing(problem, temp_i0, heat_coef, delta=1, time_step=1):
    function = heat_function(heat_coef, temp_i0)
    current = problem.randomElement()
    lastEval = problem.objective(current)
    current = (current, lastEval)
    yield current
    heat = temp_i0
    time = 0
    while (heat > 0):
        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
        if nexts:
            next_elem = nexts[random.randint(0, len(nexts) - 1)]
            if problem.compareEvaluations(current[1], next_elem[1]) > 0:
                current = next_elem
            else:
                delta_temp = abs(next_elem[1] - current[1])
                probability = math.e ** ( - delta_temp / heat)
                if (random.uniform(0,1) <= probability):
                    current = next_elem
        heat = function(time)
        time += time_step
        yield current

