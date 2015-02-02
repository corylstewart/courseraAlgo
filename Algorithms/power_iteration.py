M = [[.1,.45,.45],
     [.1,.1,.8],
     [.8,.1,.1]]

def matrix_multiply(A, R):
    R2 = []
    for i in range(len(A)):
        R2.append(A[i]*R[i])
    return R2


def power_iteration(M, R, count = 0, sigma=.00001, beta=.9):
    count += 1
    if count > 50:
        return R
    R2 = []
    for row in M:
        R2.append(sum(matrix_multiply(row, R)))
    if compare_Rs(R, R2) < sigma:
        return R2
    else:
        return power_iteration(M, R2, count)

def make_R(M):
    R = []
    for i in range(len(M)):
        R.append(1./len(M))
    return R

def compare_Rs(R, R2):
    sigma = 0
    for i in range(len(R)):
        sigma += abs(R[i] - R2[i])
    return sigma


print power_iteration(M, make_R(M))
