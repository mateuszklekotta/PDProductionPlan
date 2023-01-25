import pyodbc
import pandas as pd
print(pyodbc.drivers())

cnxn_str = ("Driver={SQL Server};"
            "Server=TEST5;"
            "Database=TEST5;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()
data = pd.read_sql("SELECT TOP(2) * FROM BOM", cnxn)
print(type(data))
