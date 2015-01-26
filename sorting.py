import random

a = [6,3,7,4,6,8,2,6,43,-99,1]

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