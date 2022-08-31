from scapy4dummy.operations.PortScanner import PortScanner
from scapy4dummy.operations.ArpScanner import ArpScanner

ip_target_list = ['192.168.5.1', 'www.google.com', 'poli.br']
port_list = [25, 80, 443, 8080]
scan_result = PortScanner.start_full_scan(ip_target_list, port_list, timeout=10, verbose=False)
#print(scan_result)


#scan_result = ArpScanner.start_scan(target_ip_list=['192.168.1.1/24'], timeout=30)
#clients = ArpScanner.get_clients(arp_result=scan_result)
#print(clients)