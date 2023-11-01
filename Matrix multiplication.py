def inMatrix(m, n):
    a = []
    for i in range(m):
        b=[]
        for j in range(n):
            j=int(input("Enter number in pocket ["+str(i)+"]["+str(j)+"]"))
            b.append(j)
        a.append(b)
    return a

def pMatrix(a):
    for i in range(len(a)): #Number of rows.
        for j in range(len(a[0])): #Number of columns.
            print(a[i][j],end=" ")
        print()

def multiply(a, b):
    mul = []
    sum = 0
    for i in range(len(a)):
        l = []
        for j in range(len(a[0])):
            for k in range(len(b)):
                sum+=a[i][k]*b[k][j]
                l.append(sum)
                sum=0
        mul.append(l)
    return mul

print("First Matrix")
m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns: "))
a=inMatrix(m, n)
print("Second Matrix")
p=int(input("Enter number of rows: "))
q=int(input("Enter number of columns: "))
b=inMatrix(p, q)
c=multiply(a, b)
print("First Matrix......")
pMatrix(a)
print("Second Matrix.....")
pMatrix(b)
print("Multiplication of Two Matrix")
pMatrix(c)
