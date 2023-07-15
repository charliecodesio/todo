import pyodbc

server = 'testdatabasejrodriguez.database.windows.net' 
database = 'bridgeinto' 
username = 'charlie' 
password = 'Ch1v45ii1*' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = conn.cursor()

