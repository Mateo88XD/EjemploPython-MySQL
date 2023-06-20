import DAOlibro

def Menu():
    
    while True:
        print("///MENU///")
        print("1_ Select")
        print("2_ Insert")
        print("3_ Update")
        print("4_ Delete")
        print("5_ Salir")
        opc = int(input("Elige una opcion: "))
        if opc == 1:
            MenuSelect()
        elif opc == 2:
            book.INSERT()
        elif opc == 3:
            MenuUpdate()
        elif opc == 4:
            book.DELETE()
        elif opc == 5:
            book.Disconnect()
            break

def MenuSelect(): # Problema en el bucle probar y coregir
    while True:
        print("///SELECT///")
        print("1_ ISBN")
        print("2_ Titulo")
        print("3_ Editorial")
        print("4_ Autor")
        print("5_ Genero")
        print("6_ Todo")
        print("7_ Atras")
        opc = int(input("Elige una opcion: "))
        if opc == 1:
            book.SELECT(opc)
        elif opc == 2:
            book.SELECT(opc)
        elif opc == 3:
            book.SELECT(opc)
        elif opc == 4:
            book.SELECT(opc)
        elif opc == 5:
            book.SELECT(opc)
        elif opc == 6:
            book.SELECT(opc)
        elif opc == 7:
            break

def MenuUpdate():
    while True:
        print("///UPDATE///")
        print("1_ Titulo")
        print("2_ Editorial")
        print("3_ Autor")
        print("4_ Genero")
        print("5_ ISBN")
        print("6_ Atras")
        opc = int(input("Elige una opcion: "))
        if opc == 1:
            book.UPDATE(opc)
        elif opc == 2:
            book.UPDATE(opc)
        elif opc == 3:
            book.UPDATE(opc)
        elif opc == 4:
            book.UPDATE(opc)
        elif opc == 5:
            book.UPDATE(opc)
        elif opc == 6:
            break

book = DAOlibro.DAOlibro()
Menu()