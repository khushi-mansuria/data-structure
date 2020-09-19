class Node: 

    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
        self.previous = None
    
class LinkedList:
        
    def __init__(self):
        self.head = None
        self.size = 0
                     
    def add_head(self,e): 
        self.head = Node(e)        
        self.size += 1 
        
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object
                    
    def add_tail(self,e):
        new_value = Node(e)
        new_value.previous = self.get_tail()
        self.get_tail().next = new_value
        self.size += 1        
                        
    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index == 0:
            return element_node.element
        if index > self.size-1:
            print("Index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter += 1
        return element_node
  

lst = LinkedList()
order = int(input('Enter the order for polynomial : '))
lst.add_head(Node(int(input(f"Enter coefficient for power {order} : "))))
for i in reversed(range(order)):
    lst.add_tail(int(input(f"Enter coefficient for power {i} : ")))
    
lst2 = LinkedList()
lst2.add_head(Node(int(input(f"Enter coefficient for power {order} : "))))
for i in reversed(range(order)):
    lst2.add_tail(int(input(f"Enter coefficient for power {i} : ")))
    
for i in range(order + 1):
    print(lst.get_node_at(i).element + lst2.get_node_at(i).element)
