def displayMatrix(matrix):
    NumberOfRows=len(matrix)
    NumberOfColumns=len(matrix[0])
    for r in range (NumberOfRows):
        for c in range(NumberOfColumns):
            print(matrix[r][c],end ="\t")
        print()
        
def inputMatrix():
    NumberOfRows= int(input("Enter the number of rows:"))
    NumberOfColumns= int(input("Enter the number of columns:"))
    matrix =[]
    print("Enter the entries rowwise:")
    for r in range(NumberOfRows):		 
            Row=[]
            for c in range(NumberOfColumns):	 
                    Row.append(float(input("Enter a Element:")))
            matrix.append(Row)
    return (matrix)        

def makePivotOne(matrix,pivotRow,pivotColumn):
    numberOfCols=len(matrix[0])
    pivotElement=matrix[pivotRow][pivotColumn]
    for c in range(numberOfCols):
        matrix[pivotRow][c]=matrix[pivotRow][c]/pivotElement
    return matrix
def makePivotColZero(M,pr,pc):
    nr=len(M)
    nc=len(M[0])
    for r in range(nr):
        if (r!=pr):
            const=M[r][pc]
            for c in range(nc):
                M[r][c]=M[r][c]-const*M[pr][c]
    return (M)            

M=inputMatrix()
displayMatrix(M)
pr=int(input("Enter pivot row number:"))
pc=int(input("Enter pivot column number:"))
pr -=1
pc -=1
while (pr>=0 and pc>=0):
    if (M[pr][pc]==0):
        print("Pivot Element Can not be zero.Re Enter")
        pr=int(input("Enter pivot row number:"))
        pc=int(input("Enter pivot column number:"))
        pr -=1
        pc -=1
        continue
    M=makePivotOne(M,pr,pc)
    M=makePivotColZero(M,pr,pc)
    displayMatrix(M)
    pr=int(input("Enter pivot row number:"))
    pc=int(input("Enter pivot column number:"))
    pr -=1
    pc -=1
