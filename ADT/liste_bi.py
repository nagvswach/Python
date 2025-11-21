
class Node:
    def __init__(self, initdata)
        self.data = initdata
        self.previous = None
        self.next = None
    
    def getNext(self)
        return self.next

    def getPrevious(self)
        return self.previous

    def getData(self)
        return self.data
    
    def setNext(self,new):
        self.next = new

    def setPrevious(self,new):
        self.previous = new

    def setData(self,new):
        self.data = new

class underedlist:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item):
        temp.setNext(self.head)
        temp.getPrevious().setPrevious(temp)<F10>
        self.head = temp


