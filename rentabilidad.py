import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")

# Obteniendo los 10 productos más rentables
query = '''
    SELECT 
        ProductName,
        SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

# top_products = pd.read_sql_query(query, conn) # Esta función abre las conexiones y crea los cursores de forma automática
# top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10,5), legend=False)

# plt.title("10 productos más rentables")
# plt.xlabel("Productos")
# plt.ylabel("Ganancias p/Producto")
# plt.xticks(rotation=90)
# plt.show()

# Obteniendo los empleados más efectivos
query2 = '''
    SELECT
        FirstName || " " || LastName as Empleado,
        COUNT(*) as Total_ventas
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total_ventas ASC
    LIMIT 3
'''

top_employees = pd.read_sql_query(query2, conn)
top_employees.plot(x="Empleado", y="Total_ventas", kind="bar", figsize=(10,5), legend=False)

plt.title("Empleados más efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total Ventas")
plt.xticks(rotation=45)
plt.show()
