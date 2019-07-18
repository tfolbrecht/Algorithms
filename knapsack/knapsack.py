#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    cache = [[{} for k in range(capacity + 1)] for k in range(len(items) + 1)]
    for i in range(len(items) + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                cache[i][j] = {'Value': 0, 'Chosen': []}
            elif items[i - 1].size > j:
                cache[i][j] = cache[i - 1][j]
            else:
                first_case = cache[i - 1][j]
                second_case = {'Value': cache[i-1][j-items[i-1].size]['Value'] + items[i-1].value,
                               'Chosen': cache[i-1][j-items[i-1].size]['Chosen'] + [items[i-1].index]}
                if first_case['Value'] > second_case['Value']:
                    cache[i][j] = first_case
                else:
                    cache[i][j] = second_case
    return cache[len(items)][capacity]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')