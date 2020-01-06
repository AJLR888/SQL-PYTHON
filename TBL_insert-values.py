
import pyodbc                                       #pyodbc is an -extension- of python.
conn = pyodbc.connect('Driver={SQL Server};'        #Driver=**Type here the name of the program I want to use, in this case is SQL server, but it could be access (in that case is typed as: {r'driver=  ) or another one.               
                      'Server=DESKTOP-PARI4K9;'     #Server=**Type here the name of the server to which I want to connet**
                      'Database=DevelopmentDB;'     #Database=**Type here the name of the database we want to use**
                      'Trusted_Connection=yes;')    #Query (unknown by me)

cursor = conn.cursor()
cursor.execute('SELECT top 2* FROM Development.dbo.Purchase')

for row in cursor:
    print(row)

########################################################################
