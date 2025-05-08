import math
n=float(input("Enter the number: "))
f=math.floor(n)
print("Floor of",n,": ",f)
c=math.ceil(n)
print("Ceil of",n,": ",c)

x=15
y=50.5
print("After copysign operation:")
print(math.copysign(x,y))

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
print("GCD of",a,",",b,"is",math.gcd(a,b))