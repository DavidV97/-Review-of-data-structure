from Node import Node


class Queue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def en_queue(self, item):
        success = True

        try:
            temp = Node(item)

            if self.length == 0:
                self.head = self.tail = temp

            else:
                tail = self.tail
                tail.setNext(temp)
                self.tail = temp

            self.length += 1

        except ValueError:
            success = False

        return success

    def length(self):
        return self.count()

    def search(self, item):

        current = self.head
        found = False

        while current is not None and not found:

            if current.getData() == item:
                found = True

            else:
                current = current.getNext()

        return found

    def de_queue(self):
        success = True

        try:
            self.head = self.head.getNext()

            if self.length == 0:
                self.tail = None

        except ValueError:
            success = False

        return success

    def get_Data_de_queue(self):
        return self.head.getData()

    def __str__(self):
        s = "Cola vacía"
        node = self.head

        if node is not None:
            s = "Cola = ["

            while node.getNext() is not None:
                s += str(node.getData()) + ", "
                node = node.getNext()

            s += str(node.getData())
            s += "]"

        return s
