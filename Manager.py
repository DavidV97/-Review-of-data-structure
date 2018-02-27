from List import LinkedList
from Stack import Stack
from Queue import Queue
from BSTree import BSTree
from AVLTree import AVLTree

linked_list = LinkedList()
stack = Stack()
queue = Queue()
bstree = BSTree()
avltree = AVLTree()


class Manager:

    @classmethod
    def add_item(cls, num, struck_type):

        struckture = cls.get_struck_obj(struck_type)

        if not (num in struckture):

            if struckture.add(num):
                return "El numero se agrego de manera exitosa\n{}".format(
                    struckture)

            else:
                return "*** Se produjo un error al agregar ***"
        else:
            if struckture == bstree or avltree:
                return"*** El numero ya existe en el " + struck_type + " ***"
            else:
                return"*** El numero ya existe en la " + struck_type + " ***"

    @classmethod
    def move_item(cls, num, struck_type):

        struckture = cls.get_struck_obj(struck_type)

        if struckture.isEmpty() is False:

            if num in struckture:

                if struckture.delete(num):

                    return True
                else:
                    return "*** Se produjo un error al mover ***"

            else:
                if struckture == bstree or avltree:
                    return "*** El numero no existe en el "
                    + struck_type + " ***"
                else:
                    return "*** El numero no existe en la "
                    + struck_type + " ***"
        else:
            if struckture == bstree or avltree:
                return "*** El " + struck_type + " esta vacío ***"
            else:
                return "*** La " + struck_type + " esta vacía ***"

    @classmethod
    def delete_item(cls, num, struck_type):
        struckture = cls.get_struck_obj(struck_type)

        if struck_type == "lista" or struck_type == "arbol binario" or struck_type == "arbol AVL":

            if num in struckture:

                if struckture.delete(num):
                    return "El numero se elimino de manera exitosa\n{}".format(
                        struckture)

                else:
                    return "*** Se produjo un error al eliminar ***"
            else:
                if struckture == bstree or avltree:
                    return "*** El numero no existe en el "
                    + struck_type + " ***"
                else:
                    return "*** El numero no existe en la "
                    + struck_type + " ***"

        else:
            if struckture.delete():
                return "El numero se elimino de manera exitosa\n{}".format(
                    struckture)

            else:
                return "*** Se produjo un error al eliminar ***"

    @classmethod
    def show_item(cls, struck_type):
        struckture = cls.get_struck_obj(struck_type)

        return struckture

    @classmethod
    def get_struck_obj(cls, struck_type):
        if struck_type == "lista":
            return linked_list
        elif struck_type == "pila":
            return stack
        elif struck_type == "cola":
            return queue
        elif struck_type == "arbol binario":
            return bstree
        elif struck_type == "arbol AVL":
            return avltree
