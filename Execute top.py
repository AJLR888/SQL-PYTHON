import pyodbc

conn = pyodbc.connect ('Driver={SQL Server};'
                       'Server=DESKTOP-PARI4K9;'
                       'Database=DevelopmentDB;'
                       'Trusted_connection=Yes;')


Cursor.execute('select * from DevelopmentDB.dbo.PonnyVioleta')

for row in cursor:
    print(row)
