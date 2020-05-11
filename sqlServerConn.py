import pyodbc

def lerCliente(conn):
    print("LerConexao")
    cursor = conn.cursor()
    cursor.execute("select * from tabCliente")
    for row in cursor:
        print(f'row = {row}')
    print()

def criarCliente(conn):
    print("Criar")
    cursor = conn.cursor()
    cursor.execute(
        'insert into tabCliente(a,b) values(?,?);',
        (1211, 'silvio')
    )
    conn.commit()
    read(conn)

def actualizarCliente(conn):
    print("Actualizar Cliente")
    cursor = conn.cursor()
    cursor.execute(
        'update tabCliente set b = ? where a = ?;',
        ('silvio', 1211)
    )
    conn.commit()
    read(conn)

def apagarCliente(conn):
    print("apagar Cliente")
    cursor = conn.cursor()
    cursor.execute(
        'delete from tabCliente where a > 5'
    )
    conn.commit()
    read(conn)    

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-OGHOFHSQ;"
    "Database=Test;"
    "Trusted_Connection=yes;"
)

lerCliente(conn)
criarCliente(conn)
actualizarConexao(conn)
apagarCliente(conn)

conn.close()