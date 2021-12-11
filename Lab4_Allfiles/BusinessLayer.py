#business layer lab4
import socket
import os

#start client 1998 side-----------------
s = socket.socket()
host = socket.gethostname()
port = 1998 #connects to userLayer
s.connect((host, port))
country = s.recv(1024).decode() #recieves the country data from userLayer
print("recieved: " + country + " as country") 
s.close()
#end client connect-----------------

#start server 1999 connect-----------------
countrySock = socket.socket()
port = 1999 #connect to DataLayer
countrySock.bind((host, port))
countrySock.listen(1)
os.system('start cmd /k "python DataLayer.py"')

c, addr = countrySock.accept()
print('Connected to ', addr)
c.send(country.encode())
c.close()
#end server connect

#start client 2000 connect-----------------

jsonSock = socket.socket()
port = 2000
jsonSock.connect((host, port))
jsonString = jsonSock.recv(1024).decode()
jsonSock.close()
print("Recieved json string")

#start server 2001 Connect-----------------
gs = socket.socket()
port = 2001
gs.bind((host, port))
gs.listen(1)
os.system('start cmd /k "GraphicLayer.py"')

c, addr = gs.accept()
print('Connected to ', addr)
c.send(jsonString.encode())
c.send(country.encode())
c.close()
#end server connect-----------------
