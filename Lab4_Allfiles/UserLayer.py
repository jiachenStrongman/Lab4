from tkinter import*
import sqlite3
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

selected = []

prompt = Label(interface, text = "CHOOSE YOUR COUNTRY", font = ("arial", 15))
prompt.pack()

def select():
    selected.append(clicked.get())

closeButton = Button(interface, text = "Close and get plot", command = interface.destroy)
closeButton.pack(side = 'bottom')

#set datatype on menu
clicked = StringVar()
#intial text 
clicked.set("COUNTRIES")
#pull down menu
pullDown = OptionMenu(interface, clicked, *listOptions)
pullDown.pack()


print(selected)
