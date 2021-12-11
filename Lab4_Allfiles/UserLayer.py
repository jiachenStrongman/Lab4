from tkinter import*
import socket
import sqlite3
import os
import xml.etree.ElementTree as et


interface = Tk()
interface.title("Country Select")
interface.geometry("300x300")

tree = et.parse('UNData.xml') #parse datafile
root = tree.getroot()
listOptions = []
for c in root.iter('Country'):
    if (c.text not in listOptions):
        listOptions.append(c.text)

selected = [] #needed data

prompt = Label(interface, text = "CHOOSE YOUR COUNTRY", font = ("arial", 15))
prompt.pack()

def select():
    selected.append(clicked.get())
    print(selected)
    interface.destroy()
    s = socket.socket()
    host = socket.gethostname()
    port = 1998 #<-----------START
    s.bind((host, port))
    s.listen(3)
    print(os.getcwd())
    os.system('start cmd /k "python BusinessLayer.py"')#opens businessLayer
    c, addr = s.accept()
    print('connected to', addr)
    c.send(selected[0].encode())
    c.close()
    

closeButton = Button(interface, text = "CLOSE AND GET PLOT", command = select)
closeButton.pack()

#set datatype on menu
clicked = StringVar()
#intial text 
clicked.set("COUNTRIES")
#pull down menu
pullDown = OptionMenu(interface, clicked, *listOptions)
pullDown.pack()

#from here the program can create the UI and store the desired country
