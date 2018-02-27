from Node import Node
from DataStructure import DataStructure


class Stack(DataStructure):

    def add(self, item):

        try:
            temp_node = Node(item)
            temp_node.next_node = self.head
            self.head = temp_node

            return True

        except ValueError:
            return False

    def delete(self):

        try:
            self.head = self.head.next_node
            return True

        except ValueError:
            return False

    def get_Data_Pop(self):
        return self.head.data
