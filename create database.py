
import pyodbc                                       #pyodbc is an -extension- of python.
conn = pyodbc.connect('Driver={SQL Server};'        #Driver=**Type here the name of the program I want to use, in this case is SQL server, but it could be access (in that case is typed as: {r'driver=  ) or another one.               
                      'Server=DESKTOP-PARI4K9;'     #Server=**Type here the name of the server to which I want to connet**
                      'Trusted_Connection=yes;')    #Query (unknown by me)

cursor = conn.cursor()

cursor.execute('create database PonnyVioleta')

for row in cursor:
    print(row)
