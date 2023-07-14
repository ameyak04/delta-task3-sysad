if __name__ == "__main__":
    import socket  # Import socket module

    port = 12312  # Reserve a port for your service.
    sock = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    sock.connect((host, port))

    n = int(input("Please input the no. of files you want to download:"))
    sock.send(str(n).encode())
    i=1
    while i<=n:    
        file_name = input("Please enter your fileName: ")
        sock.send(str(file_name).encode())
        file_name = sock.recv(1024).decode()
        print("%s\n"%file_name)
        new_file=("%s"%file_name)
        in_file =open(new_file, "wb")   

        print("File opened")
        print("Receiving data...")
        done=False
        while not done:
            data = sock.recv(1024).decode()
            print(data)
            break
        i=i+1   
        print(f"Done receiving file{i}")

        
