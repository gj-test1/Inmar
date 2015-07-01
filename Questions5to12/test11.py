import mysql.connector

try:
    cnx = mysql.connector.connect(host="localhost", user='root', passwrrd="", database='employeeDB');
    
    if cnx.is_connected():
        print "Connected to MySql DB!";
        cursor = cnx.cursor();

        cursor.execute("SELECT * FROM employees");
        
        for name in cursor:
            print name;
                 
except Error as e:
    print e;
finally:
    cnx.close();