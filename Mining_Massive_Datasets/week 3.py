'''import numpy as np
import math

print'Question 1'
A = np.matrix([[0,0,1,0,0,1,0,0],
               [0,0,0,0,1,0,0,1],
               [1,0,0,1,0,1,0,0],
               [0,0,1,0,1,0,1,0],
               [0,1,0,1,0,0,0,1],
               [1,0,1,0,0,0,1,0],
               [0,0,0,1,0,1,0,1],
               [0,1,0,0,1,0,1,0]])
D = np.matrix([[2,0,0,0,0,0,0,0],
               [0,2,0,0,0,0,0,0],
               [0,0,3,0,0,0,0,0],
               [0,0,0,3,0,0,0,0],
               [0,0,0,0,3,0,0,0],
               [0,0,0,0,0,3,0,0],
               [0,0,0,0,0,0,3,0],
               [0,0,0,0,0,0,0,3]])
L = D - A
#print 'Sum of A: ', np.sum(A)
#print 'Sum od D: ', np.sum(D)

print 'Question 2'
A = np.matrix([[0,1,1,0,0,0],
               [1,0,0,1,0,1],
               [1,0,0,1,0,0],
               [0,1,1,0,1,0],
               [0,0,0,1,0,1],
               [0,1,0,0,1,0]])

D = np.matrix([[2,0,0,0,0,0],
               [0,3,0,0,0,0],
               [0,0,2,0,0,0],
               [0,0,0,3,0,0],
               [0,0,0,0,2,0],
               [0,0,0,0,0,2]])

L = D - A


print L

eigenvalues, eigenvectors = np.linalg.eig(L)
#print eigenvalues
#print eigenvectors

def hash_it(x):
    return ((3*x)+7)%11

def count_zeros(x):
    if x == 0:
        return 4
    str_x = str(bin(x))
    count = 0
    while str_x[-1] not in ['1', 'b']:
        count += 1
        str_x = str_x[:-1]
    return count

q = [[2,6,8,10],[2,6,8,9],[3,4,8,10],[2,4,6,10]]

for j in q:
    for i in j:
        m = 0
        y = count_zeros(hash_it(i))
        if y > m:
            m = y
    print m

for i in range(1,11):
    print i, bin(hash_it(i)), count_zeros(hash_it(i))'''


