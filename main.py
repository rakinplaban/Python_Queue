class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class Queue:
    def __init__(self):
        self.count = 0
        self.front = None
        self.rear = None
        
    def Enqueue(self,val):
        node = Node(val)
        if self.count == 0:
            self.front = node 
            self.rear = node
        else:
            temp = self.rear
            temp.next = node
            self.rear = node
        self.count += 1 
        
    def Dequeue(self):
        if self.count == 0:
            print("Undef Flow!")
        else:
            temp = self.front
            self.front = temp.next
            del(temp)
            self.count -= 1
        
    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.val,end=" ")
            temp = temp.next
            
q = Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.display()
print("\nQueue Front: ",q.front.val," Queue rear: ",q.rear.val," Number of nodes: ",q.count)
q.Dequeue()
q.display()
print("\nQueue Front: ",q.front.val," Queue rear: ",q.rear.val," Number of nodes: ",q.count)

