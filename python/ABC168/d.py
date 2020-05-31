N,M = list(map(int,input().split()))
A,B = [],[]
for i in range(M):
    ab = list(map(int,input().split()))
    A.append(ab[0])
    B.append(ab[1])

load = [0] * (N + 1)



print(N,M,A,B)