class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = Node()
    
    def add(self,data):
        cur = self.head
        newNode = Node(data)
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
    
    def length(self):
        count = 0
        cur = self.head
        while cur.next != None:
            count +=1
            cur = cur.next
        return count

    
    def display(self):
        myList = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            myList.append(cur.data)
        print(myList)
    
    def get(self,idx):
        cur = self.head
        cur_idx = 0
        if idx > self.length():
            print("ERROR: Index %d is out of range" %idx)
            return
        else:
            while cur != None:
                cur = cur.next
                if cur_idx == idx:
                    print("Index {} data is: {}".format(idx,cur.data))
                cur_idx +=1
    
    def remove(self,idx):
        cur = self.head
        cur_idx = 0
        if idx > self.length():
            print("ERROR: Index %d is out of range" %idx)
            return None
        while cur != None:
            if cur_idx == idx:
                cur.next = cur.next.next
            cur = cur.next
            cur_idx +=1
                
a = Linkedlist()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.display()
a.get(2)
a.remove(6)
a.display()
