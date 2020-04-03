import math
i=0
a=int(input())
while i < a:
    i+=1
    if i == (int(math.sqrt(i)) ** 2):
        print(i)