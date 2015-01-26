import random

a = [3,7,4,66,8,2,6,43,-99,1]

def quick_sort(a):
    if len(a) < 2:
        return a
    pivot = random.randint(0,len(a)-1)
    left = list()
    middle = list()
    right = list()
    piv_elem = a[pivot]
    for i in xrange(len(a)):
        if a[i] < piv_elem:
            left.append(a[i])
        elif a[i] > piv_elem:
            right.append(a[i])
        else:
            middle.append(a[i])
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_in_place(a):
    if len(a) < 2:
        return a
    pivot = random.randint(0,len(a)-1)
    a[0], a[pivot] = a[pivot], a[0]
    i = 1
    j = 1
    while j < len(a):
        if a[j] < a[0]:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    return quick_sort_in_place(a[1:i]) + [a[0]] + quick_sort_in_place(a[i:]) 

def make_pivot(a):
    return 

print quick_sort_in_place(a)