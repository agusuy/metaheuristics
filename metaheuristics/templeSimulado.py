# -*- coding: utf-8 -*-
import random
import math

def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius)
               if center[i] - radius >= domains[i][0] and center[i] + radius <= domains[i][1]
           ]
#T es la temperatura con la que empieza luego va bajando, M la cantidad que quiero que itere y Tf la temperatura final
def temple_simulado(problem,T=30,Tf=0.5,M=15, delta=1, initial=None):
    current = initial or problem.randomElement() #obtiene una palabra random?
    lastEval = problem.objective(current) #obtiene la distancia entre current y helloworld!
    current = (current, lastEval) # la palabra con su valuacion
    yield current
    beta = (T-Tf)/(M*T*Tf) # cte que se calcula para aplicar Cauchy modificado para que itere M veces
    Tk = T
    while Tk > Tf:
        #print(str(Tk))
		#domains es el dominio de los ascii que son caracteres y evalueated los evalua con valores absolutos segun el problema
        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
        nextChangeFlg = False
        while(not nextChangeFlg):
            if len(nexts)==0:
                break
            current = nexts.pop(random.randint(0,len(nexts)-1))
            if (problem.compareEvaluations(lastEval, current[1]) > 0):
                lastEval = current[1]
                nextChangeFlg = True
            else:
				# calcular probabilidad
                diferencia = lastEval - current[1]
                if diferencia ==0:
                    yield current
                    return
                if (math.exp(diferencia/Tk)*100 >= random.randint(0,100)):
                    lastEval = current[1]
                    nextChangeFlg = True

		#bajo el Tk
        temp=Tk
        Tk = enfriamientoCauchyM(Tk,beta)
        #print("Tk prev: {}\t Tk posterior: {} \tVariacion: {}".format(temp,Tk,temp/Tk))
        yield current

def enfriamientoCauchyM(Tk,beta):#enfria T con Cauchy modificado para que itere M veces
	return Tk/(1+beta*Tk)

def test3(problem=None,T=10,Tf=0.5,M=10):
    if not problem:
        from .test_problems import hello_world,SCHAFFER_N2,BUKING_N6
        problem=hello_world()
    #return temple_simulado(problem,M=1000)
    for step in temple_simulado(problem,T=T,Tf=Tf,M=M):
        imprimir = ' '.join(map(str,step[0]))
    #print(imprimir)
    return step
def test1(problem=None,restarts=20,steps=100):
    if not problem:
        from .test_problems import hello_world,SCHAFFER_N2,BUKING_N6
        problem=BUKING_N6
        #problem = hello_world()
        #problem = SCHAFFER_N2
    result = random_restart_hill_climbing(problem,restarts,steps)
    print(result)
def test2():
    from .test_problems import hello_world,SCHAFFER_N2,BUKING_N6
    print("\nTest Hello World")
    print(test3(problem=hello_world(),T=75,Tf=0.5,M=2000))
    print("\nTest SCHAFFER_N2")
    print(test3(problem=SCHAFFER_N2,T=15,Tf=0.005,M=10000))
    print("\nTest BUKING_N6")
    print(test3(problem=BUKING_N6,T=5,Tf=0.01,M=10))
