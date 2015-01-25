import random

a = [1,2,3,4,5,100,45,34,67,43,-100]

def top_k(a, k):
    i = random.randint(0,len(a)-1)
    left = []
    right = []
    middle = []

print top_k(a,2)