from scapy.all import ARP, Ether, srp
#from exceptions.OperationErrorException import OperationErrorException

class ArpScanner:

    @staticmethod
    def send_arp_packet( 
    target_ip = '192.168.5.1/24', 
    ether_dst = 'ff:ff:ff:ff:ff:ff',
    timeout = 5):
        try:
            arp = ARP(pdst = target_ip)
            ether = Ether(dst = ether_dst)
            packet = ether / arp
            result = srp(packet, timeout = timeout)
            return result
        except Exception as ex:
            #raise OperationErrorException(f'Fatal error on send_arp_packet: {str(ex)}')
            pass

    @staticmethod
    def get_clients(arp_result):
        clients = []
        for sent, received in arp_result:
            clients.append({
                'ip_address': received.psrc,
                'mac_address': received.hwsrc
            })
        return clients

    @staticmethod
    def start_scan(target_ip_list, timeout = 5):
        ip_addr_report_list = {}
        for ip_addr in target_ip_list:
            try:
                print(f"{ip_addr} - STARTING SCAN")
                arp_result = ArpScanner.send_arp_packet(ip_addr, timeout=timeout)
                clients = ArpScanner.get_clients(arp_result[0])
            except Exception as ex:
                    print(f"{ip_addr} - SCAN FAILED: {str(ex)}")
                    break

            print(f"{ip_addr} - SCAN SUCCESSFULLY")
            ip_addr_report_list[ip_addr] = {"clients": clients}

        return ip_addr_report_list


print(ArpScanner.start_scan(['192.168.5.1/24', '192.168.1.1/24']))