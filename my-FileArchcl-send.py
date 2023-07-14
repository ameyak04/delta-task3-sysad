if __name__ == "__main__":
    import time
    import socket  # Import socket module
    sock = socket.socket()  # Create a socket object
    host = socket.gethostname() #  Get local machine name
    port = 12312

    sock.connect((host, port))

    number = int(input("Please input the no. of files you want to upload:"))
    i=1
    sock.send(str(number).encode())
while (i<=number):
    fileName = input("Please enter your fileName: ")
    in_file = open(fileName, "rb")
    sock.send(str(fileName).encode())
    time.sleep(0.100)
    data = in_file.read(1024)
    sock.sendall(bytes(data))
    print("Done sending %s"%fileName)
    i=i+1
    
print("Successfully sent the files")
