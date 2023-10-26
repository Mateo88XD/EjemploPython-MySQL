import mysql.connector

class  DAO:

    def __init__(self):
        self.conn = None

    # Coneccion
    def conectar(self):
        self.conn = mysql.connector.connect(user='root', password = 'root', host = 'localhost', database = 'bibloteca', port = '3306' )
        self._cursor = self.conn.cursor()
        if self.conn.is_connected():
            print("Conectando")   
    #--------------------------------------------------
    # Desconeccion
    def desconectar(self):
        self.conn.close()
        if self.conn:
            print("Desconectado")
    #------------------------------------------------------
    # Cosultas a la Base de Datos
    def consultar(self, sql):
        self._cursor.execute(sql)
        resultado = self._cursor.fetchall()
        return resultado
    #----------------------------------------------------
    # Alteracion a la Base de Datos
    def insertarModificrEliminar(self,sql):
        self._cursor.execute(sql)
        self.conn.commit() #Confirmacion de la acción