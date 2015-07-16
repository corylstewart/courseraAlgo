import numpy as np
import sys
maximum = 1000000

# Floyd-Warshall algorithm to solve All-Pairs Shortest Paths problem
def fw(graph,n,m):
    # initialize the A matrix
    a = np.ones((n,n),dtype=np.int)*maximum
    for i in range(n):
        a[i,i]=0
    for i in range(m):
        a[graph[i,0],graph[i,1]] = graph[i,2]
    print "# start searching shortest path"
    # start to search all shortest paths
    for k in range(1,n):
        for i in range(n):
            a[i,:] = np.amin([a[i,:],a[i,k]+a[k,:]],axis=0)
            # check negative cycles
            if a[i,i]<0:
                print "error in",i,k
                exit()
    # output
    print "shortest path length:",a[:,:].min()

if __name__ == "__main__":
    n,m = np.int_(np.fromfile(sys.argv[1],count=2,sep=' '))
    graph = np.int_(np.loadtxt(sys.argv[1],skiprows=1))
    graph[:,0] = graph[:,0]-1
    graph[:,1] = graph[:,1]-1
    fw(graph,n,m)