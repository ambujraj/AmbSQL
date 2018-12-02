import os
import sqlite3
import string
import getpass
#USE PANDAS DB
os.system("title "+"AmbSQL")
try:
    os.system("IF NOT EXIST C:\AmbSQL MKDIR C:\AmbSQL")
except:
    pass
def main():
    db = sqlite3.connect("C:\\AmbSQL\dtables.db")
    c = db.cursor()
    print("AmbSQL shell version: 1.0.2.0")
    print("")
    print("Type 'docs()' for documentation")
    print("")
    cnt = 0
    while(True):
        command = input("> ").lower()
        if(command=="connect"):
            usern = input("Enter user-name: ").lower()
            passw = getpass.getpass('Enter password: ')
            if(usern=="system" and passw=="123"):
                cnt = 1
                print("Connected.")
            elif(usern=="sys" and passw=="123"):
                print("connection as SYS is not Authorised for Users!!")
                print("")
            else:
                print("Username or Password entered wrong!!")
        elif(command=="createtable()"):
            if(cnt!=1):
                print("ERROR: Not Connected !!")
                
            else:
                #tname should be unique
                tname = input("Enter table name: ").upper()
                c1 = input("Enter 1st Column name: ").upper()
                c2 = input("2nd Column name: ").upper()
                c3 = input("3rd Column name: ").upper()
                c.execute("CREATE TABLE IF NOT EXISTS "+tname+" (id INTEGER PRIMARY KEY, "+c1+" TEXT, "+c2+" TEXT, "+c3+" TEXT)")
                db.commit()
                print("TABLE CREATED!!")
                del tname
                del c1
                del c2
                del c3
        elif(command.startswith("insertvalues(") and command.endswith(")")):
            if(cnt != 1):
                print("ERROR: Not Connected !!")
            else:
                abc = command[13:-1].upper()
                x1 = input("Enter 1st Column Value: ")#table name missing
                x2 = input("2nd Column Value: ")
                x3 = input("3rd Column Value: ")
                try:
                    c.execute("INSERT INTO "+abc+" VALUES(NULL, ?,?,?)",(x1,x2,x3))
                    db.commit()
                    print("SUCCESSFULL!!")
                except:
                    print("Table Not Found!!")
                del x1
                del x2
                del x3
                del abc
        elif(command.startswith("showtable(") and command.endswith(")")):
            if(cnt != 1):
                print("ERROR: Not Connected !!")
            else:
                abc = command[10:-1].upper
                x = c.execute("select * from "+abc)
                row = x.fetchone()
    
                while row is not None:
                    print(row)
                    row = x.fetchone()
                del abc
                del x
                del row
        elif(command=="clear()"):
            os.system("cls")
            main()
main()
