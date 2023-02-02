import pyodbc
import pandas as pd

import ProdTableQuery

print(pyodbc.drivers())

cnxn_str = ("Driver={SQL Server};"
            "Server=sql1;"
            "Database=MicrosoftDynamicsAX_PROD;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()
data = pd.read_sql(ProdTableQuery.QueryString, cnxn)
print(data)
print(type(data))
