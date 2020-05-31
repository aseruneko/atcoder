import statistics

N = int(input())
A = []
B = []
for i in range(N):
    ab = list(map(int, input().split()))
    A.append(ab[0])
    B.append(ab[1])
if N % 2 == 0:
    o = int((statistics.median(B) - statistics.median(A)) * 2 + 1)
else:
    o = int(statistics.median(B) - statistics.median(A) + 1)
print(o)