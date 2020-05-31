N = input()
A = list(map(int, input().split()))
A.sort()
o = 1
for a in A:
    o = o * a
    if o > 10 ** 18:
        o = -1
        break
print(o)