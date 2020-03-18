a = []
sum = 0
n = int(input())
a = [int(s) for s in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        sum+=1
print(sum)