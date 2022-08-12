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

## Instaling scapy4dummy locally

After clone this repository, check the following examples

> Running a ARP scan

```
from scapy4dummy.operations.ArpScanner import ArpScanner

scan_result = ArpScanner.send_arp_packet(target_ip='192.168.5.1/24', timeout=10)
clients = ArpScanner.get_clients(arp_result=scan_result)
print(clients)
```

Output example:

```
{
	    "192.168.1.1/24": {
        "clients": [
            {
                "ip_address": "192.168.1.1",
                "mac_address": "ff:ff:ff:ff:ff:ff"
            },
            {
                "ip_address": "192.168.1.102",
                "mac_address": "ff:ff:ff:ff:ff:ff"
            }
        ]
    }
}
```


> Running a PORT scan

```
from scapy4dummy.operations.PortScanner import PortScanner

ip_target_list = ['192.168.5.1', 'www.google.com']
port_list = [25, 80, 443, 8080]
scan_result = PortScanner.start_full_scan(ip_target_list, port_list, timeout=10, verbose=False)
print(scan_result)
```

Output example:
```
{
    "192.168.5.1": {
        "tcp_scan": [
            {
                "dst_port": 25,
                "status": "Closed"
            },
            {
                "dst_port": 80,
                "status": "Open"
            },
            {
                "dst_port": 443,
                "status": "Closed"
            },
            {
                "dst_port": 8080,
                "status": "Closed"
            }
        ],
        "udp_scan": [
            {
                "dst_port": 25,
                "status": "Closed"
            },
            {
                "dst_port": 80,
                "status": "Closed"
            },
            {
                "dst_port": 443,
                "status": "Closed"
            },
            {
                "dst_port": 8080,
                "status": "Closed"
            }
        ]
    },
    "www.google.com": {
        "tcp_scan": [
            {
                "dst_port": 25,
                "status": "Filtered"
            },
            {
                "dst_port": 80,
                "status": "Open"
            },
            {
                "dst_port": 443,
                "status": "Open"
            },
            {
                "dst_port": 8080,
                "status": "Filtered"
            }
        ],
        "udp_scan": [
            {
                "dst_port": 25,
                "status": "Open|Filtered"
            },
            {
                "dst_port": 80,
                "status": "Open|Filtered"
            },
            {
                "dst_port": 443,
                "status": "Open|Filtered"
            },
            {
                "dst_port": 8080,
                "status": "Open|Filtered"
            }
        ]
    }
}
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

```send_arp_packet```: Send a ARP request and returns all hosts responses.

```get_clients```: Handle the host responses, getting their IP and MAC addresses.

```start_scan```: Run a combined ARP request and retrives all clients.

### **PortScanner**

```tcp_scan```: Performs a TCP scan. Basically, send a SYN flag. 

```udp_scan```: Performs an UDP scan.

```start_full_scan```: Run a combined TCP + UDP scan.


## **Utils**

### **FileHandler**

Class is responsable for store all data obtained from scans. 