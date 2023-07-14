if __name__ == "__main__":
    import zipfile # Import Zipfile module
    import socket  # Import socket module
    import time

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
        new_file_name=file_name.split('.')[0]
        zip_file=("%s.zip"%new_file_name)
        with zipfile.ZipFile(zip_file,"w") as z:
            z.extractall()
        new_file=("%s"%file_name)
        in_file = open(new_file, "rb")
        conn.send(str(new_file).encode())
        time.sleep(0.100)
        data = in_file.read(1024)
        conn.sendall(bytes(data))
        print("Done sending %s"%file_name)
        i=i+1
