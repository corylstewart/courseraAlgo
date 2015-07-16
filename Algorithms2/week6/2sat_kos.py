import sys
sys.setrecursionlimit(10**6)
import time
#import resource
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

def make_graph(filename):
    G = dict()
    G_rev = dict()
    with open(filename) as f:
        total = f.readline()
        for line in f.readlines():
            nodes = [int(x) for x in line.split()]
            add_nodes(nodes, G, G_rev)
    return G, G_rev

def add_nodes(nodes, G, G_rev):
    a = nodes[0]
    b = nodes[1]
    if -a not in G:
        G[-a] = dict()
    if -b not in G:
        G[-b] = dict()
    if a not in G_rev:
        G_rev[a] = dict()
    if b not in G_rev:
        G_rev[b] = dict()
    G[-a][b] = 1
    G[-b][a] = 1
    G_rev[b][-a] = 1
    G_rev[a][-b] = 1



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
    return len_list

files = ['good.txt', 'bad.txt', '2sattest.txt', '2sattest2.txt', '2sat1.txt',
        '2sat2.txt', '2sat3.txt', '2sat4.txt', '2sat5.txt', '2sat6.txt']

for file in files:
    print 'working...'
    start = time.time()
    G, G_rev = make_graph(file)
    new_ordering = rev_G(G_rev)
    my_scc = scc(G, G_rev, new_ordering)
    good = True
    for key in my_scc:
        if -key == my_scc[key]:
            good = False
            break
    print file, good, time.time()-start
