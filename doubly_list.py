class Node:
    """item will store the actual data for the node
        nref => next node
        pref => previous node
    """
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

# inserting items in the doubly linked list

def insert_in_emptylist(self, data):
    """checks if the variable is None or not. If it's None, list is empty.
        then new node is created and it's initialized by value passed as parameter
        to the data parameter.
    """
    if self.start_node is None:
        new_node = Node(data)
        self.start_node = new_node
    else:
        print('list is not empty')


def insert_at_start(self, data):
    if self.start_node is None:
        new_node = Node(data)
        self.start_node = new_node
        print("node inserted")

    new_node = Node(data)
    new_node.nref = self.start_node
    self.start_node.pref = new_node
    self.start_node = new_node

def insert_at_end(self, data):
    if self.start_node is None:
        new_node = Node(data)
        self.start_node = new_node
        return
    n = self.start_node
    while n.nref is not None:
        n = n.nref
    new_node = Node(data)
    n.nref = new_node
    new_node.pref = n

def insert_after_item(self, x, data):
    """method to insert item after another item """

    if self.start_node is None:
        print("List is empty")
        return
    else:
        n = self.start_node
        while n is not None:
            if n.item == "x":
                break
            n = n.nref
        if n is None:
            print("item is not in the list")
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            if n.nref is not None:
                n.nref.prev = new_node
            n.nref = new_node
