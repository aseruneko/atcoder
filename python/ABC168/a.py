N = int(input())
i = N % 10
if i in [2,4,5,7,9]:
    o = "hon"
if i in [0,1,6,8]:
    o = "pon"
if i in [3]:
    o = "bon"
print(o)