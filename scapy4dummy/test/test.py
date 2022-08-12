from scapy4dummy.operations.ArpScanner import ArpScanner
from scapy4dummy.operations.PortScanner import PortScanner
from scapy4dummy.utils.FileHandler import FileHandler
import json
#from . import PortScanner
#scan_result = ArpScanner.start_scan(['192.168.5.1/24', '192.168.1.1/24'])
#FileHandler.save_file('arp_result.json', 'w', json.dumps(scan_result))
#print(ArpScanner.start_scan(['192.168.5.1/24', '192.168.1.1/24']))
#ip_target_list = ['192.168.5.1', 'www.google.com']
#port_list = [25, 80, 443, 8080]
#scan_result = PortScanner.start_full_scan(ip_target_list, port_list, timeout=10, verbose=False)
#FileHandler.save_file('port_result.json', 'w', json.dumps(scan_result))
#print(scan_result)