'''[Posted January 12th] You are given a sorted (from smallest to largest) 
array A of n distinct integers which can be positive, negative, or zero. 
You want to decide whether or not there is an index i such that A[i] = i. 
Design the fastest algorithm that you can for solving this problem. '''
import random
a = [-5, -3, 0, 1, 2]
b = [-4, -2, -1, 0]



def i_equals_index(a, index_start=0):
    if a[0] == index_start:
        print a[0]
        return True
    if len(a) > 1:
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
    if len(a) > 1:
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
        if i != len(a) and -i-1 == a[-i-1]:
            print -i-1, 'brute'
            return True
    return False

print does_index_match(a)
print does_index_match(b)


for i in range(1000):
    a = [random.randint(-100, 100) for x in range(50)]
    a = set(a)
    a = list(a)
    a.sort()
    y =  brute_force(a)
    if y:
        x = does_index_match(a)
        if x is None:
            x = False