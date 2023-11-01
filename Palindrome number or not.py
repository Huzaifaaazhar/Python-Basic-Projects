#Take Input
number = int(input("Enter your Number: "))
temp = number
reverse = 0
while(number>0):
    dig = number%10 #To pick the last digit from the given number
    reverse = reverse * 10 + dig #to put the last number at first place
    number = number//10 #to consider the second last(third, fourth and so on) digit from the given number

print(reverse)

if temp == reverse:
    print("Number is Palindrome")

else:
    print("Number is not Palindrome")
