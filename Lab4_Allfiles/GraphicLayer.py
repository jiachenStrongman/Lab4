#graphic layer for lab4
import matplotlib.pyplot as plt
import socket
import json

#start 2001 client connect -----------------
s = socket.socket()
host = socket.gethostname()
port = 2001
s.connect((host, port))
jsonString = s.recv(1024).decode() #receieves json string from businessLayer
country = s.recv(1024).decode()

plt.close()
xpoints = []
ypoints = []
for i in json.loads(jsonString):
    xpoints.append(i[0])
    ypoints.append(i[1])
plt.plot(xpoints, ypoints)
plt.title(country)
plt.xlabel("YEAR")
plt.ylabel("VALUE")
plt.show()

