import random
import math

def top_k(a, k):
    global count
    count += len(a)
    if len(a) < k:
        return None
    i = random.randint(0,len(a)-1)
    left = []
    right = []
    center = a[i]
    right.append(center)
    for j in xrange(len(a)):
        if i == j:
           pass
        elif a[j] < center:
            left.append(a[j])
        elif a[j] == center:
            k -= 1
        else:
            right.append(a[j])
    if len(right) == k:
        return center
    elif len(right) > k:
        return top_k(right,k)
    else:
        return top_k(left, k-len(right))

for i in range(100):
    a = [random.randint(0,10000) for x in xrange(5000)]
    a = set(a)
    a = list(a)
    count = 0
    k = random.randint(1,len(a))
    x = top_k(a,k)
    a.sort()
    y = a[-k]
    if x != y:
        print k, a
print 'done'