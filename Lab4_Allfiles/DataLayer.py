#lab 4 data layer
#uses SQl class from previous labs to create database from DataFile

import sqlite3
import socket
import re
import xml.etree.ElementTree as et

def isAlphaNum(str): #im using this to just make sure that only valid table names are used
    regex = "^[\sA-Za-z0-9_-]*$"
    p = re.compile(regex)
    if(str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False

class database:

    def __init__(self, countryDB):
        self.countryDB = sqlite3.connect('countries.db')
        cursor = self.countryDB.cursor()
        print("Database Connected")
        cursor.close()
        if(self.countryDB):
            self.countryDB.close()

    def table(self, name): #make a table for each country with columns of [ | year | value | ]
        #table name is country name, that way with search we can find country faster
        if(name[0].isdigit() == False): #makes sure that first char is not digit
            if(isAlphaNum(name)): #makes sure that all char of the name is alphanumeric
                self.countryDB = sqlite3.connect('countries.db')
                cursor = self.countryDB.cursor()
                cursor.execute('''CREATE TABLE ''' + str('`' + name + '`') + '''( YEAR INTEGER PRIMARY KEY, VALUE REAL);''')
                print("Table Created")
                self.countryDB.commit()
                if(self.countryDB):
                    self.countryDB.close()

    def insert(self, year, val, table): #insert into desired table
        self.countryDB = sqlite3.connect('countries.db')
        cursor = self.countryDB.cursor()
        insertTab = '''INSERT INTO `''' + table + '''` (YEAR, VALUE) VALUES (?, ?)'''
        data_tuple = (year, val)
        cursor.execute(insertTab, data_tuple)
        self.countryDB.commit()
        cursor.close()
        if(self.countryDB):
            self.countryDB.close()

nations = database([])

tree = et.parse('UNData.xml') #parse datafile
root = tree.getroot()

country = []
year = []
value = []

for v in root.iter('Value'): #populates value list
    if(v.text not in value):
        value.append(v.text)

for c in root.iter('Country'): #populates country list
    if (c.text not in country):
        country.append(c.text)

for y in root.iter('Year'): #populates year list
    if(y.text not in year):
        year.append(y.text)

for x in country: #populates the database with each individual country table
    nations.table(x)

count = 0 #keeps count of which point in the value list in order to retrieve the right value
for i in country: #populates each country table with their year and value
    for j in year:
        nations.insert(j, value[count], i)
        count += 1
            
#database is created from here on out


