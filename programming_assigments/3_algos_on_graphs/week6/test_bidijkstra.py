import sys
import queue
import random


def distance(adj, cost, s, t):
    
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    
    Q = queue.PriorityQueue()
    Q.put(s)
    
    while not Q.empty():
        u_idx = Q.get()
        
        for v_idx, v in enumerate(adj[u_idx]):
            if dist[v] > dist[u_idx] + cost[u_idx][v_idx]:
                dist[v] = dist[u_idx] + cost[u_idx][v_idx]
                Q.put(v)
    
    if dist[t] == float('inf'):
        return -1
    else:
        return dist[t]


def Process(v, adj, dist, prev, proc, cost, Q, put=True):
    
    for u_idx, u in enumerate(adj[v]):
        if dist[u] > dist[v] + cost[v][u_idx]:
            dist[u] = dist[v] + cost[v][u_idx]
            prev[u] = v
            if put:
                Q.put(u)
        proc.append(u)
#        if put:
#            Q.put(u)
        
    return dist, prev, proc, Q


def ShortestPath(s, t, dist, prev, proc, R_dist, R_prev, R_proc):
    
    distance = float('inf')
#    u_best = None
#    path = []
    
    all_proc = proc + R_proc
    for u in all_proc:
        if dist[u] + R_dist[u] < distance:
            distance = dist[u] + R_dist[u]
#            u_best = u
    
#    last = u_best
#    while last != s:
#        path.append(last)
#        last = prev[last]
#    path = list(reversed(path))
#    
#    last = u_best
#    while last != t:
#        path.append(last)
#        last = R_prev[last]
    
    return distance #path


def BidirectionalDijkstra(s, t, adj, R_adj, cost, R_cost):
    
    dist, R_dist = [float('inf')] * len(adj), [float('inf')] * len(adj)
    dist[s], R_dist[t] = 0, 0    
    prev, R_prev = [None] * len(adj), [None] * len(adj)
    proc, R_proc = [s], [t] 
    Q, R_Q = queue.PriorityQueue(), queue.PriorityQueue()
    Q.put(s); R_Q.put(t)
    
    while True:
        if not Q.empty():
            v = Q.get()
            dist, prev, proc, Q = Process(v, adj, dist, prev, proc, cost, Q)
            
            if v in R_proc:
                # Empty out queue
                while not Q.empty():
                    v = Q.get()
                    dist, prev, proc, Q = Process(v, adj, dist, prev, proc, cost, Q, put=False)
                
                return ShortestPath(s, t, dist, prev, proc, R_dist, R_prev, R_proc)
        else:
            break
            
        if not R_Q.empty():   
            R_v = R_Q.get()
            R_dist, R_prev, R_proc, R_Q = Process(R_v, R_adj, R_dist, R_prev, R_proc, R_cost, R_Q)
            
            if R_v in proc:
                # Empty out queue
                while not R_Q.empty():
                    R_v = R_Q.get()
                    R_dist, R_prev, R_proc, R_Q = Process(R_v, R_adj, R_dist, R_prev, R_proc, R_cost, R_Q, put=False)
                
                return ShortestPath(s, t, dist, prev, proc, R_dist, R_prev, R_proc)
        else:
            break
        
    return -1


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
    
with open('edges.txt', 'w') as f:
    f.write("n:{}\n".format(n))
    f.write("m:{}\n".format(m))
    for item in edges:
        f.write("{}\n".format(item))

testrounds = 10
for i in range(testrounds):
    s = random.randint(0, n-1)
    t = random.randint(0, n-1)
    
    print('Start on {} and finish {}'.format(s, t))
    
    dijkstra = distance(adj, cost, s, t)
    
    print('Dijkstra finished, cost: {}'.format(dijkstra))
    
    bidijkstra = BidirectionalDijkstra(s, t, adj, R_adj, cost, R_cost)
    print('Dijkstra: {}, Bidijkstra: {}'.format(dijkstra, bidijkstra))
    
    if dijkstra != bidijkstra:
        print("Found different answers")
        raise Exception("s is {} and t is {}".format(s, t))     
        
print('Completed {} tests with success'.format(testrounds))


import itertools
test = list(itertools.chain(*[[x, y, z] for ((x,y), z) in edges]))


