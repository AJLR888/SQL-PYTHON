import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AJLR;'
                      'Database=AdventureWorks2017;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('select * from AdventureWorks2017.person.Address')

for row in cursor:
    print (row)
