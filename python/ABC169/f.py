N,S = list(map(int,input().split()))
A = list(map(int,input().split()))
n = N
k = S
C = []

def bubunnwa(i,sum,b):
    if(i < n):
        b.append(0)
        bubunnwa(i+1,sum,b)
        del b[i:]
        b.append(1)
        bubunnwa(i+1,sum+A[i],b)
    elif(i == n and sum == k):
        C.append(b.copy())

bubunnwa(0,0,[])
ans = 0
for c in C:
    kazu = 0
    for cc in c:
        if cc == 1:
            kazu += 1
    ans += 2 ** (N - kazu)
ans = ans % 998244353
print(ans)