class Animal(object):
    def __init__(self):
        self.eyes = 2
        self.color = 'Red'
        self.name = 'Cosmelan'
        self.legs = 5
        self.age = 'Maloon nahi'
        self.kids = '2 hi ache'

animal = Animal()
animal.tail = 1
temp = vars(animal)
for item in temp:
    print(item,':',temp[item])
