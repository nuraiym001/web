a = []
sum = 0
n = int(input())
a = [int(s) for s in input().split()]
for i in range(len(a)):
    if a[i] > 0:
        sum+=1
print(sum)