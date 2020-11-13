# python3
import sys
import numpy as np
import random

# d = miles away
# m = miles on full tank (start with full tank)
# stops = fuel stations

# return minimum number of refills

# If it is not possible to reach destination output -1


def compute_min_refills(distance, tank, stops):
    refuels = 0
    while distance > tank:
        feasible_stops = stops[stops <= tank]
        #fuel_point = feasible_stops[-1]
        if len(feasible_stops) > 0:
            distance = distance - feasible_stops[-1]
            stops = stops[len(feasible_stops):] - feasible_stops[-1]
            refuels += 1
        else:
            return -1
    return refuels


#distance = 950
#tank = 400
#stops = np.array([200, 375, 550])
#
#compute_min_refills(distance, tank, stops)
    

# Create random tests
#distance = random.randint(0, 1000)
#tank = random.randint(50, 400)
#stops = random.randint(0, 1000)








if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, np.sort(np.array(stops))))
