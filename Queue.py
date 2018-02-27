from Node import Node
from DataStructure import DataStructure


class Queue(DataStructure):

    def __init__(self):
        super().__init__()
        self.tail = None

    def isEmpty(self):
        return self.head and self.tail is None

    def add(self, item):

        try:
            temp_node = Node(item)

            if not len(self):
                self.head = self.tail = temp_node

            else:
                tail = self.tail
                self.tail = temp_node
                tail.next_node = temp_node

            return True

        except ValueError:
            return False

    def delete(self):

        try:
            self.head = self.head.next_node

            if len(self):
                self.tail = None
                return True

        except ValueError:
            return False

    def get_Data_de_queue(self):
        return self.head.data
