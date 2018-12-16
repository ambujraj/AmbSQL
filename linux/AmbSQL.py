import sys
import getpass
import string
import sqlite3
import os
#os.system("title "+"AmbSQL")
try:
    os.system("mkdir DB")
except:
    pass
path = 'DB/'
db = sqlite3.connect(path+"dtables.db")
c = db.cursor()
dbu = sqlite3.connect(path+"duser.db")
cu = dbu.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS USERS(id INTEGER PRIMARY KEY,user TEXT,pass TEXT)")
dbu.commit()
usern = ""

def main(cnt):
    os.system("clear")
    print("AmbSQL shell version: 1.0.2.0")
    print("")
    print("Type 'docs()' for documentation")
    print("")
    while(True):
        try:
            command = input("> ").lower().strip()
            if(command == "connect"):
                cnt = 0
                usern = str(input("Enter user-name: ")).lower().strip()
                passw = str(getpass.getpass('Enter password: '))
                if(usern == "system" and passw == "123"):
                    cnt = 1
                    print("Connected.")
                else:
                    temp = cu.execute("SELECT USER,PASS FROM USERS WHERE USER= ? AND PASS= ?", (usern, passw))
                    for i in temp:
                        if(str(i[0]) == str(usern) and str(i[1]) == str(passw)):
                            cnt = 1
                            print("Connected.")
                            break
                    if(cnt == 0):
                        print("Username or Password entered wrong!!")
                        del usern
                    del temp

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
                                c.execute("CREATE TABLE " + tname +" (id INTEGER PRIMARY KEY,last_mod TEXT)")
                                for j in range(1, len(l1)):
                                    c.execute("ALTER TABLE " + tname +" ADD " + a[j - 1] + " TEXT")
                                db.commit()
                                print("Table Created.")
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
                                c.execute("INSERT INTO "+tname +" VALUES(NULL,?"+",?"*(len(l1)-1)+")", (usern,)+at)
                                db.commit()
                                print("One row inserted.")
                            except:
                                print("ERROR!! Invalid Entry!")
                            del at, a, tname
                        else:
                            print("ERROR!! There should be atleast two Parameters!")
                        del l1
                    else:
                        print("ERROR!! Please Enter the Table name!")
                    del abc
            elif(command.startswith("createuser(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Authorized !!")
                elif(usern == "system"):
                    abc = command[11:-1].lower().strip()
                    if(len(abc) != 0):
                        l1 = abc.split(",")
                        if(len(l1) == 2):
                            l1[0] = l1[0].strip()
                            l1[1] = l1[1].strip()
                            at = tuple(l1)
                            try:
                                cu.execute("INSERT INTO USERS VALUES(NULL,?,?)", at)
                                dbu.commit()
                                print("User Created.")
                            except:
                                print("ERROR!! Invalid Entry!")
                            del at
                        else:
                            print("ERROR!! There should be two Parameters!")
                        del l1
                    else:
                        print("ERROR!! Please Enter the Table name!")
                    del abc
                else:
                    print("ERROR: Not Authorized !!")
            elif(command.startswith("deleteuser(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Authorized !!")
                elif(usern == "system"):
                    abc = command[11:-1].lower().strip()
                    if(len(abc) != 0):
                        l1 = abc.split(",")
                        if(len(l1) == 1):
                            l1[0] = l1[0].strip()
                            at = tuple(l1)
                            try:
                                cu.execute("DELETE FROM USERS WHERE user= ?", at)
                                dbu.commit()
                                print("User Deleted.")
                            except:
                                print("ERROR!! Invalid Entry!")
                            del at
                        else:
                            print("ERROR!! There should be one Parameters!")
                        del l1
                    else:
                        print("ERROR!! Please Enter the Table name!")
                    del abc
                else:
                    print("ERROR: Not Authorized !!")
            elif(command.startswith("showtable(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[10:-1].upper().strip()
                    if(len(abc) != 0):
                        try:
                            c.execute("pragma table_info('"+abc+"')")
                            abv = c.fetchall()
                            print("       cid\t    name\t       pk")
                            print("----------\t--------\t---------")
                            for p, q, r, s, t, u in abv:
                                print(" "*(10-len(str(p)))+str(p)+"\t"+" " *(8-len(str(q)))+str(q)+"\t"+" "*(9-len(str(u)))+str(u))
                            print("")
                        except:
                            print("ERROR!! Table Not Found!")
                    else:
                        print("ERROR!! Please Enter the Table name!")
            elif(command.startswith("showvalues(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")

                else:
                    try:
                        abc = command[11:-1].upper().strip()
                        if(len(abc) != 0):
                            c.execute("pragma table_info('"+abc+"')")
                            abv = c.fetchall()
                            for p, q, r, s, t, u in abv:
                                print(" "*(9-len(str(q)))+str(q), end="\t")
                            print("")

                            for p, q, r, s, t, u in abv:
                                print("---------", end="\t")
                            print("")

                            c.execute("SELECT * FROM "+abc)
                            tables = c.fetchall()
                            for i in tables:
                                for j in i:
                                    print(" "*(9-len(str(j)))+str(j), end="\t")
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
                            '''
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
                                #os.system("IF EXIST C:\AmbSQL\\" + tname +".csv " + "DEL /F C:\AmbSQL\\" + tname + ".csv")
                                print("All Rows Deleted.")
                            except:
                                print("ERROR!! Invalid Table name!")
                            del tname
                        elif(len(l1) == 2):
                            tname = l1[0].strip().upper()
                            drow = l1[1].lower()
                            dd = drow.split("==")
                            if(len(dd) == 2):
                                col = dd[0].strip()
                                if(col=='id'):
                                    valued = dd[1].strip()
                                else:
                                    valued = str(dd[1]).strip()
                                try:
                                    if(col=='id'):
                                        c.execute("DELETE FROM "+tname +" WHERE "+col+"="+valued+";")
                                    else:
                                        c.execute("DELETE FROM "+tname + " WHERE "+col+" = '"+valued+"';")
                                    db.commit()
                                    #os.system("IF EXIST C:\AmbSQL\\" + tname + ".csv " + "DEL /F C:\AmbSQL\\" + tname + ".csv")
                                    print("Row(s) Deleted.")
                                except:
                                    print("ERROR!! Invalid Parameters!")
                                del col, valued
                            else:
                                print("ERROR!! Invalid Equivalence of Row and Value!")
                            del dd, drow, tname
                        else:
                            print("ERROR!! Entry should contain one or two parameters!")
                        del l1
                    else:
                        print("ERROR!! Entry should have atleast one parameter!")
                    del abc
            elif(command.startswith("updatevalue(") and command.endswith(")")):
                if (cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[12:-1]
                    if(len(abc) != 0):
                        l1 = abc.split(",")
                        if(len(l1) == 2):
                            tname = l1[0].strip()
                            dd = l1[1].split("=")
                            if(len(dd)==2):
                                col = dd[0].strip()
                                valued = str(dd[1]).strip()
                                try:
                                    c.execute("UPDATE "+tname+" SET "+col+"='"+valued+"';")
                                    db.commit()
                                    print("Row(s) Updated.")
                                except:
                                    print("ERROR!! Invalid Parameters!")
                                del col, valued
                            else:
                                print("ERROR!! Invalid Entry!")
                        elif(len(l1)==3):
                            tname = l1[0].strip()
                            dd = l1[1].split("=")
                            if(len(dd) == 2):
                                col = dd[0].strip()
                                valued = str(dd[1]).strip()
                                dd1 = l1[2].split("==")
                                if(len(dd1)==2):
                                    col1 = dd1[0].strip()
                                    if(col1=='id'):
                                        valued1 = dd1[1].strip()
                                    else:
                                        valued1 = str(dd1[1]).strip()
                                    try:
                                        if(col1=='id'):
                                            c.execute("UPDATE "+tname+" SET "+col+"='"+valued+"' WHERE id= ?", (valued1))
                                        else:
                                            c.execute("UPDATE "+tname+" SET "+col+"='"+valued+"' WHERE "+col1+"='"+valued1+"';")
                                        db.commit()
                                        print("Row Updated.")
                                    except:
                                        print("ERROR!! Invalid Parameters!")
                                    del col1, valued1
                                else:
                                    print("ERROR!! Invalid Equivalence of Row and Value!")
                                del col, valued, dd1
                            else:
                                print("ERROR!! Invalid Entry!")
                            del tname, dd
                        else:
                            print("ERROR!! Entry should contain two or three parameters!")
                        del l1
                    else:
                        print("ERROR!! Entry should have atleast two parameter!")
                    del abc
            elif(command == "clear()"):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    main(1)
            elif(command == "docs()"):
                print("")
                print("Copyright (c) 2018, Ambuj. All rights reserved.")
                print("")
                print("\tconnect                                                                 - To login to Database")
                print("\tcreateTable(<table-name>, <column1-name> , <column2-name>, ....)        - To create new Table")
                print("\tinsertValues(<table_name>, <column1-value> , <column2-value>, ...)      - To enter the values in Table")
                print("\tshowTable(<table_name>)                                                 - To show the Table schema")
                print("\tshowValues(<table_name>)                                                - To show the Table values")
                print("\tupdatevalue(<table_name> , <assignment>)                                - To Update all values of column")
                print("\tupdatevalue(<table_name> , <assignment> , <condition>)                  - To Update the values of column")
                print("\tdeleteTable(<table_name>)                                               - To truncate the Table")
                print("\tdeleteTable(<table_name> , <condition>)(e.g- deletetable(ab,name==jack))- To delete row(s) from Table")
                print("\tdropTable(<table_name>)                                                 - To drop the Table")
                print("\talterTable(<old-table_name> , <new-table_name>)                         - To rename Table Name")
                print("\tcreateUser(<user_name> , <password>)                                    - To create new User")
                print("\tdeleteUser(<user_name>)                                                 - To delete a User")
                print("\tlogout()                                                                - To Logout")
                print("\tclear()                                                                 - To clear the Screen")
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
                                #os.system("IF EXIST C:\AmbSQL\\"+old1 +".csv "+"DEL /F C:\AmbSQL\\"+old1+".csv")
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
                            #os.system("IF EXIST C:\AmbSQL\\" + abc +".csv " + "DEL /F C:\AmbSQL\\" + abc + ".csv")
                            print("Table Dropped.")
                        except:
                            print("ERROR!! Invalid Table Name!")
                    else:
                        print("ERROR!! Please Enter the Table name!")
                    del abc
            elif(command == "logout()"):
                cnt = 0
                print("Successfully Logged Out.")
            else:
                print("Command not found!!(please ensure you include '()' at the end)")
        except KeyboardInterrupt:
            print("KEYBOARD INTERRUPT")
            dbu.close()
            db.close()
            os.system("clear")
            sys.exit(0)

main(0)
