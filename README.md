# scapy4dummy


It's never been so simple to use Scapy in cybersecurity purposes.

# **Operations Available**

- Arp scan
- Port scan

# **Dependency requirements** 

```
scapy
```

# **Installing dependencies**

Please run the following commands
```
pip install -r requirements.txt
``` 

# **Getting started**

## Instaling scapy4dummy package

(Working...)

After install the scapy4dummy package, run your first scans with the examples bellow:

> Running a ARP scan

```
from scapy4dummy.operations.ArpScanner import ArpScanner

scan_result = ArpScanner.send_arp_packet(target_ip='192.168.5.1/24', timeout=10)
clients = ArpScanner.get_clients(arp_result=scan_result)
print(clients)
```


> Running a PORT scan

```
from scapy4dummy.operations.PortScanner import PortScanner

ip_target_list = ['192.168.5.1', 'www.google.com']
port_list = [25, 80, 443, 8080]
scan_result = PortScanner.start_full_scan(ip_target_list, port_list, timeout=10, verbose=False)
print(scan_result)
```


# **Project structure**

```
project/
	scapy4dummy/
		exceptions/
            OperationErrorException.py
        operations/
			ArpScanner.py
			PorScanner.py
          
	requirements.txt
	.gitignore
    setup.py
    LICENSE
    README.md
```

# **Modules description**

## **Operations**

### **ArpScanner**

```send_arp_packet```

```get_clients```

```start_scan```

### **PortScanner**

```tcp_scan```

```udp_scan```

```start_full_scan```
