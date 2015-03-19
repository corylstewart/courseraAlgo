import heapq
import random
import time

def read_file(filename):
    G = dict()
    with open(filename) as f:
        graph_size = f.readline()
        for line in f.readlines():
            edge = line.split()
            node1 = int(edge[0])
            node2 = int(edge[1])
            edge_cost = int(edge[2])
            if node1 not in G:
                G[node1] = dict()
            if node2 not in G:
                G[node2] = dict()
            G[node1][node2] = edge_cost
            G[node2][node1] = edge_cost
    return G


def join_them(G, node1, node2, edge_cost):
    if node1 not in G:
        G[node1] = dict()
    if node2 not in G:
        G[node2] = dict()
    G[node1][node2] = edge_cost
    G[node2][node1] = edge_cost

def make_small_G():
    G = dict()
    join_them(G, 1, 2, 1)
    join_them(G, 1, 3, 4)
    join_them(G, 1, 4, 3)
    join_them(G, 2, 4, 2)
    join_them(G, 3, 4, 5)

    return G

def prim(G):
    frontier = list()
    Z = dict()
    seen = dict()
    start_node = random.choice(G.keys())
    for node in G[start_node]:
        heapq.heappush(frontier, (G[start_node][node], node, start_node))
        seen[node] = [G[start_node][node], start_node]
    Z[start_node] = dict()
    while frontier:
        next_edge = heapq.heappop(frontier)
        weight = next_edge[0]
        node1 = next_edge[1]
        nodez = next_edge[2]
        if node1 not in Z:
            join_them(Z, node1, nodez, weight)
            for node2 in G[node1]:
                if node2 not in Z:
                    if node2 in seen and G[node1][node2] < seen[node2][0]:
                        try:
                            frontier.remove((seen[node2][0], node2, nodez))
                        except:
                            for i in range(len(frontier)):
                                if frontier[i][0] == seen[node2][0] and frontier[i][1] == node2:
                                    frontier.pop(i)
                                    break
                        heapq.heapify(frontier)
                        heapq.heappush(frontier, (G[node1][node2], node2, node1))
                        seen[node2] = [G[node1][node2], node1]
                    elif node2 not in seen:
                        heapq.heappush(frontier, (G[node1][node2], node2, node1))
                        seen[node2] = [G[node1][node2], node1]
    return Z


def sum_it(Z):
    total = 0
    for node1 in Z:
        for node2 in Z[node1]:
            total += Z[node1][node2]
    total /= 2
    return total

               
start = time.time()
G = read_file('edges.txt')
Z = prim(G)
total = sum_it(Z)
total_time = time.time() - start
print Z
print total
print total_time
