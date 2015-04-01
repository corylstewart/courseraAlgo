def read_file(filename):
    nodes = list()
    heads = dict()
    with open(filename) as f:
        f.readline()
        for line in f.readlines():
            node = line.replace(' ', '').strip()
            heads[node] = node
            nodes.append(node)
    return nodes, heads

def get_head(heads, node):
    head = heads[node]
    while heads[head] != head:  #walk up the parents to find the head
        head = heads[head]
    return head

def invert(bit):
    if bit == '0':
        return '1'
    else:
        return '0'


def two_steps(node):
    '''creates a list of nodes that are two steps away from node'''
    nodes = list()
    for i in range(len(node)):
        one_step = node[:i]  + invert(node[i]) + node[i+1:]
        nodes.append(one_step)
        for j in range(i+1, len(node)):
            two_step = node[:i] + invert(node[i]) + node[i+1:j] + \
                invert(node[j]) + node[j+1:]
            nodes.append(two_step)
    return nodes

def make_clusters(nodes, heads):
    print 'starting'
    clusters = len(heads)
    for node in nodes:
        head1 = get_head(heads, node)
        for neighbor in two_steps(node):
            if neighbor in heads:
                head2 = get_head(heads, neighbor)
                if head1 != head2:
                    heads[head2] = head1
                    clusters -= 1
                    if clusters%10000 == 0:
                        print clusters
    return clusters


nodes, heads = read_file('clustering_big.txt')

print make_clusters(nodes, heads)
print 'done'