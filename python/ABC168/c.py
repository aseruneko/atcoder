import math

A,B,H,M = list(map(float,input().split()))

hm = H + M / 60
h = hm * 30
m = M * 6

sa = abs(h - m)
ans = (A**2 + B**2 - A * B * math.cos(math.radians(sa)) * 2) ** 0.5


# if int(sa) == 0:
#     if int(h) == int(m):
#         ans = abs(A - B)
#     else:
#         ans = A + B

print(ans)