from Node import Node
from Merge_sort import Merge_sort
from DataStructure import DataStructure


class LinkedList(DataStructure):

    def add(self, item):

        try:
            temp_node = Node(item)

            temp_node.next_node = self.head

            self.head = temp_node

            self.head = Merge_sort.mergeSort(self.head)

            return True

        except ValueError:
            return False

    def delete(self, item):

        try:
            curr_node = self.head
            prev_node = None
            found = False

            while not found:

                if curr_node.data == item:
                    found = True

                else:
                    prev_node = curr_node
                    curr_node = curr_node.next_node

            if prev_node is None:
                self.head = curr_node.next_node

            else:
                prev_node.next_node = curr_node.next_node

            return True

        except ValueError:
            return False
