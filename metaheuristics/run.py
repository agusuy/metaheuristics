from hill_climbing import hill_climbing
from simulated_anhealing import simulated_annealing
def test1(problem=None):
    if not problem:
        import test_problems
        problem = test_problems.eggholder()
    for step in hill_climbing(problem, steps=100000):
        print (step)

def test2(problem=None):
    if not problem:
        import test_problems
        problem = test_problems.eggholder()
    for step in simulated_annealing(problem,1600, 1.0000001):
        print (step)

def test3(problem=None):
    if not problem:
        import test_problems
        problem = test_problems.alfiles()
    for step in hill_climbing(problem, steps=100000, restarts=4):
        print (step)

test3()

def test4(problem=None):
    if not problem:
        import test_problems
        problem = test_problems.alfiles()
    for step in simulated_annealing(problem,8, 1):
        print (step)

test4()