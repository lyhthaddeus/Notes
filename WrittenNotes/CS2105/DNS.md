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
