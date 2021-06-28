import random


def generate_intlist(size, num):
    data = []
    for _ in range(size):
        data.append(random.randint(0, num))
    return data


def generate_intset(size, num):
    return set(generate_list())


def generate_inttuple(size, num):
    return tuple(generate_list())


def generate_intmatrix(row, col, num):
    data = []
    for _ in range(col):
        data.append(generate_list(row, num))
    return data
