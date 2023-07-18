# import pyodbc
import sqlalchemy as sa
server = 'testdatabasejrodriguez.database.windows.net' 
database = 'bridgeinto' 
username = 'charlie' 
password = 'Ch1v45ii1*' 
# conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
# cursor = conn.cursor()
args = (username, password, server, database)
connstr = "mssql+pyodbc://{}:{}@{}/{}?driver=FreeTDS&port=1433&odbc_options='TDS_Version=8.0'"
conn = sa.create_engine(connstr.format(*args))

