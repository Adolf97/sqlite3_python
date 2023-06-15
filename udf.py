import sqlite3

square = lambda n: n*n

# Si usamos with, la conexión se cierra automáticamente
with sqlite3.connect("Northwind.db") as conn:
    conn.create_function("square", 1, square)
    cursor = conn.cursor()
    cursor.execute('SELECT Price, square(Price) FROM Products')
    results = cursor.fetchall()

print(results)
