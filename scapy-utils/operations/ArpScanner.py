from scapy.all import ARP, Ether, srp
from exceptions.OperationErrorException import OperationErrorException

class ArpScanner:

    @staticmethod
    def send_arp_packet( 
    target_ip = '192.168.1.1/24', 
    ether_dst = 'ff:ff:ff:ff:ff:ff',
    timeout = 5):
        try:
            arp = ARP(pdst = target_ip)
            ether = Ether(dst = ether_dst)
            packet = ether / arp
            result = srp(packet, timeout = timeout)
            return result
        except Exception as ex:
            raise OperationErrorException(f'Fatal error on send_arp_packet: {str(ex)}')

    @staticmethod
    def get_clients(arp_result):
        clients = []
        for sent, received in arp_result:
            clients.append({
                'ip_address': received.psrc,
                'mac_address': received.hwsrc
            })
        return clients

ArpScanner.send_arp_packet(target_ip='123Banana')