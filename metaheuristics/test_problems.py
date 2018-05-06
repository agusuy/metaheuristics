""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from math import sin

import math
from random import shuffle

from .problem import OptimizationProblem


def hello_world(target_str="Hello world!"):
    target_chars = tuple(map(ord, target_str))
    return OptimizationProblem(
        domains=((32, 126),) * len(target_str),
        objective=lambda chars: sum(abs(c - t) for (c, t) in zip(chars, target_chars))
    )


# References:
# + [Test functions for optimization @ Wikipedia](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
# + [Test functions and datasets @ Virtual Library of Simulation Experiments](https://www.sfu.ca/~ssurjano/optimization.html)

def __schaffer_N2__(elem):
    (x, y) = elem
    return 0.5 + (sin(x * x - y * y) ** 2 - 0.5) / ((1 + 0.001 * (x * x + y * y)) ** 2)


SCHAFFER_N2 = OptimizationProblem(domains=((-100, +100),) * 2, objective=__schaffer_N2__)


def generate_board():
    return [1, 2, 3, 2, 6, 8, 7, 2, 8, 6, 2, 5, 1, 3, 1, 4, 7, 1, 5, 4, 2, 5, 6, 8, 2, 8, 4, 7, 5, 1, 4, 3, 4, 3, 7, 2,
            3, 8, 5, 1, 6, 5, 6, 3, 4, 7, 8, 3, 3, 7, 1, 8, 6, 2, 4, 6, 8, 4, 5, 6, 7, 5, 1, 7]


def ocho_alfiles():
    board = generate_board()

    return OptimizationProblem(
        domains=((0, 63),) * 8, target=math.inf,
        objective=lambda alfiles: aux(board, alfiles))


def shares_diagonal(alfil_pos, alfiles):
    result = False
    row = alfil_pos // 8
    column = alfil_pos % 8
    sum_value = row + column
    abs_diff = row - column

    # Diagonal 1: Coordenadas suman lo mismo
    # Diagonal 2: Valor absoluto de coordenadas es igual
    sharing_diagonal = []
    for alfil in alfiles:
        x = alfil // 8
        y = alfil % 8
        if (x + y) == sum_value or x - y == abs_diff:
            sharing_diagonal.append(alfil)
    return


def print_a_board():
    counter = 0
    for x in range(8):
        row = ""
        for y in range(8):
            row += "{:4d}".format(counter)
            counter += 1
        print(row)


def aux(board, alfiles):
    res = 0
    for alfil_pos in alfiles:
        if shares_diagonal(alfil_pos, alfiles):
            res += -9 + board[alfil_pos]
        else:
            res += board[alfil_pos]
    return res


###############################################

def generate_matriz(n_invitados):
    n_invitados = n_invitados
    n_relations = n_invitados * (n_invitados - 1)
    percentage_plus_one = 0.3
    percentage_minus_one = 0.2

    n_plus_one = int(n_relations * percentage_plus_one)
    n_minus_one = int(n_relations * percentage_minus_one)
    n_zero = n_relations - n_plus_one - n_minus_one
    relations = [1] * n_plus_one + [-1] * n_minus_one + [0] * n_zero
    shuffle(relations)

    matriz_afinidad = []
    for x in range(n_invitados):
        matriz_afinidad.append([])
        for y in range(n_invitados):
            if x == y:
                matriz_afinidad[x].append(0)
            else:
                matriz_afinidad[x].append(relations.pop(0))

    for i, row in enumerate(matriz_afinidad):
        print("Row {}: {}".format(i, row))
    return matriz_afinidad

def boda():
    n_invitados = 70
    n_tables = 12
    matriz_afinidad = generate_matriz(n_invitados)

    return OptimizationProblem(
        domains=((0, n_tables - 1),) * n_invitados,
        target=math.inf,
        objective=lambda posiciones_invitados: evaluate_boda(posiciones_invitados, matriz_afinidad))

def evaluate_boda(posiciones_invitados, matriz_afinidad):
    max_per_table = 6
    tables = {}

    # Checkea que no haya mesas con mas de max_per_table personas sentadas
    for invitado_n, mesa in enumerate(posiciones_invitados):
        tables.setdefault(mesa, [])
        tables[mesa].append(invitado_n)

    result = 0
    for people_in_table in tables.values():
        num_in_table = len(people_in_table)
        if num_in_table > max_per_table:
            result += max_per_table - num_in_table

    # Si no hay mesas excedidas, sumar afinidades
    for people_in_table in tables.values():
        for person in people_in_table:
            for other_person in people_in_table:
                result += matriz_afinidad[person][other_person]

    return result

def is_valid_boda(posiciones_invitados):
    mesas = {}

    for mesa in posiciones_invitados:
        mesas.setdefault(mesa, 0)
        mesas[mesa] += 1

    for n_mesa, mesa in mesas.items():
        if mesa > 6:
            print("mesa {} tiene {} personas".format(n_mesa, mesa))
            return False

    return True


#############################