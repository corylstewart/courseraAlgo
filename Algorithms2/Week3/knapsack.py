import sys
from operator import itemgetter
import time

sys.setrecursionlimit(99000) 

def get_items(filename):
    items = list()
    with open(filename) as f:
        capacity = [int(x) for x in f.readline().split()][0]
        for item in f.readlines():
            items.append([int(x) for x in item.split()])
            items[-1].append(float(items[-1][0])/items[-1][1])
    #items.sort(reverse=True)
    return capacity, items

def make_array(capacity, items):
    return [[0 for y in range(len(items)+1)] for x in range(capacity+1)]

def make_narrow(capacity):
    return [[0,0] for x in xrange(capacity+1)]

def remove_col(grid):
    new_grid = list()
    for row in grid:
        new_grid.append([row[1], 0])
    return new_grid

def print_grid(grid):
    for row in grid:
        print row
    print ''

#test data
capacity = 6
items = [[3, 4], [2, 3], [4, 2], [4, 3], [1, 5]]

def knapsack(capacity, items):
    grid = make_array(capacity, items)
    i = 0
    while items:
        item = items.pop(0)
        weight = item[1]
        for x in xrange(capacity+1):
            value = 0
            if weight <= x:
                grid[x][i+1] = max((grid[x][i], grid[x-weight][i] + item[0]))
            else:
                grid[x][i+1] = grid[x][i]
        i += 1
    return grid[-1][-1]

def knap_2m(capacity, items):
    grid = make_narrow(capacity)
    while items:
        item = items.pop(0)
        weight = item[1]
        for x in xrange(capacity+1):
            if weight <= x:
                value = item[0]
                grid[x][1] = max(grid[x][0], grid[x-weight][0] + value)
            else:
                grid[x][1] = grid[x][0]
        grid = remove_col(grid)
    return grid[-1][0]

cache = dict()

def knap_rec(capacity, items, i):
    global cache
    if i <= 0 or capacity <= 0:
        return 0
    key = (capacity, i)
    if key in cache:
        return cache[key]
    weight = items[i][1]
    left = knap_rec(capacity, items, i-1)
    if weight <= capacity:
        value = items[i][0]
        bottom = knap_rec(capacity-weight, items, i-1) + value
        new_weight = max(left, bottom)
        cache[key] = new_weight
        return new_weight
    else:
        cache[key] = left
        return left



# nm size array
#capacity, items = get_items('knapsack1.txt')
#print knapsack(capacity, items) #2493893

# 2*m size array
#capacity, items = get_items('knapsack1.txt')
#print knap_2m(capacity, items) #2493893

# using caching and recusion
cache = dict()
#capacity, items = get_items('knapsack1.txt')
#print knap_rec(capacity, items, len(items)-1) #2493893

cache = dict()
capacity, items = get_items('knapsack_big.txt')
print knap_rec(capacity, items, len(items)-1)
