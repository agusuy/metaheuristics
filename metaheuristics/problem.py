# -*- coding: utf-8 -*-
from random import Random
from math import inf

class OptimizationProblem:
    """ Representation of an optimization problem.
    """

    def __init__(self, domains, objective, target=-inf, randgen=None):
       """ An optimization problem is defined by:

       + `domains`: a sequence of the ranges of each dimension of the search space, each one as a 
       pair `(min_value, max_value)`.

       + `objetive`: the function to be optimized, which takes an element and returns a number.

       + `target`: the target of the optimization. inf means maximization, -inf minimization and
       any other number is understood as the value to be approximated.
       """
       self.domains = domains
       self.objective = objective
       self.target = target
       self.randgen = randgen or Random()

    def randomElement(self, randgen=None):
        """ Generates a random element, considering the `domains` definition.
        """
        randgen = randgen or self.randgen
        return tuple(randgen.randint(*self.domains[i]) for i in range(len(self.domains)))

    def evaluate(self, element):
        return self.objective(element)
    
    def evaluated(self, elements, sorted=True):
        """ Given a list of `elements` returns a list of tuples `(element, evaluation)`. If `sorted`
        is `True` the elements are sorted by evaluation according to the problem's `target`.
        """
        result = [(e, self.evaluate(e)) for e in elements]
        if sorted:
             keyFun = (lambda p: p[1] if self.target == -inf else -p[1] if self.target == inf 
                                      else abs(self.target - p[1]))
             result.sort(key=keyFun)
        return result
    
    def compareEvaluations(self, eval1, eval2):
        """ Compares the given evaluation considering the problem's target. Returns a positive 
        number if `eval2` is better than `eval1`, a negative one if `eval1` is better than `eval2`,
        or zero otherwise.
        """
        if self.target == inf: # maximization
            return (eval2 > eval1) - (eval2 < eval1)
        elif self.target == -inf: # minimization
            return (eval1 > eval2) - (eval1 < eval2)
        else: # approximation to target
            eval1 = abs(eval1 - self.target)
            eval2 = abs(eval2 - self.target)
            return (eval1 > eval2) - (eval1 < eval2)