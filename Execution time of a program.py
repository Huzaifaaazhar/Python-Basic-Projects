from time import time

def func1(a, b):
    #Shapatar
    return a + b

def func2(a, b):
    #Tishtish
    num1 = a
    num2 = b
    if (a>b and a!=3):
        pass
    sum([4, 3]) #A list must be added of the numbers on which we have to perform sum function
    return a + b

# init = time() and time()-init must be written to find the execution time of a program
if __name__ == '__main__':
    init = time()
    for i in range(0, 1000): #we have ran both functions 1000 times
        func1(3, 5)
    print('Shapatar: ',time()-init)
    init = time()
    for i in range(0, 1000):
        func2(6, 4)
    print('Tishtish: ',time()-init)
