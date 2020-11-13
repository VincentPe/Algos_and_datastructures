import sys
import queue
import math

#import matplotlib.pyplot as plt
#import seaborn as sns

## Self made example:
#data = [10, 12, 0, 0, 1, 1, 1, 3, 2, 2, 3, 1, 2, 4, 4, 4, 5, 2, 6, 4, 6, 6, 1, 2, 2, 2, 3, 2, 2, 4, 2, 2, 5, 3, 4, 6, 2, 3, 7, 5, 5, 8, 3, 7, 9, 2, 8, 9, 3, 9, 10, 3, 7, 10, 6, 6, 7, 2, 1, 1, 10]
#
#
################################################################################
## What happens before calling the function
##data = [2, 1, 0, 0, 0, 1, 1, 2, 1, 4, 1, 1, 2, 2, 1, 2, 2, 1]
##data = [4, 4, 0, 0, 0, 1, 2, 1, 2, 0, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 6, 1, 1, 3]
#n, m = data[0], data[1]
#data = data[2:]
#
#x = data[:n*2][::2]
#y = data[:n*2][1::2]
#data = data[n*2:]
#
##sns.scatterplot(x, y)
#
#edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#data = data[m*3:]
#adj = [[] for _ in range(n)]
#R_adj = [[] for _ in range(n)]
#cost = [[] for _ in range(n)]
#R_cost = [[] for _ in range(n)]
#for ((a, b), w) in edges:
#    adj[a - 1].append(b - 1)
#    R_adj[b - 1].append(a - 1)
#    cost[a - 1].append(w)
#    R_cost[b - 1].append(w)
#    
#q = data[0]
#data = data[1:]
#s, t = data[0] -1, data[1] -1
################################################################################


class Astar_algo:
    
    def __init__(self, s, t, x, y, adj, R_adj, cost, R_cost):
        
        self.start = s
        self.finish = t
        self.endpoints = [t, s]  # is reversed
        self.x = x
        self.y = y
        self.adj = [adj, R_adj]
        self.cost = [cost, R_cost]
        
        self.initiate_distances()
        self.initiate_process()
        self.initiate_queues()
        self.initiate_potentials()
        
    def initiate_distances(self):
        self.dist = [[float('inf')] * len(self.adj[0]), [float('inf')] * len(self.adj[0])]
        self.dist[0][self.start], self.dist[1][self.finish] = 0, 0
        
    def initiate_process(self):
        self.proc = [self.start, self.finish]
        self.proc_arr = [[0] * len(self.adj[0]), [0] * len(self.adj[0])]
        self.proc_arr[0][self.start], self.proc_arr[1][self.finish] = 1, 1
        
    def initiate_queues(self):
        self.Q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.Q[0].put((0, self.start)); self.Q[1].put((0, self.finish))
        
    def initiate_potentials(self):
        self.potential = [[float('inf')] * len(self.adj[0]), [float('inf')] * len(self.adj[0])]
        
    def euclidean_distance(self, x1, x2, y1, y2):
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
    
    def approx_potential(self, u, side):
        dist_f = self.euclidean_distance(x[u], x[self.endpoints[0]], y[u], y[self.endpoints[0]])
        dist_b = self.euclidean_distance(x[u], x[self.endpoints[1]], y[u], y[self.endpoints[1]])
        
        if side == 0:
            return (dist_f - dist_b) / 2
        else: 
            return - (dist_f - dist_b) / 2
    
    def process_edge(self, v, side):
        for u_idx, u in enumerate(self.adj[side][v]):
            potential = self.approx_potential(u, side)
            
            if self.dist[side][u] == float('inf'): # and other side?
                self.proc.append(u)
            if self.potential[side][u] > (self.dist[side][v] + self.cost[side][v][u_idx] + potential):
                self.potential[side][u] = self.dist[side][v] + self.cost[side][v][u_idx] + potential
                self.dist[side][u] = self.dist[side][v] + self.cost[side][v][u_idx]
                self.Q[side].put((self.potential[side][u], u))
                
    def find_shortest_path(self):
        distance = float('inf')
        for u in self.proc:
            if self.dist[0][u] + self.dist[1][u] < distance:
                distance = self.dist[0][u] + self.dist[1][u]
        return distance 
    
    def bidirectional_search(self):
        while not self.Q[0].empty() and not self.Q[1].empty():
            for i in [0, 1]:
                _, v = self.Q[i].get()
                if self.proc_arr[not i][v] == 1:
                    return self.find_shortest_path()
                self.process_edge(v, i)
                self.proc_arr[i][v] = 1
        return -1
    
    
    
if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    data = data[2:]
    
    x = data[:n*2][::2]
    y = data[:n*2][1::2]
    data = data[n*2:]
    
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[m*3:]
    adj = [[] for _ in range(n)]
    R_adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    R_cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        R_adj[b - 1].append(a - 1)
        cost[a - 1].append(w)
        R_cost[b - 1].append(w)
        
    q = data[0]
    data = data[1:]
    
    for i in range(len(data)//2):
        s, t = data[i*2] - 1, data[i*2+1] - 1
        navi = Astar_algo(s, t, x, y, adj, R_adj, cost, R_cost) 
        print(navi.bidirectional_search())
    

    