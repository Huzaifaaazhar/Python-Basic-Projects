'''create a program in python that use resursion to the string
    "PYTOHN" to
    P
    Y
    T
    H
    O
    N
'''


def linear_print(n):
    if n:
        print(n[0])
        linear_print(n[1:])


linear_print('PYTHON')
