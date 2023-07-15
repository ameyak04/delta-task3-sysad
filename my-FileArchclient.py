if __name__ == "__main__":
    import socket  # Import socket module
    import time

    port = 12312  # Reserve a port for your service.
    sock = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    sock.connect((host, port))


    User= input("User:")
    sock.send(str(User).encode())
    Password=input("Enter Password:")
    sock.send(str(Password).encode())

    request=input("Enter UPLOAD/DOWNLOAD: ")
    sock.send(str(request).encode())

if request == 'DOWNLOAD':
    n = int(input("Please input the no. of files you want to download:"))
    sock.send(str(n).encode())
    i=1
    while i<=n:    
        file_name = input("Please enter your fileName: ")
        sock.send(str(file_name).encode())
        file=sock.recv(1024).decode()
        time.sleep(0.100)
        with open(file, 'wb') as in_file :
            print("File opened")
            print("Receiving data...")
            while True:
                data = sock.recv(1024)
                if not data:
                    break
            
        print(f"Done receiving file{i}")
        i=i+1

elif request == 'UPLOAD':
    number = int(input("Please input the no. of files you want to upload:"))
    i=1
    sock.send(str(number).encode())
    while (i<=number):
        fileName = input("Please enter your fileName: ")
        sock.send(str(fileName).encode())
        with open(fileName, "rb") as in_file:
            while True:
                data = in_file.read(1024)
                if not data:
                    break
                sock.send(data)
        print("Done sending %s"%fileName)
        i=i+1
    
    print("Successfully sent the files")




        
