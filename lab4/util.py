from reader import get_data
from power import can_be_power

list_of_counts = []
cache = dict()
INF = 10 ** 10


def fantz(binary, x, depth=0):
    if binary == '':
        list_of_counts.append(depth)
        return depth

    if binary in cache:
        return cache[binary] + depth

    list_of_depths = []

    for i in range(1, len(binary) + 1):
        if can_be_power(binary[:i], x):
            list_of_depths.append(fantz(binary[i:], x, depth + 1))

    if len(list_of_depths) == 0:
        cache[binary] = INF
    else:
        cache[binary] = min(list_of_depths) - depth

    list_of_counts.append(cache[binary] + depth)
    return cache[binary] + depth


def algorithm(file):
    data = get_data(file)
    order = data[0]
    x = data[1]
    fantz(order, x)
    if min(list_of_counts) == INF:
        return -1
    else:
        return min(list_of_counts)


print(algorithm('third_input.txt'))