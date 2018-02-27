class DataStructure(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    def __len__(self):

        temp_node = self.head
        count = 0

        while temp_node:
            count += 1
            temp_node = temp_node.next_node

        return count

    def __contains__(self, key):

        temp_node = self.head

        while temp_node:

            if temp_node.data == key:
                return True

            else:
                temp_node = temp_node.next_node

        return False

    def __str__(self):
        struck_name = self.get_es_name()
        s = struck_name + " vacía"
        node = self.head

        if len(self):
            s = struck_name + " = ["

            while node.next_node:
                s += str(node.data) + ", "
                node = node.next_node

            s += str(node.data)
            s += "]"

        return s

    def get_es_name(self):
        if str(self.__module__) == "List":
            return "Lista"
        elif str(self.__module__) == "Stack":
            return "Pila"
        elif str(self.__module__) == "Queue":
            return "Cola"
