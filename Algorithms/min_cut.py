import random
import copy

karger_data = []
with open('kargerMinCut.txt') as f:
    for line in f.readlines():
        karger_data.append(line)


def make_graph(data):
    nodes = dict()
    edges = dict()
    for line in data:
        numbs = [int(x) for x in line.split()]
        nodes[numbs[0]] = dict()
        for numb in numbs[1:]:
            if numb not in nodes[numbs[0]]:
                nodes[numbs[0]][numb] = 0
            nodes[numbs[0]][numb] += 1
            if numb < numbs[0]:
                edges[len(edges)] = (numb, numbs[0])

    return nodes, edges

my_data = ['1 2 3 4', '2 1 3', '3 1 2 6', '4 1 5 6', '5 4 6', '6 3 4 5']
def check_valid(nodes):
    for node in nodes:
        for node2 in nodes[node]:
            if node not in nodes[node2] and node != node2:
                print node, node2
                print 'bad'

def remove_edge(nodes, edges, edge):
    node1 = edges[edge][0]
    node2 = edges[edge][1]
    for node in nodes[node2]:
        if node not in nodes[node1]:
            nodes[node1][node] = 0
        nodes[node1][node] += 1
        if node1 not in nodes[node]:
            nodes[node][node1] = 0
        nodes[node][node1] += 1
        next_key = max(edges.keys())+1
        nodes[node].pop(node2, None)
    for edgey in edges:
        if node2 == edges[edgey][0]:
            if node1 < edges[edgey][1]:
                edges[edgey] = (node1, edges[edgey][1])
            else:
                edges[edgey] = (edges[edgey][1], node1)
        if node2 == edges[edgey][1]:
            if node1 < edges[edgey][0]:
                edges[edgey] = (node1, edges[edgey][0])
            else:
                edges[edgey] = (edges[edgey][0], node1)
        rem = list()
    for ed in edges:
        if edges[ed][1] == edges[ed][0]:
            rem.append(ed)
    for k in rem:
        edges.pop(k, None)

    edges.pop(edge, None)
    nodes.pop(node2, None)
    nodes[node1].pop(node2, None)
    if node1 in nodes[node1]:
        nodes[node1].pop(node1, None)
    return nodes, edges


curr_low = float('inf')

old_nodes, old_edges = make_graph(karger_data)
for i in range(200):
    if i%100 == 0:
        print i
    nodes = copy.deepcopy(old_nodes)
    edges = copy.deepcopy(old_edges)
    while len(nodes) > 2:
        edge = random.choice(edges.keys())
        nodes, edges = remove_edge(nodes, edges, edge)
        #check_valid(nodes)
    if len(edges) < curr_low:
        curr_low = len(edges)
        print curr_low, nodes


print 'done', curr_low