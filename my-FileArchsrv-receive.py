if __name__ == "__main__":
    import zipfile # Import Zipfile module
    import socket  # Import socket module

    port = 12312  # Reserve a port for your service.
    sock = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    sock.bind((host, port))  # Bind to the port
    sock.listen(5)  # Now wait for client connection.

    print("Server listening....")
    
    conn, addr = sock.accept()  # Establish connection with client.
    print(f"Got connection from {addr}")
    n = int(conn.recv(1024).decode())
    print(n)    
    i=1   
    while i<=n:    
        file_name = conn.recv(1024).decode()
        print("%s"%file_name)
        new_file=("%s"%file_name)
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
        zip_file=("/%s.zip"%new_file_name)

        print(zip_file)
        with zipfile.ZipFile(zip_file,"w",compression= zipfile.ZIP_DEFLATED) as z:
            z.writestr(file_name,data)
            print("Compression complete ")
    
