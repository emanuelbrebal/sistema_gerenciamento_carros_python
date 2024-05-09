import sqlite3

conexao = sqlite3.connect('carros.sqlite')
cursor = conexao.cursor()

def create_table(): #cria a tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo VARCHAR NOT NULL,
            ano_carro INTEGER NOT NULL,
            qtd_portas INTEGER NOT NULL,
            potencia INTEGER NOT NULL
        );
    """)
    conexao.commit()

create_table()

def insert_car(modelo, ano_carro, qtd_portas, potencia): #insere valores na tabela
    cursor.execute("""
        INSERT INTO cars(modelo, ano_carro, qtd_portas, potencia) VALUES (?, ?, ?, ?)
    """, [modelo, ano_carro, qtd_portas, potencia])
    conexao.commit()




