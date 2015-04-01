def make_graph_from_file(filename):
    '''creates a sorted list of edges of the form (cost, [node1, node2])
    and a ditionary of nodes with parent pointing to itself'''
    edges = list()
    nodes = dict()
    with open(filename) as f:
        f.readline()
        for line in f.readlines():
            data = line.split()
            node1 = int(data[0])
            node2 = int(data[1])
            edge_cost = int(data[2])
            edges.append((edge_cost, [node1, node2]))
            nodes[node1] = node1
            nodes[node2] = node2
    edges.sort()
    print 'graph done'
    return edges, nodes

def get_head(nodes, node):
    head = nodes[node]
    while nodes[head] != head:  #walk up the parents to find the head
        head = nodes[head]
    return head

def k_cluster(edges, nodes, k=4):
    clusters = len(nodes)  #set intial number of clusters
    for edge in edges:
        head1 = get_head(nodes, nodes[edge[1][0]])
        head2 = get_head(nodes, nodes[edge[1][1]])
        if head1 != head2:  #make sure we are not already in the same cluster
            if clusters <= k:  #if we are at the maximum count of clusters
                return edge[0]  #return current edge cost
            nodes[head2] = head1  #set new parent head
            clusters -= 1  #decriment the cluster count




edges, nodes= make_graph_from_file('clustering1.txt')
cost = k_cluster(edges, nodes)
print cost
