# scapy4dummy

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

(working...)


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
