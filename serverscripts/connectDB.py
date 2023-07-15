import psycopg2
import string
User= input("User:")
print("User: ",User)
Password=input("Enter Password:")
print("Password is : ",Password)
#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='mysecretpassword', host='mydbcontainer', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute("select * from student where name=%s",(User,))

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print (data)
for row in data:
        DBPassword=format(row[1])
print (DBPassword)

if Password == DBPassword:
    print("Both strings are  equal") # return if true
else:
    print("Both strings are not equal") # return if false
#Closing the connection
conn.close()
