from List import LinkedList
from Stack import Stack
from Queue import Queue
from BSTree import BSTree

linked_list = LinkedList()
stack = Stack()
queue = Queue()
bstree = BSTree()


class Manager:

        # thinks of list.
    @staticmethod
    def add_item_list(num):
        if linked_list.search(num) is False:

            if linked_list.add(num) is True:
                return ("El numero se agrego de manera exitosa\n" +
                        str(linked_list.__str__()))

            else:
                return ("*** Se produjo un error al agregar ***")
        else:
            return("*** El numero ya existe en la lista ***")

    @staticmethod
    def move_item_list(num):
        if linked_list.isEmpty() is False:

            if linked_list.search(num) is True:

                if linked_list.remove(num) is True:

                    return True
                else:
                    return ("*** Se produjo un error al mover ***")

            else:
                return ("*** El numero no existe en la lista ***")
        else:
            return("*** La lista esta vacía ***")

    @staticmethod
    def delete_item_list(num):
        if linked_list.isEmpty() is False:

            if linked_list.search(num) is True:

                if linked_list.remove(num) is True:

                    return ("El numero se elimino de manera exitosa\n" +
                            str(linked_list.__str__()))
                else:
                    return ("*** Se produjo un error al eliminar ***")

            else:
                return ("*** El numero no existe en la lista ***")
        else:
            return("*** La lista esta vacía ***")

    @staticmethod
    def show_item_list():
        return linked_list.__str__()

        # thinks of Stack.
    @staticmethod
    def add_item_stack(num):
        if stack.search(num) is False:

            if stack.push(num) is True:
                return ("El numero se agrego de manera exitosa\n" +
                        str(stack.__str__()))

            else:
                return ("*** Se produjo un error al agregar ***")
        else:
            return("*** El numero ya existe en la pila ***")

    @staticmethod
    def move_item_stack():
        if stack.isEmpty() is False:

            if stack.pop() is True:
                return True
            else:
                return ("*** Se produjo un error al mover ***")
        else:
            return("*** La pila esta vacía ***")

    @staticmethod
    def get_item_stack():
        return stack.get_Data_Pop()

    @staticmethod
    def delete_item_stack():
        if stack.isEmpty() is False:

            if stack.pop() is True:
                return ("El numero se elimino de manera exitosa\n" +
                        str(stack.__str__()))
            else:
                return ("*** Se produjo un error al eliminar ***")
        else:
            return("*** La pila esta vacía ***")

    @staticmethod
    def show_item_stack():
        return stack.__str__()

        # thinks of Queue.
    @staticmethod
    def add_item_queue(num):
        if queue.search(num) is False:

            if queue.en_queue(num) is True:
                return ("El numero se agrego de manera exitosa\n" +
                        str(queue.__str__()))

            else:
                return ("*** Se produjo un error al agregar ***")
        else:
            return("*** El numero ya existe en la cola ***")

    @staticmethod
    def move_item_queue():
        if queue.isEmpty() is False:

            if queue.de_queue() is True:
                return True
            else:
                return ("*** Se produjo un error al mover ***")
        else:
            return("*** La cola esta vacía ***")

    @staticmethod
    def get_item_queue():
        return stack.get_Data_de_queue()

    @staticmethod
    def delete_item_queue():
        if queue.isEmpty() is False:

            if queue.de_queue() is True:
                return ("El numero se elimino de manera exitosa\n" +
                        str(queue.__str__()))
            else:
                return ("*** Se produjo un error al eliminar ***")
        else:
            return("*** La cola esta vacía ***")

    @staticmethod
    def show_item_queue():
        return queue.__str__()

        # thinks of BTree.
    @classmethod
    def add_item_BTree(cls, num):
        if bstree.contains(num) is False:

            if bstree.insert(num) is True:
                return ("El numero se agrego de manera exitosa\n" +
                        cls.show_item_BTree())

            else:
                return ("*** Se produjo un error al agregar ***")
        else:
            return("*** El numero ya existe en el arbol ***")

    @staticmethod
    def move_item_BTree(num):
        if bstree.size != 0:

            if bstree.remove(num) is True:
                return True
            else:
                return ("*** Se produjo un error al mover ***")
        else:
            return("*** El arbol esta vacío ***")

    @classmethod
    def delete_item_BTree(cls, num):
        if bstree.size != 0:

            if bstree.remove(num) is True:
                return ("El numero se elimino de manera exitosa\n" +
                        cls.show_item_BTree())
            else:
                return ("*** Se produjo un error al eliminar ***")
        else:
            return("*** El arbol esta vacío ***")

    @classmethod
    def show_item_BTree(cls):
        s = "Arbol vacío"
        count = 0

        if bstree.size != 0:
            s = "Pre order: ["

            for i in bstree.pre_order_traversal():
                if count == 0:
                    s += str(i)
                else:
                    s += ", " + str(i)

                count += 1

            s += "] \nIn order: ["
            count = 0

            for x in bstree.in_order_traversal():
                if count == 0:
                    s += str(x)
                else:
                    s += ", " + str(x)

                count += 1

            s += "] \nPost order: ["
            count = 0

            for y in bstree.post_order_traversal():
                if count == 0:
                    s += str(y)
                else:
                    s += ", " + str(y)

                count += 1
            s += "]"

            return (s)

        else:
            return (s)
