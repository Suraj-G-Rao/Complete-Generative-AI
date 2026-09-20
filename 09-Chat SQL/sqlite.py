import sqlite3

## connect to sqllite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Suraj','Data Science','A',70)''')
cursor.execute('''Insert Into STUDENT values('Niroop','Data Science','B',99)''')
cursor.execute('''Insert Into STUDENT values('Anushree','Data Science','A',100)''')
cursor.execute('''Insert Into STUDENT values('Pranav','DEVOPS','A',75)''')
cursor.execute('''Insert Into STUDENT values('Sanjeev','DEVOPS','A',75)''')
cursor.execute('''Insert Into STUDENT values('Sankar','Cyber Security','A',99)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
