a = int(input("Enter number of rows: ")) #taking input number of rows as integer.
b = int(input("Enter number of columns: ")) #taking input number of columns as integer.
matrix = [] #assigning a variable named matrix as an empty list or array
for i in range(a): #Loop for rows.
    c = [] #variable c as an empty list to get values assigned in variable j
    for j in range(b): #Loop for columns
        j = int(input("Enter number in pocket: "+str(i)+" "+str(j)+" ")) #taking input of values for matrix
        c.append(j) #putting values in the empty list C
    print () # giving space of a line
    matrix.append(c)

for i in range(a): #loop to view the matrix
    for j in range(b):
        print(matrix[i][j], end = " ")
    print()
