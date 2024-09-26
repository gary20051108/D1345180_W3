import math
n=int(input("請輸入一個數"))
a=int(n//100)
b=int(math.floor(n/10)-a*10)
c=int(n-math.floor(n/10)*10)
print(a+b+c)