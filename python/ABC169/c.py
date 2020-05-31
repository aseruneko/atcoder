from decimal import Decimal

A,B = input().split()
A = Decimal(A)
B = Decimal(B)
o = int(A * B)
print(o)