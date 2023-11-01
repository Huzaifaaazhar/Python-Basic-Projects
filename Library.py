class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}
        
    def dispalyBook(self):
        print(f"Books in the Library: {self.name}")
        for book in self.bookslist():
            print(book)
    
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("You can take the Book")
        else:
            print(f"Book is already taken by {self.lendDict[book]}")
            
    def addBook(self, book):
        self.bookslist.append(book)
        print("Book has been added to bookslist")
    
    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    l = Library(['Python', '12 rules for life', 'rich dad poor dad', 'harry potter', 'Algorithms'], 'Shapatar Library')
    while(True):
        print(f"Welcome to {l.name}. Enter book name: ")
        print("1. Display book")
        print("2. Lend book")
        print("3. Add book")
        print("4. Return book")
        userChoice = int(input())
        
        if userChoice == 1:
            l.dispalyBooks()
        
        elif userChoice == 2:
            book = input("Enter book to lend: ")
            user = input("Enter your name: ")
            l.lendBook(user, book)
        
        elif userChoice == 3:
            book = input("Enter name of the book to add: ")
            l.addBook(book)
        
        elif userChoice == 4:
            book = input("Enter name of the book to return: ")
            l.returnBook(book)
        
        else:
            print("Invalid Option")
            
        print("Press Q to quit and C to continue")
        userChoice2 = ''
        while(userChoice2 != 'q' and userChoice2 != 'c'):
            userChoice2 = input()
            
            if userChoice2 =='q':
                exit()
            
            elif userChoice2 == 'c':
                continue