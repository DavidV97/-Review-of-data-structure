from Node import Node


class Stack(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, item):
        success = True

        try:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp

        except ValueError:
            success = False

        return success

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):

        current = self.head
        found = False

        while current is not None and not found:

            if current.getData() == item:
                found = True

            else:
                current = current.getNext()

        return found

    def pop(self):
        success = True

        try:
            self.head = self.head.getNext()

        except ValueError:
            success = False

        return success

    def get_Data_Pop(self):
        return self.head.getData()

    def __str__(self):
        s = "Pila vacía"
        node = self.head

        if node is not None:
            s = "Pila = ["

            while node.getNext() is not None:
                s += str(node.getData()) + ", "
                node = node.getNext()

            s += str(node.getData())
            s += "]"

        return s
