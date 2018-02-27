from Manager import Manager


def start():
    exit = True

    while exit:

        menu()
        option = get_option()
        exit = execute_menu(option)


def menu():
    print("____________Menu principal____________\n")
    print("1. Agregar datos en una estructura\n")
    print("2. Mover datos en una estructura\n")
    print("3. Eliminar datos en una estructura\n")
    print("4. Mostrar datos de una estructura\n")
    print("0. Salir\n")
    print("______________________________________\n")


def get_option():

    option = input("Digite una opcion: ")

    return option


def execute_menu(option):
    exit = True
    operation = ""

    if option == "1":
        operation = "Add"
        add_move_delete_show_menu(operation)
        option = get_option()
        execute_add_move_delete_show(option, operation)

    elif option == "2":

        operation = "Move"
        add_move_delete_show_menu(operation)
        option = get_option()
        execute_add_move_delete_show(option, operation)

    elif option == "3":

        operation = "Delete"
        add_move_delete_show_menu(operation)
        option = get_option()
        execute_add_move_delete_show(option, operation)

    elif option == "4":

        operation = "Show"
        add_move_delete_show_menu(operation)
        option = get_option()
        execute_add_move_delete_show(option, operation)

    elif option == "0":

        exit = False
        print("Gracias...")

    else:
        print("*Opcion invalida*")

    return exit


def add_move_delete_show_menu(operation):
    operation = get_ES_name(operation)

    print("____________" + operation + " datos____________\n")
    print("1. En una lista\n")
    print("2. En una pila\n")
    print("3. En una cola\n")
    print("4. En un arbol binario\n")
    print("5. En un arbol AVL\n")
    print("0. <-\n")
    print("______________________________________")


def get_ES_name(operation):
    if operation == "Add":
        return "Agregar"
    elif operation == "Move":
        return "Mover"
    elif operation == "Delete":
        return "Eliminar"
    else:
        return "Mostrar"


def execute_add_move_delete_show(option, operation):
    strcuk_type = ""

    if option == "1":
        strcuk_type = "lista"
        execute_operation(operation, strcuk_type)

    elif option == "2":
        strcuk_type = "pila"
        execute_operation(operation, strcuk_type)

    elif option == "3":
        strcuk_type = "cola"
        execute_operation(operation, strcuk_type)

    elif option == "4":
        strcuk_type = "arbol binario"
        execute_operation(operation, strcuk_type)

    elif option == "5":
        strcuk_type = "arbol AVL"
        execute_operation(operation, strcuk_type)

    elif option == "0":
        pass

    else:
        print("Opcion invalida")


def execute_operation(operation, struck_type):
    num = 0

    if operation == "Add" or operation == "Delete" or operation == "Move":

        if operation == "Add":

            num = get_input()
            print(str(Manager.add_item(num, struck_type)))

        elif operation == "Move":
            movement_op(struck_type)

        else:
            if struck_type == "lista" or struck_type == "arbol binario" or struck_type == "arbol AVL":
                num = get_input()
                print(str(Manager.delete_item(num, struck_type)))
            else:
                num = 0
                print(str(Manager.delete_item(num, struck_type)))
    else:
        print(str(Manager.show_item(struck_type)))


def movement_op(struck_type):
    movement_menu(struck_type)
    option = get_option()
    move_to(option, struck_type)


def movement_menu(struck_type):
    print("______________________________________\n")
    if struck_type == "lista":
        print("2. Mover a una pila\n")
        print("3. Mover a una cola\n")
        print("4. Mover a un arbol\n")
        print("5. Mover a un arbol AVL\n")

    elif struck_type == "pila":
        print("1. Mover a una lista\n")
        print("3. Mover a una cola\n")
        print("4. Mover a un arbol\n")
        print("5. Mover a un arbol AVL\n")

    elif struck_type == "cola":
        print("1. Mover a una lista\n")
        print("2. Mover a una pila\n")
        print("4. Mover a un arbol\n")
        print("5. Mover a un arbol AVL\n")

    elif struck_type == "arbol binario":
        print("1. Mover a una lista\n")
        print("2. Mover a una pila\n")
        print("3. Mover a una cola\n")
        print("5. Mover a un arbol AVL\n")

    elif struck_type == "arbol AVLvalue, ..., sep, end, file, flush":
        print("1. Mover a una lista\n")
        print("2. Mover a una pila\n")
        print("3. Mover a una cola\n")
        print("4. Mover a un arbol\n")
    print("______________________________________")


def move_to(option, struck_type):

    print("\n" + str(Manager.show_item(struck_type)) + "\n")
    print("Numeros a mover\n")
    num = get_input()

    if(Manager.move_item(num, struck_type) is True):

        if(option == "1"):
            strcuk_typ = "lista"
            print(str(Manager.add_item(num, strcuk_typ)) + "\n")
        elif(option == "2"):
            strcuk_typ = "pila"
            print(str(Manager.add_item(num, strcuk_typ)) + "\n")
        elif(option == "3"):
            strcuk_typ = "cola"
            print(str(Manager.add_item(num, strcuk_typ)) + "\n")
        elif(option == "4"):
            strcuk_typ = "arbol binario"
            print(str(Manager.add_item(num, strcuk_typ)) + "\n")
        elif(option == "5"):
            strcuk_typ = "arbol AVL"
            print(str(Manager.add_item(num, strcuk_typ)) + "\n")
        else:
            print("*** Opcion invalida ***")
    else:
        print("*** Error al mover ***")


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
