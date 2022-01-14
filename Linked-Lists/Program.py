from re import L
from LinkedList import LinkedList
from Node import Node

# Nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

list = LinkedList()
list.head = node1

list.head.pointer = node2
node2.pointer = node3
node3.pointer = node4

def walk():

    current = list.head

    while (current is not None):
        print(current.element)
        current = current.pointer


def search(item):
    current = list.head
    found = False
    while (current is not None and found is False):
        if (current.element == item):
                found = True
        current = current.pointer
    return found

def printList():
    current = list.head
    while (current is not None):
        if (current.pointer is None):
            end = None
        else:
            end = " -> "
        print(current.element, end=end)
        current = current.pointer
        
def insertBefore(node, item):

    newNode = Node(item)

    if (list.head == node):
        temp = list.head
        list.head = newNode
        newNode.pointer = temp
        return
    current = list.head
    foundNode = None
    
    while (current is not None and foundNode is None):
        if (current.pointer == node):
            foundNode = current.pointer
        current = current.pointer
    

    if (foundNode is None):
        print("Error")
    else:
        temp = foundNode.pointer
        foundNode.pointer = newNode
        newNode.pointer = temp






printList()
insertBefore(node1, 0)
printList()
insertBefore(node3, 'x')
printList()

