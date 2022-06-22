#pip install pyodbc
import pyodbc

conect_bd = (
    #tipo de bd
    "Driver={SQL Server};"
    #Nome do server
    "Server=DESKTOP-9QRQSJ0\SQLEXPRESS;"
    #nome do banco de dados
    "Database=bd;"
)

conect = pyodbc.connect(conect_bd)
print("deu certo!")