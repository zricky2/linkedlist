# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null
        self.prev = None

# Linked List class

class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
        self.size = 0

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
            newNode.prev = current
        else:
            self.head = newNode
        self.size += 1

    def remove(self, data):
        current = self.head
        # if the linked list is not empty
        while (current is not None):
            if (current.data == data):
                prevNode = current.prev
                nextNode = current.next
                if(current == self.head):
                    if (nextNode is not None):
                        self.head = nextNode
                        nextNode.prev = None
                        current = None
                    else:
                        self.head = None
                        current = None
                    self.size -= 1
                    return
                if (nextNode is None):
                    prevNode.next = None
                else:
                    prevNode.next = nextNode
                    nextNode.prev = prevNode
                    current = None
                self.size -= 1
                return
            current = current.next
        return

    def getSize(self):
        return self.size


    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


llist = LinkedList()
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(16)#removed
llist.insert(90)
llist.insert(87)
llist.insert(1)
llist.insert(10)#removed
llist.insert(45)
llist.remove(16)
llist.remove(10)
llist.insert(7)
llist.insert(77)
llist.insert(9)
llist.remove(8)#not in list
llist.insert(7)

llist.printLL()
