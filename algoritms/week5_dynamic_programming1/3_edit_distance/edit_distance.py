import array
import numpy as np
# Uses python3
def edit_distance(A, B):
    D = np.zeros((len(A) , len(B)))
    n = len(A)
    m = len(B)
    D[:, 0] = range(n )
    D[0, :] = range(m)
    for j in range(1, m):
        for i in range(1, n):
            insertion = D[i, j-1] + 1
            deletion = D[i-1,j] + 1
            match = D[i-1, j-1]
            mismatch = D[i-1, j-1] + 1
            if(A[i] == B[j]):
                D[i,j]=min(insertion,deletion,match)
            else:
                D[i,j]=min(insertion,deletion,mismatch)
    return D[n-1,m-1]

if __name__ == "__main__":
    A=['0']
    B=['0']
    data = input()
    A.extend(data)
    data = input()
    B.extend(data)
    print(int(edit_distance(A,B)))

