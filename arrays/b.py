a = []
n = int(input())
a = [int(s) for s in input().split()]
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i])