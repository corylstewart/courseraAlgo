import random
import time
a = [10,2,3,22,33,7,4,1,2]
d = []
#with open("IntegerArray.txt") as f:
#    numbers = f.readlines()
#    for number in numbers:
#        d.append(int(number))

def count_merge(a,b):
    c = 0
    d = len(a) + len(b)
    i = 0
    j = 0
    count = 0
    a.sort()
    b.sort()
    while c < d:
        if len(a) == i:
            break
        if len(b) == j:
            break
        if a[i] <= b[j]:
            c += 1
            i+= 1
        else:
            c += 1
            count += len(a)-i
            j+= 1
    return count

def count_inversions(a):
    if len(a) < 2:
        return 0
    left = a[:len(a)/2]
    right = a[len(a)/2:]
    return count_inversions(left) + count_inversions(right) + count_merge(left, right)
  

#print count_inversions(d)

def top_k(a, k):
    middle = a[random.randint(0,len(a)-1)]
    left = []
    center = []
    right = []
    for i in range(len(a)):
        if a[i] == middle:
            center.append(a[i])
        elif a[i] < middle:
            left.append(a[i])
        else:
            right.append(a[i])
    if len(right) == 1:
        return center[0]
    elif len(right) > 1:
        return top_k(right, k)

    print left, center, right


top_k(a,2)
