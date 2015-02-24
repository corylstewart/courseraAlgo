def make_array(filename):
    A = list()
    with open(filename) as f:
        for line in f.readlines():
            A.append(int(line))
    A.sort()
    B = set(A)
    return A

def two_sum(A, low, high):
    i = 0
    j = len(A) - 1
    count = []
    while A[i] < high:
        j_curr = j
        if A[i] + A[j_curr] < low:
            i += 1
        else:
            while A[i] + A[j_curr] > low:
                if A[i] + A[j_curr] > high:
                    j -= 1
                else:
                    count.append(A[i] + A[j_curr])
                j_curr -= 1
            i += 1
    return len(set(count))



A = make_array('algo1-programming_prob-2sum.txt')
print two_sum(A, -10000, 10000)