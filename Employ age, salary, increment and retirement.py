def employ(age, salary, joinyear):
    if (age>0) and (age<60):
        d = 60 - age
        reyr = d + joinyear
        print("Retirement year is: ",reyr)
        totsal = salary * 12
        bonus = totsal * (10/100)
        increment = salary * 0.1
        print("Increment: ", increment)
        return("Bonus: ",bonus)

age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
joinyear = int(input("Enter year of joining: "))
c = employ(age, salary, joinyear)
print(c)
