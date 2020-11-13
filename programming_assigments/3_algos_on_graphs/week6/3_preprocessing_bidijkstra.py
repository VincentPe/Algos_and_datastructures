import sys
import queue
import math
import itertools

# import matplotlib.pyplot as plt
# import seaborn as sns

# Hints:
# I found that increasing the weight of the 'contracted neighbours' heuristic improved the querying speed.
# Also max hops could be set to quite a high number (5-6) if the pre-processing is implemented correctly.


# Pseudo code

# Preprocess the graph
# 1: Order nodes by importance
# 2: Pull least important node from queue (node a)
# 3: Recompute importance
# 4: Pull the next least important node from queue (node b)
# 5: If importance a < importance b: go to step 6 else put back in queue with new importance and repeat
# 6: For every u, w in (u, v) - (v, w) check if witness path exists
# 7: If no witness path exists add shortcut to preserve distance
# 8: Eliminate node
# 9: Repeat until all nodes are ranked by importance
# 10: Output augmented graph + node order

# Query the preprocessed graph
# 1: Start bidirectional dijkstra using only upward edges
# 2: Stop Dijkstra when the extracted node is already farther than the target
# 3: ComputeDistance function to find meeting point of both dijkstra's results and compute length shortest path
# 4: Return nodes used in bidirectional dijkstra for shortest path
# 5: Reconstruct the shortest path in the initial graph (only when returning the shortest path)

# Settings
settings = {
    'k_hops': 4,
    'v_attempts': 10,
    'ed_weight': 1,
    'cn_weight': 2,
    'sc_weight': 1,
    'L_weight': 1
}

########################################################################################################################
# Self made example:
data = [10, 13,  # n, m
        1, 2, 2, 2, 3, 2, 2, 4, 2, 2, 5, 3, 4, 6, 2, 4, 7, 6, 3, 7, 5,  # u, v and l
        5, 8, 3, 7, 9, 2, 8, 9, 3, 9, 10, 3, 7, 10, 6, 6, 7, 2,  # more u, v and l
        #1, 1, 10  # q, s and t
        ]
########################################################################################################################
# # Plot nodes and edges
# sns.scatterplot(x, y)
# for (i, j), l in edges:
#    sns.lineplot([x[i-1], x[j-1]], [y[i-1], y[j-1]])
########################################################################################################################


