'''[Posted January 12th] You are given a sorted (from smallest to largest) 
array A of n distinct integers which can be positive, negative, or zero. 
You want to decide whether or not there is an index i such that A[i] = i. 
Design the fastest algorithm that you can for solving this problem. '''
import random
import time
a = [-5, 6, 7, 8, 9]
b = [-4, -2, -1, 0]



def i_equals_index(a, index_start=0):
    #print a, index_start
    if a[0] == index_start:
        print a[0]
        return True
    if len(a) > 1 and a[0] < index_start:
        center_index = len(a)/2
        left = a[:center_index]
        right = a[center_index:]
        if right[0] <= index_start+center_index:
            if i_equals_index(right, index_start+center_index):
                return True
        if len(left) > 0:
            if i_equals_index(left, index_start):
                return True

def i_equals_negative_index(a, index_reverse=-1):
    #print a, index_reverse
    if a[-1] == index_reverse:
        print a[-1]
        return True
    if len(a) > 1 and a[-1] > index_reverse:
        center_index = (len(a)/2)
        left = a[:center_index]
        right = a[center_index:]
        #print left, right, index_reverse
        if right[-1] >= index_reverse:
            if i_equals_negative_index(right, index_reverse):
                return True
        if len(left) > 0:
            if len(a)%2 == 1:
                center_index += 1
            if i_equals_negative_index(left, index_reverse-center_index):
                return True

def does_index_match(a):
    return i_equals_index(a) or i_equals_negative_index(a)

def brute_force(a):
    for i in range(len(a)):
        if i == a[i]:
            print i, 'brute'
            return True
        elif i != len(a) and -i-1 == a[-i-1]:
            print -i-1, 'brute'
            return True
    return False

def other_way(a):
    for i in xrange(len(a)):
        if a[i] > i:
            break
        elif a[i] == i:
            print i, 'other'
            return True
    for i in xrange(len(a)):
        if a[-i-1] < -i-1:
            break
        elif a[-i-1] == -i-1:
            print -i-1, 'other'
            return True
    return False



#print other_way(a)
#print does_index_match(b)
fast = 0
slow = 0
maybe = 0


for i in range(10000):
    if i%100 == 0:
        print i
    low = random.randint(-1000000, 1000000)
    high = random.randint(-1000000, 1000000)
    if high < low:
        low, high = high, low
    a = [random.randint(low, high) for x in range(5000)]
    a = set(a)
    a = list(a)
    a.sort()

    #start = time.time()
    #x = does_index_match(a)
    #fast += time.time() - start
    start = time.time()
    y =  brute_force(a)
    slow += time.time() - start
    start = time.time()
    z =  other_way(a)
    maybe += time.time() - start

print fast
print slow
print maybe