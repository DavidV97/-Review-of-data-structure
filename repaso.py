from Manager import Manager


def start():
    exit = True

    while exit:

        menu()
        option = get_option()
        exit = execute_menu(option)


def menu():
    print("1. Agregar datos en una estructura\n")
    print("2. Mover datos en una estructura\n")
    print("3. Eliminar datos en una estructura\n")
    print("4. Mostrar datos de una estructura\n")
    print("0. Salir\n")


def get_option():

    option = input("Digite una opcion\n")

    return option


def execute_menu(option):
    exit = True

    if option == "1":

        add_menu()
        option = get_option()
        execute_add_menu(option)

    elif option == "2":

        move_menu()
        option = get_option()
        execute_move_menu(option)

    elif option == "3":

        delete_menu()
        option = get_option()
        execute_delete_menu(option)

    elif option == "4":

        show_menu()
        option = get_option()
        execute_show_menu(option)

    elif option == "0":

        exit = False
        print("Gracias...")

    else:
        print("Opcion invalida")

    return exit


def add_menu():
    print("1. Agregar datos en una lista\n")
    print("2. Agregar datos en una pila\n")
    print("3. Agregar datos en una cola\n")
    print("4. Agregar datos en un arbol\n")


def execute_add_menu(option):
    num = 0

    if option == "1":
        num = get_input()
        print(str(Manager.add_item_list(num)) + "\n")

    elif option == "2":
        num = get_input()
        print(str(Manager.add_item_stack(num)) + "\n")

    elif option == "3":
        num = get_input()
        print(str(Manager.add_item_queue(num)) + "\n")

    elif option == "4":
        num = get_input()
        print(str(Manager.add_item_BTree(num)) + "\n")
    else:
        print("Opcion invalida")


def move_menu():
    print("1. Mover datos en una lista\n")
    print("2. Mover datos en una pila\n")
    print("3. Mover datos en una cola\n")
    print("4. Mover datos en un arbol\n")


def execute_move_menu(option):

    if option == "1":
        move_from_list()

    elif option == "2":
        move_from_stack()

    elif option == "3":
        move_from_queue()

    elif option == "4":
        move_from_btree()

    else:
        print("Opcion invalida")


def movement_menu(num):
    if num == 1:
        print("1. Mover a una pila\n")
        print("2. Mover a una cola\n")
        print("3. Mover a un arbol\n")
    elif num == 2:
        print("1. Mover a una lista\n")
        print("2. Mover a una cola\n")
        print("3. Mover a un arbol\n")
    elif num == 3:
        print("1. Mover a una lista\n")
        print("2. Mover a una pila\n")
        print("3. Mover a un arbol\n")
    else:
        print("1. Mover a una lista\n")
        print("2. Mover a una pila\n")
        print("3. Mover a una cola\n")


def move_from_list():
    movement_menu(1)
    option = get_option()

    print(str(Manager.show_item_list()) + "\n")
    num = get_input()

    if(Manager.move_item_list(num) is True):

        if(option == "1"):
            print(str(Manager.add_item_stack(num)) + "\n")
        elif(option == "2"):
            print(str(Manager.add_item_queue(num)) + "\n")
        elif(option == "3"):
            print(str(Manager.add_item_BTree(num)) + "\n")
        else:
            print("*** Opcion invalida ***")
    else:
        print(str(Manager.move_item_list(num)) + "\n")


def move_from_stack():
    movement_menu(2)
    option = get_option()

    num = Manager.get_item_stack()

    if(Manager.move_item_stack() is True):

        if(option == "1"):
            print(str(Manager.add_item_list(num)) + "\n")
        elif(option == "2"):
            print(str(Manager.add_item_queue(num)) + "\n")
        elif(option == "3"):
            print(str(Manager.add_item_BTree(num)) + "\n")
        else:
            print("*** Opcion invalida ***")
    else:
        print(str(Manager.move_item_list()) + "\n")


def move_from_queue():
    movement_menu(3)
    option = get_option()

    num = Manager.get_item_queue()

    if(Manager.move_item_queue() is True):

        if(option == "1"):
            print(str(Manager.add_item_list(num)) + "\n")
        elif(option == "2"):
            print(str(Manager.add_item_stack(num)) + "\n")
        elif(option == "3"):
            print(str(Manager.add_item_BTree(num)) + "\n")
        else:
            print("*** Opcion invalida ***")
    else:
        print(str(Manager.move_item_list()) + "\n")


def move_from_btree():
    movement_menu(4)
    option = get_option()

    print(str(Manager.show_item_BTree()) + "\n")
    num = get_input()

    if(Manager.move_item_BTree(num) is True):

        if(option == "1"):
            print(str(Manager.add_item_list(num)) + "\n")
        elif(option == "2"):
            print(str(Manager.add_item_stack(num)) + "\n")
        elif(option == "3"):
            print(str(Manager.add_item_queue(num)) + "\n")
        else:
            print("*** Opcion invalida ***")
    else:
        print(str(Manager.move_item_BTree(num)) + "\n")


def delete_menu():
    print("1. Eliminar datos en una lista\n")
    print("2. Eliminar datos en una pila\n")
    print("3. Eliminar datos en una cola\n")
    print("4. Eliminar datos en un arbol\n")


def execute_delete_menu(option):

    if option == "1":
        num = get_input()
        print(str(Manager.delete_item_list(num)) + "\n")

    elif option == "2":
        print(str(Manager.delete_item_stack()) + "\n")

    elif option == "3":
        print(str(Manager.delete_item_queue()) + "\n")

    elif option == "4":
        num = get_input()
        print(str(Manager.delete_item_BTree(num)) + "\n")
    else:
        print("Opcion invalida")


def show_menu():
    print("1. Mostrar datos de la lista\n")
    print("2. Mostrar datos de la pila\n")
    print("3. Mostrar datos de la cola\n")
    print("4. Mostrar datos del arbol\n")


def execute_show_menu(option):

    if option == "1":
        print(str(Manager.show_item_list()) + "\n")
    elif option == "2":
        print(str(Manager.show_item_stack()) + "\n")
    elif option == "3":
        print(str(Manager.show_item_queue()) + "\n")
    elif option == "4":
        print(str(Manager.show_item_BTree()) + "\n")
    else:
        print("Opcion invalida")


def get_input():

    success = True

    while success:
        try:
            option = int(input("Digite el numero: "))
            success = False

        except ValueError:
            print("El numero debe ser entero")

    return option


if __name__ == "__main__":
    start()
