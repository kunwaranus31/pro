class Node:
    def _init_(self, key, val):
        self.value = val
        self.next = None
        self.prev = None
        self.key = key
        self.index = 0


class Double:
    def _init_(self):
        self.head = None
        self.tail = None

    def insertFirst(self, key, val):
        x = Node(key, val)
        if self.head == None and self.tail == None:
            self.head = x
            self.tail = x
            x.index = 0
        else:
            temp = self.head
            x.next = self.head
            x.index = 0
            self.head = x
            temp.prev = x
            self.updateIndex(x.next)

    def insertLast(self, key, val):
        x = Node(key, val)
        if self.head == None and self.tail == None:
            self.head = x
            self.tail = x
        else:
            temp = self.tail
            temp.next = x
            self.tail = x
            self.tail.prev = temp
            x.index = temp.index + 1

    def insertAtIndex(self, index, key, val):
        if index == 0:
            self.insertFirst(key, val)
        elif self.head != None and self.tail != None:
            x = Node(key, val)
            temp = self.head
            y = temp.next
            while y:
                if y.index == index:
                    x.prev = y.prev
                    y.prev.next = x
                    x.next = y
                    y.prev = x
                    x.index = index
                    self.updateIndex(x.next)
                    break
                # if y.next == None and y.index + 1 == index:
                #    self.insertLast(key,val)
                #    break
                temp = temp.next
                y = y.next
            if not y:
                print("Value not found")
        else:
            print("List is Empty")

    def updateIndex(self, obj):
        if self.head == None and self.tail == None:
            print("List is Empty")
        else:
            x = obj
            while x:
                x.index += 1
                x = x.next

    def getValueByIndex(self, index):
        if index > self.tail.index:
            return "index out of range"
        elif self.head == None and self.tail == None:
            print("List is Empty")
        else:
            x = self.head
            while x:
                if x.index == index:
                    return x.value
                x = x.next

    def getValueByKey(self, key):
        if self.head == None and self.tail == None:
            print("List is Empty")
        else:
            x = self.head
            while x:
                if x.key == key:
                    return x.value
                x = x.next
            return "key not found"

    def deleteFirst(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            self.head = self.head.next
            self.head.prev = None
        else:
            print("List is Empty")

    def deleteLast(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
        else:
            print("List is Empty")

    def deleteVal(self, val):
        if self.head == self.tail and self.head.value == val and self.tail.value == val:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            x = self.head
            y = x.next
            if self.head.value == val:
                self.deleteFirst()
            elif self.tail.value == val:
                self.deleteLast()
            elif self.head == None and self.tail == None:
                print("List is Empty")
            else:
                while y:
                    if x.value == val:
                        y.prev.prev.next = y
                        y.prev = x.prev
                        break
                    else:
                        y = y.next
                        x = x.next
                if not y:
                    print("Item Not found")
        else:
            print("List is Empty")

    def deleteindex(self, index):
        if self.head == self.tail and self.head.index == index and self.tail.index == index:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            x = self.head
            y = x.next
            if self.head.index == index:
                self.deleteFirst()
            elif self.tail.index == index:
                self.deleteLast()
            elif self.head == None and self.tail == None:
                print("List is Empty")
            else:
                while y:
                    if x.index == index:
                        y.prev.prev.next = y
                        y.prev = x.prev
                        break
                    else:
                        y = y.next
                        x = x.next
                if not y:
                    print("Item Not found")
        else:
            print("List is Empty")

    def deletekey(self, key):
        if self.head == self.tail and self.head.key == key and self.tail.key == key:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            x = self.head
            y = x.next
            if self.head.key == key:
                self.deleteFirst()
            elif self.tail.key == key:
                self.deleteLast()
            elif self.head == None and self.tail == None:
                print("List is Empty")
            else:
                while y:
                    if x.key == key:
                        y.prev.prev.next = y
                        y.prev = x.prev
                        break
                    else:
                        y = y.next
                        x = x.next
                if not y:
                    print("Item Not found")
        else:
            print("List is Empty")

    def PrintkeyValues(self):
 
        if self.head == None and self.tail == None:
            print("List is Empty")
        else:
            print("{", end="")
            x = self.head
            while x:
                print(str(x.key) + ": " + str(x.value), end="")
                if x.next != None:
                    print(",", end=" ")
                x = x.next
        print("}")

    def printValues(self):
        if self.head == None and self.tail == None:
            print("List is Empty")
        else:
            print("[", end="")
            x = self.head
            while x:
                print(x.value, end="")
                if x.next != None:
                    print(",", end=" ")
                x = x.next
        print("]")

    def printKeys(self):
        if self.head == None and self.tail == None:
            print("List is Empty")
        else:
            print("[", end="")
            x = self.head
            while x:
                print(x.key, end="")
                if x.next != None:
                    print(",", end=" ")
                x = x.next
        print("]")

    def PrintReverse(self):
        if self.head == None and self.tail == None:
            print("List is Empty")
        else:
            print("{", end="")
            x = self.tail
            while x:
                print(str(x.key) + ": " + str(x.value), end="")
                if x.prev != None:
                    print(",", end=" ")
                x = x.prev
        print("}")


d1 = Double()
d1.insertFirst("a", 1)
d1.insertFirst("b", 2)
d1.insertFirst("c", 3)
d1.insertLast("d", 4)
d1.insertAtIndex(1, "e", 9)
d1.insertAtIndex(0, "f", 10)
d1.insertAtIndex(3, "g", 8)
d1.insertAtIndex(4, "h", 7)
d1.insertAtIndex(4, "i", 22)
d1.deleteFirst()
d1.deleteLast()
d1.deleteVal(7)
d1.deletekey('b')
d1.deleteindex(3)
print("Values: ", end="")
d1.printValues()
print("Keys: ", end="")
d1.printKeys()
print("HashTable: ", end="")
d1.PrintkeyValues()
print("Reverse HashTable: ", end="")
d1.PrintReverse()
print("Value at Key 'i':", d1.getValueByKey("i"))
print("Value at index 7:", d1.getValueByIndex(5))