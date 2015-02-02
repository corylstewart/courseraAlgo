import numpy as np
import math


'''Problem 1 Week 1'''
beta = .7
M = np.matrix([[0, 0, 0],
               [.5, 0, 0],
               [.5, 1., 1.]])

r = np.matrix([1./3, 1./3, 1./3]).T

S = np.matrix([(1-beta)/3, (1-beta)/3, (1-beta)/3]).T


def power_iteration(M, r, S, beta, epsilon=.00001):
    r2 = beta * M * r + S
    if math.fabs((r2-r).max()) < epsilon:
        return r2
    else:
        return power_iteration(M, r2, S, beta)


r = power_iteration(M, r, S, beta)
r *= 3
a = r.flat[0]
b = r.flat[1]
c = r.flat[2]

print 'Problem 1'
print 'a = ', a
print 'b = ', b
print 'c = ', c
print 'a + b = ', a + b
print 'a + c = ', a + c
print ''


'''Problem 2 Week 1'''
beta = .85
M = np.matrix([[0, 0, 1.],
               [.5, 0, 0],
               [.5, 1, 0]])

r = np.matrix([1./3, 1./3, 1./3]).T

S = np.matrix([(1-beta)/3, (1-beta)/3, (1-beta)/3]).T

r = power_iteration(M, r, S, beta)
a = r.flat[0]
b = r.flat[1]
c = r.flat[2]

print 'Problem 2'
print 'a = ', a
print 'b = ', b
print 'c = ', c
epsilon = .00001
print 'b = .575a + .15c', abs(b - (.575*a + .15*c)) <= epsilon
print 'b = .475a + .05c', abs(b - (.475*a + .05*c)) <= epsilon
print '.95a = .9c + .05b', abs(.95*a - (.9*c + .05*b)) <= epsilon
print 'a = c + .15b', abs(a - (c + .15*b)) <= epsilon
print ''

'''Problem 3 Week 1'''
beta = .85
M = np.matrix([[0, 0, 1.],
               [.5, 0, 0],
               [.5, 1, 0]])

r = np.matrix([1, 1, 1]).T

S = np.matrix([(1-beta)/3, (1-beta)/3, (1-beta)/3]).T



def no_taxation(M, r, S, beta, count=0, epsilon=.00001):
    r2 = M * r
    if count == 4:
        print 'Fifth iteration'
        print 'a = ', r2.flat[0]
        print 'b = ', r2.flat[1]
        print 'b = ', r2.flat[2]
    count += 1
    if math.fabs((r2-r).max()) < epsilon:
        return r2
    else:
        return no_taxation(M, r2, S, beta, count)

print 'Problem 3'
r = no_taxation(M, r, S, beta)
a = r.flat[0]
b = r.flat[1]
c = r.flat[2]
print 'At limit'
print 'a = ', a
print 'b = ', b
print 'b = ', c
print ''

'''Problem4 week 1'''
def map(x):
    tups = list()
    prime_facts = prime_factors(x)
    for fact in prime_facts:
        tups.append((fact, x))
    return tups


def prime_factors(x):
    primes = make_primes(x)
    prime_facts = list()
    for prime in primes:
        if x%prime == 0:
            prime_facts.append(prime)
    return prime_facts

def make_primes(x):
    primes = [2]
    for i in range(3,x+1):
        is_prime = True
        for prime in primes:
            if i%prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print 'Problem 4 Week 1'
nums = [15, 21, 24, 30, 49]
to_reduce = list()
reduced = dict()
for num in nums:
    to_reduce += map(num)
for tup in to_reduce:
    if tup[0] not in reduced:
        reduced[tup[0]] = 0
    reduced[tup[0]] += tup[1]
for key in reduced:
    print (key, reduced[key])