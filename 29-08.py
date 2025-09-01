#LIFO
#QUEUE => 
#Operations => Insert, Remove, is_empty
#peek 

class Queue:

    def __init__(self):
        self.__vals = []
        print('Queue object created')

    def insert_elem (self, elem):
        self.__vals.append(elem)
        print(self.__vals)

    def remove_elem(self):
        if len(self.__vals) == 0:
            return 'Already empty'
        
        return self.__vals.pop(0)

    def is_empty(self):
        return len(self.__vals) == 0
    
    def peek(self):
        if len(self.__vals) == 0:
            return 'Already empty'

        return self.__vals[0]
    


qu1 = Queue()

qu1.insert_elem(5)
qu1.insert_elem(-3)
qu1.remove_elem()
qu1.remove_elem()
qu1.is_empty()
qu1.insert_elem(2)
qu1.peek()
qu1.insert_elem(-32)
qu1.insert_elem(77)
qu1.insert_elem(66)




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        print('Empty Linkedlist created')

    def add_node(self, elem):
        if self.head == None:
            self.head = Node(elem)
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(elem)
        return
    
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, ' ->', end='')
            temp = temp.next

        return 
    
    def find(self, search_elem):
        temp = self.head
        while temp:
            if temp.data == search_elem:
                return True
            temp = temp.next

        return False

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        return count
    
    def delete_node(self, elem):
        if self.head == None:
            return 
        
        if self.head.data == elem:
            self.head = self.head.next
            return
        
        temp = self.head
        prev = None

        while temp:
            if temp.data == elem:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next


        return 



            

ll1 = LinkedList()
print(ll1.head)

ll1.add_node(5)
ll1.add_node(15)
ll1.add_node(25)
ll1.add_node(35)
ll1.add_node(45)

ll1.display()
print()
ll1.delete_node(5)
ll1.display()
print()
ll1.delete_node(35)
print()
ll1.display()

print(ll1.find(45))
print(ll1.length())