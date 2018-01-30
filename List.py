from Node import Node
from Merge_sort import Merge_sort


class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        success = True

        try:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp

            self.head = Merge_sort.mergeSort(self.head)

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

    def remove(self, item):
        success = True

        try:
            current = self.head
            previous = None
            found = False

            while not found:

                if current.getData() == item:
                    found = True

                else:
                    previous = current
                    current = current.getNext()

            if previous is None:
                self.head = current.getNext()

            else:
                previous.setNext(current.getNext())

        except ValueError:
            success = False

        return success

    def __str__(self):
        s = "Lista vacía"
        node = self.head

        if node is not None:
            s = "Lista = ["

            while node.getNext() is not None:
                s += str(node.getData()) + ", "
                node = node.getNext()

            s += str(node.getData())
            s += "]"

        return s
