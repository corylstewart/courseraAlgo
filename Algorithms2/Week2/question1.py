import heapq

def make_graph_from_file(filename):
    heap = list()
    with open(filename) as f:
        f.readline()
        for line in f.readlines():
            data = line.split()
            node1 = int(data[0])
            node2 = int(data[1])
            edge_cost = int(data[2])
            heap.append((edge_cost, [node1, node2]))
    heapq.heapify(heap)
    print 'graph done'
    return heap

def find_node(graphs, node):
    for i in range(len(graphs)):
        if node in g[i]:
            return i
    return none

def make_union(graphs, i, j):
    if len(i) > len(j):
        graphs[i].update(graphs[j])
        graphs.pop(j)
    else:
        graphs[j].update(graphs[i])
        graphs.pop(i)
    return graphs

def make_graphs(heap):
    graphs = list()
    seen = list()
    for edge in heap:
        if edge[1][0] not in seen:
            seen.append(edge[1][0])
            graphs.append({edge[1][0]:1})
        if edge[1][1] not in seen:
            seen.append(edge[1][1])
            graphs.append({edge[1][1]:1})
    return graphs

def k_cluster(heap, num_clusters):
    graphs = make_graphs(heap)
    while len(graphs) > k:
        pass

heap = make_graph_from_file('clustering1.txt')
k = 4
k_cluster(heap, k)