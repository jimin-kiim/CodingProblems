# import math
a,b = map(int, input().split())
# print(math.lcm(a,b))
i = max(a,b)
while(1):
    if i%a ==0 and i%b ==0 :
        print(i)
        break
    i+=1