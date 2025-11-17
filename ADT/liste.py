"""Méthode de la classe Noeud"""

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new):
        self.data = new

    def setNext(self, new):
        self.next = new


class Unorderedlist:
    def __init__(self):
        self.head = None

    def est_vide(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def add_apres_ref(self,base_ref,item):
        temp = Node(item)
        temp.setNext(base_ref.getNext())
        base_ref.setNext(temp)

    def add_apres_val(self, base_val, item):
        temp = Node(item)
        current = self.head
        while current is not None and current.getData() != base_val:
            current = current.getNext()
        if current is None:
            print("introuvable")
            return
        temp.setNext(current.getNext())
        current.setNext(temp)

    def add_fin(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(temp)

    def longueur(self):
        current = self.head
        count = 0 
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def recherche(self, base):
        current = self.head
        while current is not None and current.getData() != base:
            current = current.getNext()
        return current is not None

    def supprimer_ref(self, base_ref):
        prec = None
        current = self.head
        found = False
        while current != None and not found:
            if current is base:
                found = True
            else:
                prec = current
                current = current.getNext()
        if found:
            if prec != None:
                prec.setNext(base_ref.getNext())
            else:
                self.head = base_ref.getNext()

    def supprimer_val(self,base_val):
        prec = None 
        current = self.head
        found = True
        while current is not None and not found:
            if current.getData() == base_val:
                found = True
            else:
                prec = current
                current = current.getNext()
        if found:
            if prec is not None:
                prec.setNext(current_ref.getNext())
            else:
                self.head = current.getNext()
            


            

l = Unorderedlist()
l.add(5)
l.add(3)
print(l.longueur())
print(l.recherche(5))
l.supprimer_val(5)
print(l.longueur())
