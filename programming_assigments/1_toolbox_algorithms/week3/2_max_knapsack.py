# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    value = 0.
    weight_per_thing = values / weights
    while (capacity > 0) & (len(values) > 0):
        if weights[np.argmax(weight_per_thing)] <= capacity:
            value += values[np.argmax(weight_per_thing)]
        else:
            value += values[np.argmax(weight_per_thing)] / weights[np.argmax(weight_per_thing)] * capacity
            
        capacity = capacity - weights[np.argmax(weight_per_thing)]
        values = np.delete(values, np.argmax(weight_per_thing))
        weights = np.delete(weights, np.argmax(weight_per_thing))
        weight_per_thing = np.delete(weight_per_thing, np.argmax(weight_per_thing))

    return round(value, 4)


#capacity = 50
#values = np.array([60, 100, 120])
#weights = ([20, 50, 30])
#
#get_optimal_value(capacity, weights, values)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, np.array(weights), np.array(values))
    print("{:.4f}".format(opt_value))
