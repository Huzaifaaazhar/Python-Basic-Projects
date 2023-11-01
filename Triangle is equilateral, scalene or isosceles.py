print("A triangle has three sides")
a=int(input())
b=int(input())
c=int(input())
if (a==b==c):
    print("Equilateral triangle")
elif (a==b!=c)or(a==c!=b)or(b==c!=a):
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    
