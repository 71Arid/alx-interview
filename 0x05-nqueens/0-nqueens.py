#!/usr/bin/python3
"""this module solves the nqueens problem"""
from sys import argv, exit


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(argv[1])


def solve(n):
    solutions = []
    state = []
    search(state, solutions, n)
    for sol in solutions:
        print(sol)


def is_valid_state(state, n):
    """checks for validity of state of candidate"""
    return len(state) == n


def get_candidates(state, n):
    """get the valid candidates respective to the
    current position to be n queened
    """
    if not state:
        return range(n)
    position = len(state)
    candidate = set(range(n))
    for row, col in enumerate(state):
        candidate.discard(col)
        dist = position - row
        candidate.discard(col + dist)
        candidate.discard(col - dist)
    return list(candidate)


def search(state, solutions, n):
    """searches for the available solution"""
    if is_valid_state(state, n):
        state_format = state_to_format(state)
        solutions.append(state_format)
        return

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def state_to_format(state):
    """converts to the correct format required
    """
    ret = []
    for i, j in enumerate(state):
        item = [i, j]
        ret.append(item)
    return ret


solve(n)
