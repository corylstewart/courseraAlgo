import sys
sys.setrecursionlimit(10**6)

#import resource
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

edges = [(1,7), (7,4), (4,1), (7,9), (9,6), (6,3), (3,9), (6,8), (8,2), (2,5), (5,8), (5,10)]
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

G, G_rev = make_big_G()
def make_ordering(G_rev, start_node, seen, new_ordering, count, depth=0):
    #print depth, start_node, start_node in seen
    depth += 1
    seen.append(start_node)
    if start_node in G_rev:
        for node2 in G_rev[start_node]:
            if node2 not in seen:
                count = make_ordering(G_rev, node2, seen, new_ordering, count, depth)
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
            #print node, new_ordering
            #raw_input()
            count = make_ordering(G_rev, node, seen, new_ordering, count)
    return new_ordering

def straight_G(G, start_node, seen, scc_cluster, parent):
    if start_node not in seen:
        seen.append(start_node)
        if start_node in G:
            scc_cluster[start_node] = parent
            #print scc_cluster
            #print start_node, seen
            for node2 in G[start_node]:
                #raw_input()
                if node2 not in seen:
                    straight_G(G, node2, seen, scc_cluster, parent)

def scc(G, G_rev, new_ordering):
    #print new_ordering
    seen = []
    scc_cluster = dict()
    k = new_ordering.keys()
    k.sort(reverse=True)
    #print k
    for node in k:
        straight_G(G, new_ordering[node], seen, scc_cluster, new_ordering[node])
    return scc_cluster

def make_scc_in_order(G, G_rev):
    new_ordering = rev_G(G_rev)
    print 'made new ordering'
    raw_input()
    my_scc = scc(G, G_rev, new_ordering)
    print 'done with my scc'
    scc_dict = dict()
    for node in my_scc:
        if my_scc[node] not in scc_dict:
            scc_dict[my_scc[node]] = list()
        scc_dict[my_scc[node]].append(node)
    len_list = list()
    for key in scc_dict:
        l = len(scc_dict[key])
        len_list.append((l, key))
    len_list.sort(reverse=True)
    return len_list[:10]

print 'made it'
#l = make_scc_in_order(G, G_rev)
#for t in l[:10]:
#    print t
print len(G)