# bibliotecas
import sqlite3

# Configurações iniciais de um banco de dados para SQlite3
conexao = sqlite3.connect("banco.db")   # Nome do arquivo do banco de dados
cursor = conexao.cursor()               # Cursor do banco de dados

# Criação de um banco de dados (nesse caso com as colunas: id, titular, saldo, cpf)
cursor.execute("""CREATE TABLE IF NOT EXISTS banco (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titular TEXT NOT NULL,
                saldo FLOAT NOT NULL,
                cpf TEXT NOT NULL UNIQUE)
                """)

# Inserir dados no banco
cursor.execute(f"""INSERT INTO banco
                (titular, saldo, cpf) VALUES
                ('{input("Seu nome: ")}',{input("Seu saldo atual: ")}, '{input("Seu CPF: ")}')
                """)

# Consulta geral e inprimir retorno
cursor.execute("""SELECT * FROM banco""")
banco = cursor.fetchall()
print(banco)

# Consulta com filtro
cursor.execute("""SELECT titular,saldo FROM banco
                WHERE saldo > 100""")
ContasMaior100 = cursor.fetchall()
print(ContasMaior100)

# Deletar dados do banco
cursor.execute("""DELETE FROM banco WHERE saldo = 0""")

# Atualizar dados 
cursor.execute("""UPDATE banco
                SET saldo = saldo - 100
                WHERE titular = 'Enzo'""")
cursor.execute("""SELECT * FROM banco""")
print(cursor.fetchall())

# Enviar atualizações feitas
conexao.commit()