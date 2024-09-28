# Transport layer
* [DNS](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2105/TransportLayer.md#dns-domain-name-system) 
* [Addressing Process](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2105/TransportLayer.md#addressing-processes)
* [Socket](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2105/TransportLayer.md#sockets)
* [UDP](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2105/TransportLayer.md#udp)
* [TCP](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2105/TransportLayer.md#tcp)

# DNS (Domain Name System)
There are two ways to identify a host
* Hostname
    * a string idenfier like www.example.org
* IP address
    * a 32 bit integer split into 4 segment eg 93.184.216.34 

> [!NOTE]
> Both Hostname and IP Address refer to the same device. But Hostname is more hu;man friendly
> However, devices uses IP addresses. Browser will identify the hostname, then convert it 
> to IP for connection. This is a service provided by DNS.

> [!WARNING]
> The mapping of IP to Hostname may not be one to one. E.g Google.com is mapped to many IPs

### Resource Record (DNS:RR)
RR format:(name, value, type, ttl) <br>
| Type | name | value | 
| ---- | ---- | ----- | 
| A    | hostname | IP address |
| CNAME (Canonical Name)| alias name | canonical name | 
| NS (Name Server)| domain | value | 
| MX (Mail Exchange)| address | name of mail server | 

### Distributed, Hierarchical Database
DNS stored RR in distributed databses implemented in hierarchy of many name servers
1. First layer would be the Root DNS Server
2. Second layer will be the many top level domain (TLD) DNS server (eg .com/ .org/ .edu)
3. Lastly it will then lead to the website (Authorative) DNS server (eg. Facebook DNS Server)

### Caching
Once a name server learns mapping, it caches mapping for future uses. 

> [!WARNING]
> Cached entries may be out of date and will expire after some time (TTL). if name host changes IP address,
> it may not be known Internet-wide until all TTLs expire

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
    * uses **one socket** to server all clinets
    * **no connection** is establised before sending data 
    * Sender explicitly attaches **destination IP address + port #** 
* TCP: unreliable datagram socket
    * Server creates a new socket for each client
    * Client establishes a handshake/ **connection** to server 
    * server uses the **connection** to identify the client  

> [!TIP]
> Conceptually, you can treat a socket = IP Address + port number 

# UDP
1. server listen to port 53 
2. client 1 send packet to server (explicitly attaches destination IP address and 
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
