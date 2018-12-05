import sys
import pandas as pd
import getpass
import string
import sqlite3
import os
os.system("title "+"AmbSQL")
#USE PANDAS DB
try:
    os.system("IF NOT EXIST C:\AmbSQL MKDIR C:\AmbSQL")
except:
    pass
path = 'C:\\AmbSQL\\'
db = sqlite3.connect(path+"dtables.db")
c = db.cursor()
dbu = sqlite3.connect(path+"duser.db")
cu = dbu.cursor()
def main(cnt):
    os.system("cls")
    print("AmbSQL shell version: 1.0.2.0")
    print("")
    print("Type 'docs()' for documentation")
    print("")
    while(True):
        try:
            command = input("> ").lower()
            if(command == "connect"):
                usern = input("Enter user-name: ").lower()
                passw = getpass.getpass('Enter password: ')
                if(usern == "system" and passw == "123"):
                    cnt = 1
                    print("Connected.")
                elif(usern == "sys" and passw == "123"):
                    print("connection as SYS is not Authorised for Users!!")
                    print("")
                else:
                    print("Username or Password entered wrong!!")
                del usern
            elif(command == "createtable()"):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")

                else:
                    tname = input("Enter table name: ").upper()
                    c1 = input("Enter 1st Column name: ").upper()
                    c2 = input("2nd Column name: ").upper()
                    c3 = input("3rd Column name: ").upper()
                    try:
                        c.execute(
                            "CREATE TABLE "+tname + " (id INTEGER PRIMARY KEY, "+c1+" TEXT, "+c2+" TEXT, "+c3+" TEXT)")
                        db.commit()
                        print("TABLE CREATED!!")
                    except:
                        print("Table Name already exists!!")
                    del tname, c1, c2, c3
            elif(command.startswith("insertvalues(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    try:
                        abc = command[13:-1].upper()
                        if(len(abc) != 0):
                            # table name missing
                            x1 = input("Enter 1st Column Value: ").lower()
                            x2 = input("2nd Column Value: ").lower()
                            x3 = input("3rd Column Value: ").lower()
                            try:
                                c.execute("INSERT INTO "+abc +
                                          " VALUES(NULL,?,?,?)", (x1, x2, x3))
                                db.commit()
                                print("SUCCESSFULL!!")
                            except:
                                print("ERROR!! Table Not Found!")
                            del x1, x2, x3
                        else:
                            print("Error!! Please Enter the Table name!")
                        del abc
                    except:
                        print("Error!! Table Not Found!")
            elif(command.startswith("showtable(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    try:
                        abc = command[10:-1].upper()
                        if(len(abc) != 0):
                            c.execute(
                                "SELECT name FROM sqlite_master WHERE type='table';")
                            tables = c.fetchall()
                            for table_name in tables:
                                table_name = table_name[0]
                                table = pd.read_sql_query(
                                    "SELECT * from %s" % table_name, db)
                                table.to_csv(path+table_name +
                                             '.csv', index_label='index')
                            pdr = pd.read_csv(
                                path+abc+'.csv', usecols=[1, 2, 3, 4])
                            print(pdr)
                            del pdr
                        else:
                            print("Error!! Please Enter the Table name!")
                        del abc
                    except:
                        print("Error!! Table Not Found!")
            elif(command == "clear()"):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    main(1)
            elif(command == "docs()"):
                print("")
                print("Copyright (c) 2018, Ambuj. All rights reserved.")
                print("")
                print("\tconnect                    - To login to database")
                print("\tcreateTable()              - To create new table")
                print("\tinsertValues(<table_name>) - To enter the values in Table")
                print("\tshowTable(<table_name>)    - To show the Table with values")
                print("\tclear()                    - To clear the Screen")
                print("\tlogout()")                 - To logout
                print("")
                print("\tnote=> Username: 'system', password: '123'")
            elif(command== "logout()"):
                cnt = 0
                print("Successfully Logged Out!!")
            else:
                print("Command not found!!(please ensure you include '()' at the end)")
        except KeyboardInterrupt:
            os.system("cls")
            sys.exit(0)


main(0)
