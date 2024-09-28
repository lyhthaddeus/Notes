# Addressing Processes
A Process is identified by (IP address, port number). the port number is a 16 bit integer
* HTTP server: 80
* SMTP server: 25
* DNS server: 53 

> [!NOTE]
> IANA coordinates the assignment of port numbers: [IANA](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) 

# Sockets
Socket is the software interface between app processes and transort layer protocol.
Programming wise can be treated as a set of APIs. There are two types of Sockets
* UDP: reliable, byte stream-oriented socket
* TCP: unreliable datagram socket

# UDP
1. server listen to port 53 
2. client 1 send packet to server (explicityly attaches destination IP address and 
port number to **EACH** packet)
3. server extracts the sender IP address and port number from the packets

### UDP Echo Server
```python
from socket import *

serverPort = 2105

# create a socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind socket to local port number 2106
serverSocket.bind((', serverPort'))
print('Server is ready to receive message')

# extract client address from received packet
message, clientAddress = serverSocket.recvfrom(2048) # 2048 byte

serverSocket.sendto(message, clientAddress)

serverSocket.close()
```

### UDP Echo Client 
```python
from socket import *

serverName = 'localhost' # client, server on the same host
serverPort = 2105

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Enter a message: ')

# send msg to server address
clientSocket.sendto(message.encode(), (serverName, serverPort))

receivedMsg, serverAddress = clientSocket.recvfrom(2048)

print('from server:', receivedMsg.decode())

clientSocket.close()
```

# TCP
1. when client creates a socket, clinet TCP establishes a connection to server TCP. // handshake require
2. When contact by client, **server TCP creates a new socket** for servre process to communicate 
    with that client

### TCP Echo Server 
```python
from socket import *

serverPort = 2105

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.build(('', serverPort))

serverSocket.listen()
print('Server is ready to receive message')

connectionSocket, clinetAddr = serverSocket.accept()
message - connectionSocket.recv(2048)

connectionSocket.send(message)

connectionSocket.close()
```

### TCP Echo Client
```python
from socket import *

serverName = 'localhost'
serverPort = 2105 
 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input('Enter a message: ')

clientSocket.send(message.encode())

receivedMsg = clientSocket.recv(2048)

print('from server:', receivedMsg.decode())

clientSocket.close()
```
