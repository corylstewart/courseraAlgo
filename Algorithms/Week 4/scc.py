edges = [(1,7), (7,4), (4,1), (7,9), (9,6), (6,3), (3,9), (6,8), (8,2), (2,5), (5,8)]
G = dict()
G_rev = dict()
for edge in edges:
    node1 = edge[0]
    node2 = edge[1]
    if node1 != node2:
        if node2 not in G:
            G[node2] = dict()
        G[node2][node1] = 1
        if node1 not in G_rev:
            G_rev[node1] = dict()
        G_rev[node1][node2] = 1


def make_big_G():
    G = dict()
    G_rev = dict()


    with open('SCC.txt') as f:
        for line in  f.readlines():
                nodes = [int(x) for x in line.split()]
                node1 = nodes[0]
                node2 = nodes[1]
                if node1 != node2:
                    if node1 not in G:
                        G[node1] = dict()
                    G[node1][node2] = 1
                    if node2 not in G_rev:
                        G_rev[node2] = dict()
                    G_rev[node2][node1] = 1

    return G, G_rev

#G, G_rev = make_big_G()
def make_ordering(G_rev, start_node, seen, new_ordering, count):
    seen.append(start_node)
    for node2 in G_rev[start_node]:
        if node2 not in seen:
            count = make_ordering(G_rev, node2, seen, new_ordering, count)
    new_ordering[count] = start_node
    count += 1
    return count


def rev_G(G_rev):
    seen = []
    new_ordering = dict()
    k = G_rev.keys()
    k.sort(reverse=True)
    count = 1
    for node in k:
        if node not in seen:
            count = make_ordering(G_rev, node, seen, new_ordering, count)
    return new_ordering

def straight_G(G, start_node, seen, scc_cluster, parent):
    seen.append(start_node)
    print start_node
    for node2 in G[start_node]:
        raw_input()
        if node2 not in seen:
            straight_G(G, node2, seen, scc_cluster, parent)
    scc_cluster[node2] = parent
    print scc_cluster

def scc(G, G_rev):
    new_ordering = rev_G(G_rev)
    seen = []
    scc_cluster = dict()
    k = new_ordering.keys()
    k.sort(reverse=True)
    print k
    for node in k:
        straight_G(G, new_ordering[node], seen, scc_cluster, new_ordering[node])
    print scc_cluster



scc(G, G_rev)