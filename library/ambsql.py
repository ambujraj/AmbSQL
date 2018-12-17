import string
import sqlite3
import os
if(os.name == 'nt'):
    try:
        os.system("IF NOT EXIST C:\AmbSQL MKDIR C:\AmbSQL")
    except:
        pass
    path = 'C:\\AmbSQL\\'
else:
    try:
        os.system("mkdir DB")
    except:
        pass
    path = 'DB/'
    # Connect to Tables Database
db = sqlite3.connect(path+"dtables.db")
c = db.cursor()


def createtable(tname="", *cols):
    x = list(cols)
    for s in range(len(cols)):
        x[s] = str(x[s])
    y = tuple(x)
    del x
    try:
        c.execute("CREATE TABLE " + tname + " (id INTEGER PRIMARY KEY)")
        for j in y:
            c.execute("ALTER TABLE " + tname + " ADD " + j + " TEXT")
        db.commit()
    except:
        raise ValueError("Table Name and Attribute name should be unique!")


def insertvalues(tname="", *cols):
    x = list(cols)
    for s in range(len(cols)):
        x[s] = str(x[s])
    y = tuple(x)
    del x
    try:
        c.execute("INSERT INTO "+tname +
                  " VALUES(NULL"+",?"*(len(cols))+")", y)
        db.commit()
    except:
        raise ValueError("Table Name not found!")


def showtable(tname=""):
    try:
        c.execute("pragma table_info('"+tname+"')")
        abv = c.fetchall()
        print("       cid\t    name\t       pk")
        print("----------\t--------\t---------")
        for p, q, r, s, t, u in abv:
            print(" "*(10-len(str(p)))+str(p)+"\t"+" " *
                  (8-len(str(q)))+str(q)+"\t"+" "*(9-len(str(u)))+str(u))
        print("")
    except:
        raise ValueError("Table Not Found!")


def showvalues(tname=""):
    try:
        c.execute("pragma table_info('"+tname+"')")
        abv = c.fetchall()
        for p, q, r, s, t, u in abv:
            print(" "*(9-len(str(q)))+str(q), end="\t")
        print("")

        for p, q, r, s, t, u in abv:
            print("---------", end="\t")
        print("")

        c.execute("SELECT * FROM "+tname)
        tables = c.fetchall()
        for i in tables:
            for j in i:
                print(" "*(9-len(str(j)))+str(j), end="\t")
            print("")
    except:
        raise ValueError("Table Not Found!")


def deletetable(tname=""):
    try:
        c.execute("DELETE FROM "+tname)
        db.commit()

    except:
        raise ValueError("Table name not found!")
def altertable(otname="", ntname=""):
    try:
        c.execute("ALTER TABLE "+otname +
                  " RENAME TO "+ntname)
        db.commit()
    except:
        raise ValueError("Table name not found!")


def droptable(self, tname=""):
    try:
        self.c.execute("DROP TABLE "+tname)
        self.db.commit()
    except:
        raise ValueError("Invalid Table Name!")
