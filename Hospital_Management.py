import mysql.connector

global where_clause
global order_by_clause
global group_by_clause
global update_value_clause

def insert():
    b = input("Do you want to insert data into all columns?(y/n)")
    if (b == 'y'):
        val = input("Enter values **FORMAT: value1, value2, ...***  :")
        myCur.execute(f"INSERT INTO payments VALUES ({val});")
    elif (b == 'n'):
        col = input("Enter columns **FORMAT: column1, column2, ...***  :")
        val = input("Enter values **FORMAT: value1, value2, ...***  :")
        myCur.execute(f"INSERT INTO payments ({col}) VALUES ({val});")
    mydb.commit()

def view():
    where_clause = ""
    order_by_clause = ""
    group_by_clause = ""
    
    a = input("Do you want a where clause?(y/n)")
    if (a=='y'):
        where_clause = input("Enter where clause: (Format: WHERE <column_name> = <value>)")
    b = input("Do you want a Order By clause?(y/n)")
    if (b=='y'):
        order_by_clause = input("Enter Order BY clause: (Format: ORDER BY <column_name> ASC/DSC)")
    c = input("Do you want a GROUP BY clause?(y/n)")
    if (c=='y'):
        group_by_clause = input("Enter Group BY clause: (Format: GROUP BY <column_name>)")
    myCur.execute(f"Select * from payments {where_clause} {order_by_clause} {group_by_clause};")
    mr = myCur.fetchall()
    for x in mr:
        print(x)

def update():
    where_clause = ""
    update_value_clause = ""
    a = input("Do you want a where clause?(y/n)")
    if (a=='y'):
        where_clause = input("Enter where clause **Format: WHERE <column_name> = <value>** :")
    update_value_clause = input("Enter update clause **FORMAT: <Column-Name> = <value>** :")
    myCur.execute(f"Update payments SET {update_value_clause} {where_clause};")
    mydb.commit()


def delete():
    where_clause = ""
    a = input("Do you want a where clause?(y/n)")
    if (a=='y'):
        where_clause = input("Enter where clause: (Format: WHERE <column_name> = <value>)")
    myCur.execute(f"DELETE FROM payments {where_clause};")
    mydb.commit()

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "*******"
    database = "databaseName"
)

myCur = mydb.cursor()

print("*** Welcome ***")

print("1. View      2. Update       3. Delete       4. Insert")

choice = 1

while choice in range(1,5):
    choice = int(input("Enter your choice: "))

    if choice == 1:
        view()
    elif choice == 2:
        update()
    elif choice == 3:
        delete()
    elif choice == 4:
        insert()
    else:
        print("Invalid choice, please chose from the above.")