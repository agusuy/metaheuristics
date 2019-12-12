# Importar lo del modulo de mi equipo
from metaheuristics.hill_climbing import hill_climbing, SCHAFFER_N2, simulated_annealing

def compareHCvsSA():
    problem = SCHAFFER_N2
    n_steps = 100
    HC_solution = ((0, 0), 1)
    SA_solution = ((0, 0), 1)

    # Hill Cimbling with Restart
    best_ref = []
    for step in hill_climbing(problem, steps=n_steps, best_elem_array=best_ref):
        print(step[1], step)
        HC_solution = best_ref

    # Simmulated Annealing
    temperature_func = lambda k: 1000 * 0.95 ** k
    # temperature_func = lambda k: 100 - k
    for step in simulated_annealing(problem, temperature_func, steps=n_steps):
        print(step[1], step)
        SA_solution = step

    print("HC_solution", HC_solution)
    print("SA_solution", SA_solution)
    HC_result = HC_solution[0][1]
    SA_result = SA_solution[1]

    if HC_result > SA_result:
        best_solution = 0
    elif SA_result > HC_result:
        best_solution = 1
    else:
        best_solution = -1

    return HC_result, SA_result, best_solution