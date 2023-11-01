class node:    
    
    def __init__(self, data):
        self.data = data
        self.next = None;

class LinkedList:
    
    def __init__(self):
        self.start = None;
    
    def viewList(self):
        if self.start == None:
            print("Linked List is empty")
        else:
            temp = self.start
            while (temp != None):
                print(temp.data, end=' ')
                temp = temp.next
    
    def deleteFirst(self):
        if (self.start == None):
            print("Linked List is empty")
        else:
            self.start = self.start.next
    
    def insertLast(self,value):
        newNode = node(value)
        if (self.start == None):
            self.start = newNode;
        else:
            temp = self.start
            while (temp.next != None):
                temp = temp.next

myList = LinkedList()
myList.insertLast(50)
myList.insertLast(20)
myList.insertLast(30)
myList.insertLast(40)
myList.viewList()
print()
myList.deleteFirst()
myList.viewList()
input()