class HierarchiesShortestPath:

    def __init__(self, data, settings):

        # Init graph and query params
        self.n, self.m = data[0], data[1]
        self.edges = self.get_edges(data[2:])
        self.adj, self.cost = self.get_adjacents_and_costs()
        #self.q, self.s, self.t = data[0], data[1::2], data[2::2]

        # Init node order
        self.node_order = [0] * self.n
        self.order_count = 1

        # Init settings
        self.k_hops = settings['k_hops']
        self.v_attempts = settings['v_attempts']
        self.ed_weight = settings['ed_weight']
        self.cn_weight = settings['cn_weight']
        self.sc_weight = settings['sc_weight']
        self.L_weight = settings['L_weight']

        # Init node importance
        self.shortcuts = [0] * self.n  # to or from this node
        self.incoming = [len(x) for x in self.adj[1]]
        self.outgoing = [len(x) for x in self.adj[0]]
        self.edge_diff = [s - i - o for s, i, o in zip(self.shortcuts, self.incoming, self.outgoing)]
        self.contract_neighbors = [0] * self.n
        self.shortcut_list = [[] for x in range(self.n)]
        self.shortcut_cover = self.get_shortcut_cover()  # around this node
        self.node_level = [0] * self.n
        self.node_importance = [ed * self.ed_weight + cn * self.cn_weight + sc * self.sc_weight + L * self.L_weight for
                                ed, cn, sc, L in
                                zip(self.edge_diff, self.contract_neighbors, self.shortcut_cover, self.node_level)]

        # Init distance calculation items
        self.estimate = float('inf')
        self.endpoints = []
        self.dist = []
        self.proc_arr = []
        self.Q = []

    def get_edges(self, data):
        return list(zip(zip(data[0:(3 * self.m):3], data[1:(3 * self.m):3]), data[2:(3 * self.m):3]))

    def get_adjacents_and_costs(self):
        adj = [[[] for _ in range(self.n)], [[] for _ in range(self.n)]]
        cost = [[[] for _ in range(self.n)], [[] for _ in range(self.n)]]
        for ((a, b), w) in self.edges:
            adj[0][a - 1].append(b - 1)
            adj[1][b - 1].append(a - 1)
            cost[0][a - 1].append(w)
            cost[1][b - 1].append(w)
        return adj, cost

    def get_shortcut_cover(self):
        shortcut_cover = []
        for v in range(self.n):
            shortcut_cover.append(self.count_shortcut_cover(v))
        return shortcut_cover

    def count_shortcut_cover(self, v):
        counter = 0
        self.shortcut_list[v] = []
        for u, w in list(itertools.product(self.adj[1][v], self.adj[0][v])):
            max_shortcut_length = self.cost[0][u][self.adj[0][u].index(v)] + self.cost[0][v][self.adj[0][v].index(w)]
            wp = self.check_witness_path(u, w, v, max_shortcut_length)
            if wp:
                counter += 1
                self.shortcut_list[v].append(((u, w), max_shortcut_length))
        return counter

    def check_witness_path(self, s, t, ignore_v, max_shortcut_length):

        dist = [float('inf')] * self.n
        dist[s] = 0
        Q = queue.PriorityQueue()
        Q.put((s, 0))

        while not Q.empty():
            u_idx, hop = Q.get()
            if hop < self.k_hops:
                for v_idx, v in enumerate(self.adj[0][u_idx]):
                    if (v != ignore_v) & (self.node_order[v] == 0):
                        new_dist = dist[u_idx] + self.cost[0][u_idx][v_idx]
                        if (dist[v] > new_dist) & (new_dist < max_shortcut_length):
                            dist[v] = dist[u_idx] + self.cost[0][u_idx][v_idx]
                            Q.put((v, hop + 1))

        if dist[t] == float('inf'):
            return 1  # No witness path, so v is important (shortcut should be added)
        else:
            return 0  # witness path, so v is unimportant (no shortcut required)

    def preprocess_graph(self):
        Q = queue.PriorityQueue()
        for idx, ni in enumerate(self.node_importance):
            Q.put((ni, idx))
        while not Q.empty():
            imp_a, node_a = Q.get()
            if not Q.empty():
                imp_a = self.recompute_importance(node_a)
                imp_b, node_b = Q.get()
                if imp_a <= imp_b:
                    self.contract_node(node_a)
                    Q.put((imp_b, node_b))
                else:
                    Q.put((imp_a, node_a))
                    Q.put((imp_b, node_b))
            else:
                self.contract_node(node_a)

    def contract_one_node(self):
        if not hasattr(self, 'Q'):
            print('Creating new queue')
            self.Q = queue.PriorityQueue()
            for idx, ni in enumerate(self.node_importance):
                self.Q.put((ni, idx))
        else:
            print('Pulling from existing queue')

        while not self.Q.empty():
            imp_a, node_a = self.Q.get()
            print('Pulled node {} with importance {} from queue'.format(node_a, imp_a))
            if not self.Q.empty():
                imp_a = self.recompute_importance(node_a)
                print('Recomputed importance, which is now: {}'.format(imp_a))
                imp_b, node_b = self.Q.get()
                print('Pulled node {} which was second in line with importance: {}'.format(node_b, imp_b))
                if imp_a <= imp_b:
                    print('Importance of node a is smaller than or equal to the importance of node b')
                    self.contract_node(node_a)
                    print('Contracted node {}'.format(node_a))
                    print('Updated node order: {}'.format(self.node_order))
                    print('Updated node levels: {}'.format(self.node_level))
                    print('Updated shortcuts: {}'.format(self.shortcuts))
                    print('Updated contracted neighbors: {}'.format(self.contract_neighbors))
                    self.Q.put((imp_b, node_b))
                    print('Put node {} back in the queue'.format(node_b))
                    break
                else:
                    print('Put recomputed node a together with node b back in queue')
                    self.Q.put((imp_a, node_a))
                    self.Q.put((imp_b, node_b))
            else:
                self.contract_node(node_a)
                print('This was the last node')
                print('Updated node order: {}'.format(self.node_order))
                break

    def recompute_importance(self, node):
        ed = self.shortcuts[node] - self.incoming[node] - self.outgoing[node]
        cn = self.contract_neighbors[node]
        sc = self.count_shortcut_cover(node)
        L = self.node_level[node]

        return ed * self.ed_weight + cn * self.cn_weight + sc * self.sc_weight + L * self.L_weight

    def contract_node(self, node):
        self.update_node_order(node)
        self.update_node_levels(node)
        self.update_shortcuts(node)  # Adds shortcuts as well
        self.update_contract_neighbors(node)
        # update shortcut cover when node is fetched from queue

    def update_node_order(self, node):
        self.node_order[node] = self.order_count
        self.order_count += 1

    def update_node_levels(self, node):
        for i in self.adj[0][node] + self.adj[1][node]:
            self.node_level[i] = max([self.node_level[i], self.node_level[node] + 1])

    def update_shortcuts(self, node):

        for (u, w), v in self.shortcut_list[node]:
            if (self.node_order[u] == 0) & (self.node_order[w] == 0):
                #print('Adding shortcut: {}'.format([((u, w), v)]))
                self.adj[0][u].append(w)
                self.cost[0][u].append(v)
                self.adj[1][w].append(u)
                self.cost[1][w].append(v)

                self.shortcuts[u] += 1
                self.shortcuts[w] += 1

    def update_contract_neighbors(self, node):
        for i in self.adj[0][node] + self.adj[1][node]:
            self.contract_neighbors[i] += 1

    def clean_variables(self, s, t):
        self.estimate = float('inf')
        self.endpoints = [s - 1, t - 1]
        self.dist = self.initiate_dist(s - 1, t - 1)
        self.proc_arr = self.initiate_proc_arr(s - 1, t - 1)
        self.Q = self.initiate_queues(s - 1, t - 1)

    def calculate_distance_sp(self):

        while not self.Q[0].empty() or not self.Q[1].empty():
            for i in [0, 1]:
                if not self.Q[i].empty():
                    _, v = self.Q[i].get()
                    if self.dist[i][v] <= self.estimate:
                        self.process_edge(v, i)
                        self.proc_arr[i][v] = 1
                        if (v in self.proc_arr[not i]) & (self.dist[0][v] + self.dist[1][v] < self.estimate):
                            self.estimate = self.dist[0][v] + self.dist[1][v]

        if self.estimate == float('inf'):
            return -1
        else:
            return self.estimate

    def process_edge(self, v, side):
        for u_idx, u in enumerate(self.adj[side][v]):
            if self.node_order[u] > self.node_order[v]:
                #print('Processing edge {}-{} for side {}'.format(v, u, side))

                if self.dist[side][u] > self.dist[side][v] + self.cost[side][v][u_idx]:
                    self.dist[side][u] = self.dist[side][v] + self.cost[side][v][u_idx]
                    # print('Putting in node {} with importance {}'.format(u, self.potential[side][u]))
                    self.Q[side].put((self.dist[side][u], u))

    def initiate_dist(self, s, t):
        dist = [[float('inf')] * self.n, [float('inf')] * self.n]
        dist[0][s], dist[1][t] = 0, 0
        return dist

    def initiate_proc_arr(self, s, t):
        proc_arr = [[0] * self.n, [0] * self.n]
        proc_arr[0][s], proc_arr[1][t] = 1, 1
        return proc_arr

    def initiate_queues(self, s, t):
        Q = [queue.PriorityQueue(), queue.PriorityQueue()]
        Q[0].put((0, s)); Q[1].put((0, t))
        return Q

    def initiate_potentials(self):
        return [[float('inf')] * self.n, [float('inf')] * self.n]


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    navi = HierarchiesShortestPath(data, settings)
    navi.preprocess_graph()
    #navi.contract_one_node()
    #print('Ready\n', flush=True)
    print("Ready\n")
    sys.stdout.flush()
    queries = list(map(int, sys.stdin.read().split()))
    for q in range(queries[0]):
        navi.clean_variables(queries[1::2][q], queries[2::2][q])
        print(navi.calculate_distance_sp())
