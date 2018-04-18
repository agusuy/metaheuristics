from metaheuristics import *

tests = [
    simulated_annealing.sum_squares,
    hill_climbing.sum_squares,
    random_restart_hill_climbing.sum_squares,
    simulated_annealing.hello_world,
    hill_climbing.hello_world,
    random_restart_hill_climbing.hello_world,
    simulated_annealing.bukin_n6,
    hill_climbing.bukin_n6,
    random_restart_hill_climbing.bukin_n6,
    simulated_annealing.schaffer_n2,
    hill_climbing.schaffer_n2,
    random_restart_hill_climbing.schaffer_n2
]

for test in tests:
    print(test.__module__ + " - " + test.__name__)
    test()

