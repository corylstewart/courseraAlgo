import random


def pprint_grid(grid):
    for row in grid:
        print '\t'.join('{0:3d}'.format(x) for x in row)

def local_min(grid, i=None, j=None):
    if i is None:
        i = len(grid)/2
        j = i
    #print i,j
    global count
    count += 1
    if check_north(grid, i, j):
        return local_min(grid, i-1, j)
    count += 1
    if check_south(grid, i, j):
        return local_min(grid, i+1, j)
    count += 1
    if check_west(grid, i, j):
        return local_min(grid, i, j-1)
    count += 1
    if check_east(grid, i, j):
        return local_min(grid, i, j+1)
    return i, j
    

def check_north(grid, i, j):
    if i == 0:
        return False
    return grid[i-1][j] < grid[i][j]

def check_south(grid, i, j):
    if i == len(grid) - 1:
        return False
    return grid[i+1][j] < grid[i][j]

def check_west(grid, i, j):
    if j == 0:
        return False
    return grid[i][j-1] < grid[i][j]

def check_east(grid, i, j):
    if j == len(grid) - 1:
        return False
    return grid[i][j+1] < grid[i][j]

for k in range(100000):
    if k%1000 == 0:
        print k
    
    b = [x for x in range(1000)]

    a = [[b.pop(random.randint(0,len(b)-1)) for x in range(20)] for z in range(20)]
    count = 0
   
    i, j = local_min(a)
    if count > len(a):
        pprint_grid(a)
        print i, j, count
        print 'bad something happened'
        break
print 'done'