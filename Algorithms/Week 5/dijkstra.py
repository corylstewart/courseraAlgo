import heapq

'''create a dictionary mapping 2 nodes to the distance between nodes'''
def make_graph(filename):
    G = dict()
    with open(filename) as f:
        for line in f.readlines():
            this_line = line.split()
            node = int(this_line.pop(0))
            edges = [x.split(',') for x in this_line]
            G[node] = dict()
            for edge in edges:
                G[node][int(edge[0])] = int(edge[1])
    return G

def dijkstra(G, s, v):
    #create the heap that will tell us which node to explore next
    frontier = list()
    frontier.append((0,s))
    #create the dictionary that will keep the best path distance between nodes
    seen = {s:0}
    #while we have not seen v or there are still shorter paths to explore then the current path to v
    while v not in seen or seen[v] > frontier[0][0]:
        #grab the current min distance
        dist, node = heapq.heappop(frontier)
        for edge in G[node]:
            new_dist = G[node][edge] + dist
            #if edge not in seen add it to the frontier and seen
            if edge not in seen:
                seen[edge] = new_dist
                heapq.heappush(frontier, (new_dist, edge))
            #if edge in seen and the new distance is better then the current path
            #pop the current path out reheapify the heap and add the new shorter path
            #to the heap and update the seen value
            elif new_dist < seen[edge]:
                frontier.remove((seen[edge], edge))
                heapq.heapify(frontier)
                heapq.heappush(frontier, (new_dist, edge))
                seen[edge] = new_dist
    return seen[v]

G = make_graph('dijkstraData.txt')
nodes = [7,37,59,82,99,115,133,165,188,197]
dists = list()
for node in nodes:
    dists.append(dijkstra(G, 1, node))
print dists