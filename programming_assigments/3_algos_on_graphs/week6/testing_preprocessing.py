import random

from preprocessing_bidijkstra_coords import HierarchiesShortestPath, settings
from coordinates_search import Astar_algo

# Define random experiments
n = random.randint(5, 10)
m = random.randint(10, 20)

if (n * n-1) < m:
    raise Exception("There arent enough unique possible edges to connect the nodes")

data = []
while len(data) < m:
    new_edge = (random.randint(1, n), random.randint(1, n))
    if (new_edge not in data) & (new_edge[0] != new_edge[1]):
        data.append(new_edge)

edges = []
for edge in data:
    edges.append((edge, random.randint(1, 10)))

adj = [[] for _ in range(n)]
R_adj = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
R_cost = [[] for _ in range(n)]
for ((a, b), w) in edges:
    adj[a - 1].append(b - 1)
    R_adj[b - 1].append(a - 1)
    cost[a - 1].append(w)
    R_cost[b - 1].append(w)

testrounds = 10
for i in range(testrounds):
    s = random.randint(0, n-1)
    t = random.randint(0, n-1)

print('Start on {} and finish {}'.format(s, t))

navi1 = Astar_algo(s, t, x, y, adj, R_adj, cost, R_cost)
wo_processing = navi1.bidirectional_search()

print('Dijkstra without processing, cost: {}'.format(wo_processing))

navi2 = HierarchiesShortestPath(data, settings)
navi2.preprocess_graph()

navi2.clean_variables(s, t)
w_processing = navi2.calculate_distance_sp()
print('Dijkstra with processing, cost: {}'.format(wo_processing))

if wo_processing != w_processing:
    print("Found different answers")
    raise Exception("s is {} and t is {}".format(s, t))

print('Completed {} tests with success'.format(testrounds))