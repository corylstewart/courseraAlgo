
M = [[.5,.5,0],[.5,0,1],[0,.5,0]]

def matrix_multiply(A, R):
    R2 = []
    for i in range(len(A)):
        R2.append(A[i]*R[i])
    return R2


def power_iteration(M, R, sigma=.01):
    R2 = []
    for row in M:
        R2.append(sum(matrix_multiply(row, R)))
    if compare_Rs(R, R2) < sigma:
        return R2
    else:
        return power_iteration(M, R2)

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
