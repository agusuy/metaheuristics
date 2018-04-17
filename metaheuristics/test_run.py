from .hill_climbing import hill_climbing, hill_climbing_restart
from .sim_annealing import sim_annealing

def test1(problem=None):
    print("Simulated Annealing")
    if not problem:
        from .test_problems import hello_world
        problem = hello_world()
    print(sim_annealing(problem))

def test2(problem=None):
    print("Simulated Annealing")
    if not problem:
        from .test_problems import SCHAFFER_N2
        problem = SCHAFFER_N2
    print(sim_annealing(problem))

def test3(problem=None):
    print("Simulated Annealing")
    if not problem:
        from .test_problems import LEVY_N13
        problem = LEVY_N13
    print(sim_annealing(problem))

def test4(problem=None):
    print("Hill Climbing")
    if not problem:
        from .test_problems import hello_world
        problem = hello_world()
    last = None
    for i in hill_climbing(problem, steps=1000):
        last = i
    print(last)

def test5(problem=None):
    print("Hill Climbing")
    if not problem:
        from .test_problems import SCHAFFER_N2
        problem = SCHAFFER_N2
    last = None
    for i in hill_climbing(problem, steps=1000):
        last = i
    print(last)

def test6(problem=None):
    print("Hill Climbing")
    if not problem:
        from .test_problems import LEVY_N13
        problem = LEVY_N13
    last = None
    for i in hill_climbing(problem, steps=1000):
        last = i
    print(last)

def test7(problem=None, iterations=1000):
    print("Hill Climbing con reinicio")
    if not problem:
        from .test_problems import hello_world
        problem = hello_world()
    print(hill_climbing_restart(problem, iterations=iterations))

def test8(problem=None, iterations=1000):
    print("Hill Climbing con reinicio")
    if not problem:
        from .test_problems import SCHAFFER_N2
        problem = SCHAFFER_N2
    print(hill_climbing_restart(problem, iterations=iterations))

def test9(problem=None, iterations=1000):
    print("Hill Climbing con reinicio")
    if not problem:
        from .test_problems import LEVY_N13
        problem = LEVY_N13
    print(hill_climbing_restart(problem, iterations=iterations))

def test_schaffer(iters=100):
    from .test_problems import SCHAFFER_N2 as sch
    sa_count = 0
    hc_count = 0
    hc_r_count = 0
    #Simulated Annealing
    for i in range(iters):
        sa = sim_annealing(sch)
        if sa[1] == 0.:
            sa_count +=1
    #Hill Climbing
    for i in range(iters):
        last = None
        for j in hill_climbing(sch, steps=1000):
            last = j
        if last[1]==0.:
            hc_count += 1
    # Hill Climbing c/ reinicio aleatorio
    for i in range(iters):
        hcr = hill_climbing_restart(sch, iterations=1000)
        if hcr[1] == 0.:
            hc_r_count += 1

    print("---Problem: Schaffer N2---")
    print("Metaheuristic | Runs    | Found   |")
    print("Hill Climbing |      {}|      {}|".format(iters, hc_count))
    print("HC c/ R. Al.  |      {}|      {}|".format(iters, hc_r_count))
    print("Simulated An. |      {}|      {}|".format(iters, sa_count))
    print("-"*30)