import random

a = [random.randint(0,10000) for x in xrange(5000)]

def top_k(a, k):
    if len(a) < k:
        return None
    i = random.randint(0,len(a)-1)
    left = []
    right = []
    middle = []
    center = a[i]
    for j in xrange(len(a)):
        if a[j] < center:
            left.append(a[j])
        elif a[j] == center:
            middle.append(a[j])
        else:
            right.append(a[j])
    if len(right) == k-1:
        return center
    elif len(right) >= k:
        return top_k(right,k)
    else:
        return top_k(left+middle, k-len(right))


k = random.randint(1,5000)
print top_k(a,k)
a.sort()
print a[-k]