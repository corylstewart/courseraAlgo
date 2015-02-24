import heapq

def read_file(filename):
    A = list()
    with open(filename) as f:
        for line in f.readlines():
            A.append(int(line))
    return A

def median_main(A):
    left = list()  #create the min side of the list
    right = list()  #create the max side of the list
    median = A[0]  #first element is a median
    heapq.heappush(right, A[0])  #add the first element to the max side
    for i in range(1,len(A)):
        if A[i] < right[0]:  #if the next element is smaller then the min of the max
            heapq.heappush(left, -A[i])  #add it to the min side heap
        else:
            heapq.heappush(right, A[i])  #else add it to the max side heap
        if len(left) - len(right) >=2:  #balance the size of the heaps so that the two heaps
            q = heapq.heappop(left)  #are the same size or the min heap is one element larger
            heapq.heappush(right, -q)
        elif len(right) - len(left) >=1:
            q = heapq.heappop(right)
            heapq.heappush(left, -q)
        median = (median + -left[0])%10000  #add the max of the min heap to the nedian
    return median

def other_median(A):
    x = []
    median = 0
    for z in A:
        x.append(z)
        x.sort()
        median = (median+x[(len(x)-1)/2])%10000
    return median



A = read_file('Median.txt')
print median_main(A)
print other_median(A)