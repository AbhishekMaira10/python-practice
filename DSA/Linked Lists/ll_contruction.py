# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        pass

    def setTail(self, node):
        # Write your code here.
        pass

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        if (node == self.head):
            self.head = self.head.next
        if(node == self.tail):
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNodeBindings(self, node):
        #write your code here
        pass
