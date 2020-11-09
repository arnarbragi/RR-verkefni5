class Node: 
    # SmiÃ°ur, frumstillir d og nÃºllstillir bendana prv og nxt
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    # EndurkvÃ¦mt fall sem bÃ¦tir aftast Ã¡ listann.   
    def append(self,d):
        if self.nxt == None:
            temp = Node(d)
            temp.prv = self
            self.nxt = temp
        else:
            self.nxt.append(d);

    # EndurkvÃ¦mt fall sem prentar listann.
    def printList(self):
        print(self.data, end = " ")
        if self.nxt == None:
            pass
        else:
            self.nxt.printList()
                 
    # EndurkvÃ¦mt fall sem athuga hvort stak d er Ã­ listanum.
    def find(self, d):
        if self.data == d:
            return True
        else:
            if self.nxt == None:
                return False
            else:
                return self.nxt.find(d)

    # EndurkvÃ¦mt fall sem eyÃ°ir staki d Ãºr listanum.
    def delete(self, d):
        if self.data == d:
            self.prv.nxt = self.nxt
            self.nxt.prv = self.prv
            return "Successfully deleted :)"
        else:
            if self.nxt == None:
                return "Data not found :("
            else:
                return self.nxt.delete(d)

class DLL:
    # SmiÃ°ur, nÃºllstillir Haus listans
    def __init__(self):
        self.head = None

    # BÃ¦tir viÃ° fremst Ã¡ listann, hnÃºturinn verÃ°ur Head -> fÃ¶rum ekki Ã­ Node klasann.
    def push(self,d):
        temp = Node(d)
        temp.data = d
        if self.head == None:
            self.head = temp
        else:
            self.head.prv = temp
            temp.nxt = self.head
            self.head = temp
    
    # BÃ¦tir viÃ° aftast Ã¡ listann -> kallar Ã¡ endurkvÃ¦mnt fall Ã­ Node.
    def append(self, d):
        if self.head == None:
            temp = Node(d)
            self.head = temp
        else:
            self.head.append(d)

    # Prentar listann allan Ã¡ skjÃ¡ -> kallar Ã¡ endurkvÃ¦mt fall Ã­ Node.
    def printList(self):
        self.head.printList()
    
    # Finnur stak d Ã­ ef til -> kallar Ã¡ endurkvÃ¦mnt fall Ã­ Node.
    def find(self, d):
        return self.head.find(d)

    # EyÃ°ir staki d Ãºr lista ef til -> kallar Ã¡ endurkvÃ¦mnt fall Ã­ Node.
    def delete(self, d):
        return self.head.delete(d)

# KeyrslurÃºtÃ­na
dbl = DLL()
dbl.append(5)           # 5
dbl.append(7)           # 5 7         
dbl.push(1)             # 1 5 7 
dbl.push(0)             # 0 1 5 7 
dbl.append(10)          # 0 1 5 7 10
dbl.printList()         
print()
print(dbl.delete(5))   # 0 1 7 10
dbl.printList() 
print()
print(dbl.find(5))      # False
print(dbl.find(7))      # True
