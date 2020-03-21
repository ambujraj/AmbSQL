#!usr/bin/env python3
import sys
import getpass
import string
import sqlite3
import os
import datetime
if(os.name=='nt'):
    os.system("title "+"AmbSQL")
    try:
        os.system("IF NOT EXIST C:\AmbSQL MKDIR C:\AmbSQL") # Create Folder AmbSQL for storage of Database file
    except:
        pass
    path = 'C:\\AmbSQL\\'
# For Linux and MacOS
else:
    try:
        os.system("mkdir -p /home/"+os.getlogin()+"/DB")
    except:
        pass
    path = '/home/'+os.getlogin()+'/DB/'
db = sqlite3.connect(path+"dtables.db") # Connect to Tables Database
c = db.cursor()
dbu = sqlite3.connect(path+"duser.db") # Connect to Users Database
cu = dbu.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS USERS(id INTEGER PRIMARY KEY,user TEXT,pass TEXT)")
dbu.commit()
usern = ""
def main(cnt):
    if(os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")
    print("AmbSQL shell version: 1.0.2   "+str(datetime.datetime.now()))
    print("")
    print("Type 'docs()' for documentation")
    print("")
    while(True):
        try:
            command = input("> ").lower().strip() # Input Command
            if(command == "connect"):
                cnt = 0
                usern = str(input("Enter user-name: ")).lower().strip() # Input Username
                passw = str(getpass.getpass('Enter password: ')) # Input Password
                # Username, Password Auth
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
            # Create Table
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
            
            # Sum Values of an Attribute in Table
            elif(command.startswith("sumvalue(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    try:
                        abc = command[9:-1].strip()
                        if(len(abc) != 0):
                            l1 = abc.split(",")
                            if(len(l1) == 2):
                                tname = str(l1[0])
                                attr = str(l1[1])

                                c.execute("SELECT SUM("+attr+") FROM " + tname)
                                ans = list(c.fetchone())
                                ans = str(ans).strip('[]')
                                print("Sum : " + ans)
                                del ans, tname, attr, l1
                            else:
                                print("Error: There should be only two parameters") 
                        else:
                            print("ERROR: Please Enter the command correctly")
                             
                        del abc  
                    except:
                        print("ERROR: Please Enter the parameters correctly")

             	 


            # Max Value of an Attribute in Table
            #Note: It only works on Integer-type (numerical attributes)
            elif(command.startswith("maxvalue(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    try:
                        abc = command[9:-1].strip()
                        if(len(abc) != 0):
                            l1 = abc.split(",")
                            if(len(l1) == 2):
                                tname = str(l1[0])
                                attr = str(l1[1])

                                c.execute("SELECT MAX("+attr+") FROM " + tname)
                                ans = list(c.fetchone())
                                ans = str(ans).strip('[]')
                                print("Max : " + ans)
                                del ans, tname, attr, l1
                            else:
                                print("Error: There should be only two parameters") 
                        else:
                            print("ERROR: Please Enter the command correctly")
                             
                        del abc  
                    except:
                        print("ERROR: Please Enter the parameters correctly")

            # Min Value of an Attribute in Table
            #Note: It only works on Integer-type (numerical attributes)
            elif(command.startswith("minvalue(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    try:
                        abc = command[9:-1].strip()
                        if(len(abc) != 0):
                            l1 = abc.split(",")
                            if(len(l1) == 2):
                                tname = str(l1[0])
                                attr = str(l1[1])

                                c.execute("SELECT MIN("+attr+") FROM " + tname)
                                ans = list(c.fetchone())
                                ans = str(ans).strip('[]')
                                print("Min : " + ans)
                                del ans, tname, attr, l1
                            else:
                                print("Error: There should be only two parameters") 
                        else:
                            print("ERROR: Please Enter the command correctly")
                             
                        del abc  
                    except:
                        print("ERROR: Please Enter the parameters correctly")

            # Average Value of an Attribute in Table
            #Note: It only works on Integer-type (numerical attributes)
            elif(command.startswith("avgvalue(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    try:
                        abc = command[9:-1].strip()
                        if(len(abc) != 0):
                            l1 = abc.split(",")
                            if(len(l1) == 2):
                                tname = str(l1[0])
                                attr = str(l1[1])

                                c.execute("SELECT AVG("+attr+") FROM " + tname)
                                ans = list(c.fetchone())
                                ans = str(ans).strip('[]')
                                print("Average : " + ans)
                                del ans, tname, attr, l1
                            else:
                                print("Error: There should be only two parameters") 
                        else:
                            print("ERROR: Please Enter the command correctly")
                             
                        del abc  
                    except:
                        print("ERROR: Please Enter the parameters correctly")

            #replace Function added to replace all the occurences with another string
            elif(command.startswith("replace(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    try:
                        abc = command[8:-1].upper().strip()
                        if(len(abc) != 0):
                            l1 = abc.split(",")
                            if(len(l1) == 3):
                                full_str = str(l1[0])
                                st1 = str(l1[1])
                                st2 = str(l1[2])
                               
                                c.execute("SELECT REPLACE('"+full_str+"','"+st1+"','"+st2+"')")
                                
                                ans = list(c.fetchone())
                                ans = str(ans).strip('[]')
                                print("FINAL STRING : " + ans)
                                del ans, full_str,st1,st2, l1
                            else:
                                print("Error: There should be only three parameters") 
                        else:
                            print("ERROR: Please Enter the command correctly")
                             
                        del abc  
                    except:
                        print("ERROR: Please Enter the parameters correctly")


             #Substring Function to extract the characters from a string
            elif(command.startswith("substr(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    try:
                        abc = command[7:-1].strip()
                        if(len(abc) != 0):
                            l1 = abc.split(",")
                            if(len(l1) == 3):
                                full_str = str(l1[0])
                                st1 = str(l1[1])
                                st2 = str(l1[2])
                               
                                c.execute("SELECT substr('"+full_str+"','"+st1+"','"+st2+"')")
                                
                                ans = list(c.fetchone())
                                ans = str(ans).strip('[]')
                                print("SUB STRING : " + ans)
                                del ans, full_str,st1,st2, l1
                            else:
                                print("Error: There should be only three parameters") 
                        else:
                            print("ERROR: Please Enter the command correctly")
                             
                        del abc  
                    except:
                        print("ERROR: Please Enter the parameters correctly")


            #Fetched the currect DATE
            elif(command.startswith("today(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    abc = command[9:-1].strip()
                    if (len(abc) == 0):
                        try:
                            c.execute("SELECT DATE('now')")
                            ans = list(c.fetchone())
                            ans = str(ans).strip('[]')
                            print("Today's Date: " + ans)
                        except:
                            print("Please Enter the command correctly")
                    else:
                        print("ERROR: Please Enter the command correctly")

            #Lower case 
            elif(command.startswith("tolower(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    abc = command[8:-1].strip()
                    if (len(abc) != 0):
                        l1 = abc.split(",")
                        if(len(l1) == 1):
                            s = str(l1[0])
                            s = s.lower()
                            print(s)
                        else:
                            print("ERROR: There should only be one parameter")

                    else:
                        print("ERROR: Please Enter the command correctly")

            #Upper case 
            elif(command.startswith("toupper(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    abc = command[8:-1].strip()
                    if (len(abc) != 0):
                        l1 = abc.split(",")
                        if(len(l1) == 1):
                            s = str(l1[0])
                            s = s.upper()
                            print(s)
                        else:
                            print("ERROR: There should only be one parameter")

                    else:
                        print("ERROR: Please Enter the command correctly")


             #Length of a string 
            elif(command.startswith("length(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    abc = command[7:-1].strip()
                    if (len(abc) != 0):
                        l1 = abc.split(",")
                        if(len(l1) == 1):
                            s = str(l1[0])
                            s = int(len(s))
                            print(s)
                            
                        else:
                            print("ERROR: There should only be one parameter")

                    else:
                        print("ERROR: Please Enter the command correctly")


            #Absolute Function to return only positive numeric type value
            elif(command.startswith("absolute(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected")
                else:
                    abc = command[9:-1].strip()
                    if (len(abc) != 0):
                        l1 = abc.split(",")
                        if(len(l1) == 1):
                            try:
                                s = int(l1[0])
                                s = abs(s)
                                print(s)
                            except:
                                print("ERROR: Please Enter an integer numeric value")

                            
                        else:
                            print("ERROR: There should only be one parameter")

                    else:
                        print("ERROR: Please Enter the command correctly")

                                
            # Insert Values into Table
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
            # Create New User
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
            # Delete Existing User
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
            # Show Schema
            elif(command.startswith("showtable(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[10:-1].upper().strip()
                    if(len(abc) != 0):
                        try:
                            c.execute("pragma table_info('"+abc+"')")
                            abv = c.fetchall()
                            if(len(abv) > 0):                                   #Added Condition check, whether abv object contains something
                                print("       cid\t    name\t       pk")
                                print("----------\t--------\t---------")
                                for p, q, r, s, t, u in abv:
                                    print(" "*(10-len(str(p)))+str(p)+"\t"+" " *(8-len(str(q)))+str(q)+"\t"+" "*(9-len(str(u)))+str(u))
                                print("")
                            else:                                              #Else Table not found in database
                                print("Table Not Found!")
    
                        except:
                            print("ERROR!! Please Enter the correct table!")
                    else:
                        print("ERROR!! Please Enter the Table name!")

                    del abc                                                     #Added




            

            #Count the number of rows/records in a Table
            elif(command.startswith("counttable(") and command.endswith(")")):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    abc = command[11:-1].strip()
                    if(len(abc) != 0):
                        l1= abc.split(",")
                        if(len(l1) == 1):
                            tname = str(l1[0])
                            try:
                                c.execute("SELECT COUNT(*) FROM " + tname)
                                ans = list(c.fetchone())
                                print(str(ans).strip('[]') + " Record(s)")
                                del l1, tname, ans
                            except:
                                print("NO TABLE FOUND")
                    else:
                        print("ERROR!! Please Enter the Table name!")
                    del abc

          
                            
            # Show Values In Table
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
            # Delete Rows Either with Condition or Truncate Table
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
            # Update Values in Table either with condition or with no condition
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
            # Clear the Screen
            elif(command == "clear()"):
                if(cnt != 1):
                    print("ERROR: Not Connected !!")
                else:
                    main(1)
            # Documentation
            elif(command == "docs()"):
                print("")
                print("Copyright (c) 2018, Ambuj. All rights reserved.")
                print("")
                print("\tconnect                                                                 - To login to Database")
                print("\tcreatetable(<table-name>, <column1-name> , <column2-name>, ....)        - To create new Table")
                print("\tinsertvalues(<table_name>, <column1-value> , <column2-value>, ...)      - To enter the values in Table")
                print("\tshowtable(<table_name>)                                                 - To show the Table schema")
                print("\tshowvalues(<table_name>)                                                - To show the Table values")
                print("\tupdatevalue(<table_name> , <assignment>)                                - To Update all values of column")
                print("\tupdatevalue(<table_name> , <assignment> , <condition>)                  - To Update the values of column")
                print("\tdeletetable(<table_name>)                                               - To truncate the Table")
                print("\tdeletetable(<table_name> , <condition>)(e.g- deletetable(ab,name==jack))- To delete row(s) from Table")
                print("\tcounttable(<table_name>)                                                - To count the rows/records of Table")  #Documentation Updated for count()
                print("\tsumvalue(<table_name>, <attribute>)                                     - To sum of records of particular attribute of Table") #Function Added
                print("\tmaxvalue(<table_name>, <attribute>)                                     - To find the max value of particular attribute of Table") #Function Added 
                print("\tminvalue(<table_name>, <attribute>)                                     - To find the min value of particular attribute of Table") #Function Added 
                print("\tavgvalue(<table_name>, <attribute>)                                     - To find the average value of particular attribute of Table") #Function Added
                print("\tdroptable(<table_name>)                                                 - To drop the Table")
                print("\tcounttable(<table_name>)                                                - To count the rows/records of Table")  #Documentation Updated for count()
                print("\ttolower(<string>)                                                       - To change the string to lower case")
                print("\ttoupper(<string>)                                                       - To change the string to upper case")
                print("\tabsolute(<integer_value>)                                               - To find the absolute value") #Function Added
                print("\taltertable(<old-table_name> , <new-table_name>)                         - To rename Table Name")
                print("\tcreateuser(<user_name> , <password>)                                    - To create new User")
                print("\ttoday()                                                                 - To fetch the current date")
                print("\treplace(<string>,<first_char>,<second_char>)                            - To replace all occurrences of a specified string with another string")
                print("\tlength()                                                                - To fetch the length of a string")
                print("\tsubstr(<string>,<start_index>,<end_index>)                              - To fetch a substring from a string starting at a specified position with a predefined length")
                print("\tdeleteuser(<user_name>)                                                 - To delete a User")
                print("\tlogout()                                                                - To Logout")
                print("\tclear()                                                                 - To clear the Screen")
                print("")
                print("\tnote=> Username: 'system', password: '123'")
            # Alter Table Name
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
            # Drop Table
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
            # Logout From Current Session
            elif(command == "logout()"):
                cnt = 0
                print("Successfully Logged Out.")
            else:
                print("Command not found!!(please ensure you include '()' at the end)")
        # Handle KeyBoard Interrupt
        except KeyboardInterrupt:
            print("KEYBOARD INTERRUPT")
            dbu.close()
            db.close()
            if(os.name=='nt'):
                os.system("cls")
            else:
                os.system("clear")
            sys.exit(0)
# Call the main function
if __name__ == '__main__':
    main(0)
