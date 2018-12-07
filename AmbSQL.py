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
            command = input("> ").lower().strip()
            if(command == "connect"):
                usern = str(input("Enter user-name: ")).lower()
                passw = str(getpass.getpass('Enter password: '))
                if(usern == "system" and passw == "123"):
                    cnt = 1
                    print("Connected.")
                elif(usern == "sys" and passw == "123"):
                    print("connection as SYS is not Authorised for Users!!")
                    print("")
                else:
                    print("Username or Password entered wrong!!")
                del usern

            elif(command.startswith("createtable(") and command.endswith(")")):
                if (cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[12:-1].upper()
                    if (len(abc) != 0):
                        l1 = abc.split(",")
                        if (len(l1) >= 2):
                            tname = l1[0]
                            a = []
                            for i in range(1, len(l1)):
                                a.insert(i - 1, l1[i].lower().strip())
                            try:
                                c.execute("CREATE TABLE " + tname +" (id INTEGER PRIMARY KEY)")
                                for j in range(1, len(l1)):
                                    c.execute("ALTER TABLE " + tname +" ADD " + a[j - 1] + " TEXT")
                                db.commit()
                                print("TABLE CREATED!!")
                            except:
                                print("ERROR!! Table Name and Attribute name should be unique!")
                            del tname, a
                        else:
                            print("ERROR!! There should be atleast two Parameters!")
                        del l1
                    else:
                        print("ERROR!! Please Enter the Table name!")
                    del abc
            elif(command.startswith("insertvalues(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[13:-1].upper().strip()
                    if(len(abc) != 0):
                        l1 = abc.split(",")
                        if(len(l1) >= 2):
                            tname = str(l1[0])
                            a = []
                            for i in range(1, len(l1)):
                                a.insert(i-1, str(l1[i]).lower().strip())
                            at = tuple(a)
                            try:
                                c.execute("INSERT INTO "+tname +" VALUES(NULL"+",?"*(len(l1)-1)+")", at)
                                db.commit()
                                print("One row inserted!!")
                            except:
                                print("ERROR!! Invalid Entry!")
                            del at, a, tname
                        else:
                            print("ERROR!! There should be atleast two Parameters!")
                        del l1
                    else:
                        print("ERROR!! Please Enter the Table name!")
                    del abc
            elif(command.startswith("showschema(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[11:-1].upper().strip()
                    if(len(abc)!=0):
                        try:
                            c.execute("pragma table_info('"+abc+"')")
                            abv = c.fetchall()
                            print("       cid\t    name\t       pk")
                            print("----------\t--------\t---------")
                            for p,q,r,s,t,u in abv:
                                print(" "*(10-len(str(p)))+str(p)+"\t"+" "*(8-len(str(q)))+str(q)+"\t"+" "*(9-len(str(u)))+str(u))
                            print("")
                        except:
                            print("ERROR!! Table Not Found!")
                    else:
                        print("ERROR!! Please Enter the Table name!")
            elif(command.startswith("showtable(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    try:
                        abc = command[10:-1].upper().strip()
                        if(len(abc) != 0):
                            '''
                            c.execute("pragma table_info('"+abc+"')")
                            abv = c.fetchall()
                            for p,q,r,s,t,u in abv:
                                print(q, end="\t  ")
                            print("")
                            for p,q,r,s,t,u in abv:
                                print("-"*len(q), end="\t  ")
                            print("")
                            c.execute("SELECT * FROM "+abc)
                            tables = c.fetchall()
                            for i in tables:
                                for j in i:
                                    print(str(j), end="\t  ")
                                print("")
                            '''
                            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
                            tables = c.fetchall()
                            for table_name in tables:
                                table_name = table_name[0]
                                table = pd.read_sql_query("SELECT * from %s" % table_name, db)
                                table.to_csv(path+table_name +'.csv', index=None)
                            pdr = pd.read_csv(path+abc+'.csv')
                            print(pdr)
                            del pdr
                        else:
                            print("ERROR!! Please Enter the Table name!")
                        del abc
                    except:
                        print("ERROR!! Table Not Found!")
            elif(command.startswith("deletetable(") and command.endswith(")")):
                if (cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[12:-1]
                    if (len(abc) != 0):
                        l1 = abc.split(",")
                        if(len(l1) == 1):
                            tname = l1[0].strip().upper()
                            try:
                                c.execute("DELETE FROM "+tname)
                                db.commit()
                                os.system("IF EXIST C:\AmbSQL\\" + tname +".csv " + "DEL /F C:\AmbSQL\\" + tname + ".csv")
                                print("All Rows Deleted!!")
                            except:
                                print("ERROR!! Invalid Table name!")
                            del tname
                        elif(len(l1) == 2):
                            tname = l1[0].strip().upper()
                            drow = l1[1].lower()
                            dd = drow.split("=")
                            if(len(dd) == 2):
                                col = dd[0].strip()
                                valued = dd[1].strip()
                                try:
                                    c.execute("DELETE FROM "+tname +" WHERE "+col+"="+valued+";")
                                    db.commit()
                                    os.system("IF EXIST C:\AmbSQL\\" + tname + ".csv " + "DEL /F C:\AmbSQL\\" + tname + ".csv")
                                    print("Row(s) Deleted!!")
                                except:
                                    print("ERROR!! Invalid Parameters!")
                                del col, valued
                            else:
                                print("ERROR!! Invalid Equivalence of Row and Value!")
                            del dd, drow, tname
                        else:
                            print("ERROR!! Entry should contain one or two parameters!")
                    else:
                        print("ERROR!! Entry should have atleast one parameter!")
            elif(command == "clear()"):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    main(1)
            elif(command == "docs()"):
                print("")
                print("Copyright (c) 2018, Ambuj. All rights reserved.")
                print("")
                print("\tconnect                                                            - To login to Database")
                print("\tcreateTable(<table-name>, <column1-name> , <column2-name>, ....)   - To create new Table")
                print("\tinsertValues(<table_name>, <column1-value> , <column2-value>, ...) - To enter the values in Table")
                print("\tshowSchema(<table_name>)                                           - To show the Table schema")
                print("\tshowTable(<table_name>)                                            - To show the Table with values")
                print("\tdeleteTable(<table_name>)                                          - To truncate the Table")
                print("\tdeleteTable(<table_name> , <condition>)                            - To delete row(s) from Table")
                print("\tdropTable(<table_name>)                                            - To drop the Table")
                print("\talterTable(<old-table_name> , <new-table_name>)                    - To rename Table Name")
                print("\tclear()                                                            - To clear the Screen")
                print("")
                print("\tnote=> Username: 'system', password: '123'")
            elif(command.startswith("altertable(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[11:-1].upper()
                    try:
                        if(len(abc) != 0):
                            l1 = abc.split(",")
                            if(len(l1) == 2):
                                old1 = l1[0].strip()
                                new1 = l1[1].strip()
                                c.execute("ALTER TABLE "+old1 +" RENAME TO "+new1)
                                db.commit()
                                os.system("IF EXIST C:\AmbSQL\\"+old1 +".csv "+"DEL /F C:\AmbSQL\\"+old1+".csv")
                                print("Table name Updated from " +
                                      old1+" to "+new1)
                                del old1, new1
                            else:
                                print("ERROR!! There should be two Parameters!")
                        else:
                            print("ERROR!! Please Enter the Table names!")
                    except:
                        print("ERROR!! Invalid Table Name!")
                    del abc
            elif(command.startswith("droptable(") and command.endswith(")")):
                if (cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[10:-1].upper().strip()
                    if(len(abc) != 0):
                        try:
                            c.execute("DROP TABLE "+abc)
                            db.commit()
                            os.system("IF EXIST C:\AmbSQL\\" + abc +".csv " + "DEL /F C:\AmbSQL\\" + abc + ".csv")
                            print("Table Dropped!!")
                        except:
                            print("ERROR!! Invalid Table Name!")
                    else:
                        print("ERROR!! Please Enter the Table name!")
                    del abc
            elif(command == "logout()"):
                cnt = 0
                print("Successfully Logged Out!!")
            else:
                print("Command not found!!(please ensure you include '()' at the end)")
        except KeyboardInterrupt:
            print("KEYBOARD INTERRUPT")
            db.close()
            os.system("cls")
            sys.exit(0)
main(0)
