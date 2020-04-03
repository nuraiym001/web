n = int(input())
i = 0
p = 0
a = 1

while(a < n):
    while(i <= p):
        a *= 2
        i += 1
    p += 1

if(a == n):
    print("YES")
else:
    print("NO")
