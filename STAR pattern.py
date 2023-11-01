n = int(input("Enter rows: "))
c = int(input("Enter columns: "))
for i in range(1, n+1):
    for j in range(1, c+1):
        if (i==1 or i==n or j==1 or j==c):
            print("*", end="")
        else:
            print(" ", end="")
    print()
