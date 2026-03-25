import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS banco (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titular TEXT NOT NULL,
                saldo FLOAT NOT NULL,
                cpf TEXT NOT NULL UNIQUE)
                """)

cursor.execute(f"""INSERT INTO banco
                (titular, saldo, cpf) VALUES
                ('{input("Seu nome: ")}',{input("Seu saldo atual: ")}, '{input("Seu CPF: ")}')
                """)

cursor.execute("""SELECT * FROM banco""")

banco = cursor.fetchall()
print(banco)

cursor.execute("""SELECT titular,saldo FROM banco
                WHERE saldo > 100""")

ContasMaior100 = cursor.fetchall()
print(ContasMaior100)

cursor.execute("""DELETE FROM banco WHERE saldo = 0""")

cursor.execute("""UPDATE banco
                SET saldo = saldo - 100
                WHERE titular = 'Enzo'""")

cursor.execute("""SELECT * FROM banco""")

print(cursor.fetchall())


conexao.commit()