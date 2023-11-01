sub1 = int(input("Maths: "))
sub2 = int(input("Science: "))
sub3 = int(input("Urdu: "))
sub4 = int(input("English: "))
sub5 = int(input("Computer: "))
tot = (500)
sum1 = sub1+sub2+sub3+sub4+sub5
p = (sum1 * 100)/tot
if (p >= 80)&(p < 100):
    print("Grade is A+")
elif (p >= 70)&(p < 80):
    print("Grade is A")
elif (p >= 60)&(p < 70):
    print("Grade is B")
elif (p >= 50)&(p < 60):
    print("Grade is C")
elif (p >= 40)&(p < 50):
    print('Grade is D')
else:
    print("Fail")
