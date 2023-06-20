import DAO

class DAOlibro(DAO.DAO): # La clase DAOlibro HEREDA de DAO es decir que puede usar los metodos de DAO sin nesesidad de un objeto DAO

    def __init__(self):# Todo los datos NO aceptan valores nulos

        super().__init__()
        self.conectar()
        self.ISBN = None # Llave Primaria
        self.Titulo = None
        self.Editorial = None
        self.Autor = None
        self.Genero = None

    def Disconnect(self):
        self.desconectar()

    def SELECT(self, opc):
        if opc == 1: #Se Busca toda la columna ISBN
            sql = "SELECT ISBN FROM libro;"
            for fila in  self.consultar(sql):
                print("ISBN")
                print(fila[0])
        
        elif opc == 2: #Se Busca toda la columna Titulo
            sql = "SELECT Titulo FROM libro;"
            for fila in  self.consultar(sql):
                print("Titulos")
                print(fila[0])
        elif opc == 3: #Se Busca toda la columna Editorial
            sql = "SELECT Editorial FROM libro;"
            for fila in  self.consultar(sql):
                print("Editoriales")
                print(fila[0])
        elif opc == 4: #Se Busca toda la columna Autor
            sql = "SELECT Autor FROM libro;"
            for fila in  self.consultar(sql):
                print("Autores")
                print(fila[0])
        elif opc == 5: #Se Busca toda la columna Genero
            sql = "SELECT Genero FROM libro;"
            for fila in  self.consultar(sql):
                print("ISBN")
                print(fila[0])
        elif opc == 6: #Se Busca toda la tabla
            sql = "SELECT * FROM libro;"
            for fila in  self.consultar(sql):
                print(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]}")

    def INSERT(self):
        self.ISBN = int(input("Ingrese el ISBN: "))
        self.Titulo = input("Ingrese el Titulo: ")
        self.Editorial = input("Ingrese la Editorial: ")
        self.Autor = input("Ingrese el nombre del Autor: ")
        self.Genero = input("Ingrese el Genero: ")
        sql = "INSERT INTO libro (ISBN,Titulo,Editorial,Autor,Genero) VALUES ('" + str(self.ISBN) + "','" + self.Titulo + "','" + self.Editorial + "','" + self.Autor + "','" + self.Genero + "');"
        self.insertarModificrEliminar(sql)

    def UPDATE(self,opc):
        self.ISBN = int(input("Indique el ISBN a Cambiar"))
        if opc == 1: # Se modifica el Titulo segun el ISBN

            self.Titulo = input("Indique el nuevo Titulo: ")
            sql = "UPDATE libro SET Titulo = '" + self.Titulo + "' WHERE ISBN = '" + str(self.ISBN) + "';"
            self.insertarModificrEliminar(sql)

        elif opc == 2: # Se modifica la Editorial segun el ISBN

            self.Editorial = input("Indique la nueva Editorial: ")
            sql = "UPDATE libro SET Editorial = '" + self.Editorial + "' WHERE ISBN = '" + str(self.ISBN) + "';"
            self.insertarModificrEliminar(sql)

        elif opc == 3: # Se modifica el Autor segun el ISBN

            self.Autor = input("Indique el nuevo Autor: ")
            sql = "UPDATE libro SET Autor = '" + self.Autor + "' WHERE ISBN = '" + str(self.ISBN) + "';"
            self.insertarModificrEliminar(sql)

        elif opc == 4: # Se modifica el Genero segun el ISBN

            self.Genero = input("Indique el nuevo Genero: ")
            sql = "UPDATE libro SET Genero '" + self.Genero + "' WHERE ISBN = '" + str(self.ISBN) + "';"
            self.insertarModificrEliminar(sql)

        elif opc == 5: # Se modifica el ISBN

            newISBN = int(input("Indique el nuevo ISBN: "))
            sql = "UPDATE libro SET ISBN = '" + str(newISBN) + "' WHERE ISBN = '" + str(self.ISBN) + "';"
            self.insertarModificrEliminar(sql)
        
    def DELETE(self):

        self.ISBN = int(input("Indique el ISBN a borrar: "))
        sql = "DELETE FROM libro WHERE ISBN = '" + str(self.ISBN) + "';"
        opc = input(f"Seguro de eliminar la fila {self.ISBN}? Y/N = ")
        if opc.upper == "Y":
            self.insertarModificrEliminar(sql)
            print("Dato eliminado")
        else:
            print("Se a cancelado la eliminacion")


        
    