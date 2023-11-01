a = [4,1,5,6,7,0,2,89]
print(a)
for i in range(len(a)-1):
    minimum = min(a[i:])
    index = a.index(minimum, i)
    if a[i]!= a[index]:
        a[i],a[index] = a[index],a[i]
    print(a)
