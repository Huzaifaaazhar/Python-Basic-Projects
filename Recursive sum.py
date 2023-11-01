'''Create a program that use resursion to
calculate the sum of the input number EX: 12345 is input,
the answer will be 15.

'''

def sum(n):
    if n<=1:
        return n
    return n + sum(n-1)

print(sum(8))
