
import pandas as pd
from DAO import DAO

dao = DAO()

exelRuta = "C:/Users/mateo/OneDrive/Escritorio/Proyectos/PruebasMySQL/PruebasExel-sql/Libros.xlsx"


dao.conectar()

df = pd.read_excel(exelRuta)

print("Lectura realizada")

for index, row in df.iterrows():
    ISBN = str(row['ISBN'])
    Titulo = row['Titulo']
    Editorial = row['Editorial']
    Autor = row['Autor']
    Genero = row['Genero']

    sql = f"INSERT INTO libro (ISBN, Titulo, Editorial, Autor, Genero) VALUE ('{ISBN}','{Titulo}','{Editorial}','{Autor}','{Genero}')"

    dao.insertarModificrEliminar(sql)

dao.desconectar()

print("Ya se cargaron los datos y desconeccion exitosa")