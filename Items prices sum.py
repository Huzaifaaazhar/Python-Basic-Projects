#You are a shopkeeper and you have to design a utility to sum the price of
#items until user presses q.


sum = 0
while(True):
    num = input("Enter the price: ")

    if (num != 'q'):
        sum = sum + int(num)
        print(f"Total order so far: {sum}")

    else:
        print(f"Your Total Bill is: {sum}")
        break
