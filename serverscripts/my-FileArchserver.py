if __name__ == "__main__":
    import zipfile # Import Zipfile module
    import socket  # Import socket module
    import time
    import psycopg2

    port = 12312  # Reserve a port for your service.
    sock = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    sock.bind((host, port))  # Bind to the port
    sock.listen(5)  # Now wait for client connection.

    print("Server listening....")
    
    conn, addr = sock.accept()  # Establish connection with client.
    print(f"Got connection from {addr}")
    User = (conn.recv(1024).decode())
    Password = (conn.recv(1024).decode())

    #establishing the connection of database
    connect = psycopg2.connect( database="postgres", user='postgres', password='mysecretpassword', host='mydbcontainer', port= '5432')
    #Creating a cursor object using the cursor() method
    cursor = connect.cursor()

    cursor.execute("select * from student where name=%s",(User,))

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    print (data)
    for row in data:
            DBPassword=format(row[1])
            DBUser=format(row[0])

if User == DBUser and Password == DBPassword:
    print("User has logged in") # return if true
    request = conn.recv(1024).decode()

    if request == 'DOWNLOAD':
        n = int(conn.recv(1024).decode())
        print(n)    
        i=1   
        while i<=n:
            file_name = conn.recv(1024).decode()
            new_file_name=file_name.split('.')[0]
            zip_file=(f"/data/{User}/{new_file_name}.zip")
            extracted_file=(f"/data/{User}/server/{file_name}")
            print(zip_file)
            with zipfile.ZipFile(zip_file,"r") as z:
                z.extractall(f"/data/{User}/server")
            conn.send(str(extracted_file).encode())    
            with open(extracted_file, "rb") as in_file:
                while True:
                    data = in_file.read(1024)
                    if not data:
                        break
                    conn.send(data)
            print(data)
            print("Done sending %s"%file_name)
            i=i+1

    elif request == 'UPLOAD':
        n = int(conn.recv(1024).decode())
        print(n)    
        i=1   
        while i<=n:    
             file_name = conn.recv(1024).decode()
             new_file=(f"/data/{User}/{file_name}")
             with open(new_file, "wb") as in_file :   
                print("File opened")
                print("Receiving data...")
                while True:
                    data = conn.recv(1024).decode()
                    print(data)
                    break
             i=i+1   
             print("Done receiving data")

        print("Compressing the file with Zip")
        new_file_name=file_name.split('.')[0]
        zip_file=(f"/data/{User}/{new_file_name}.zip")

        print(zip_file)
        with zipfile.ZipFile(zip_file,"w",compression= zipfile.ZIP_DEFLATED) as z:
            z.writestr(file_name,data)
            print("Compression complete ")

else:
   print("Not in database") # return if false
#Closing the connection
connect.close()
conn.close()
sock.close()
