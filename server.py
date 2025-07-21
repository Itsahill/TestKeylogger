import socket

# Creating a socket
host = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, 9999))
sock.listen(1)

# Accepting the Client Connection
print("Waiting for Client...")
conn,addr = sock.accept()
print("Connection from " + addr[0] + " Confirmed.")

#Printing Data from Client
while True:
    data = conn.recv(1024)
    if data:
        print(data.decode('utf-8'))
