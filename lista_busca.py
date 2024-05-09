import sqlite3

conexao = sqlite3.connect('carros.sqlite')
cursor = conexao.cursor()

def list_cars():
    cars = cursor.execute("""
            SELECT * FROM cars
    """).fetchall()
    print(cars)

def list_cars_byId(id):
    cars = cursor.execute("""
            SELECT * FROM cars WHERE id = ?
    """, [id]).fetchall()
    print(cars)
