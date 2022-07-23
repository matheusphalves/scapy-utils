from scapy.all import IP, TCP, UDP, sr1, sr, ICMP, RandShort
class PortScanner:
    
    @staticmethod
    def tcp_scan(dst_ip, dst_port, timeout = 10, verbose = True):
        status = None
        src_port = RandShort()
        scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=timeout, verbose = verbose)
        if(scan_resp is None):
            status = "Filtered"
        elif(scan_resp.haslayer(TCP)):
            if(scan_resp.getlayer(TCP).flags == 0x12): # ACK
                send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=timeout, verbose = verbose)
                status = "Open"
            elif (scan_resp.getlayer(TCP).flags == 0x14): # R
                status = "Closed"
        elif(scan_resp.haslayer(ICMP)):
            if(int(scan_resp.getlayer(ICMP).type)==3 and int(scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                status = "Filtered"

        return {'dst_ip': dst_ip, 'dst_port': dst_port, 'status': status}

    @staticmethod
    def udp_scan(dst_ip, dst_port, timeout, verbose = True):
        status = None
        udp_scan_resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=timeout, verbose = True)
        if (udp_scan_resp is None):
            return {'dst_ip': dst_ip, 'dst_port': dst_port, 'status': "Open|Filtered"}

        elif (udp_scan_resp.haslayer(UDP)):
            return {'dst_ip': dst_ip, 'dst_port': dst_port, 'status': "Open"}

        elif(udp_scan_resp.haslayer(ICMP)):
            if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code)==3):

                return {'dst_ip': dst_ip, 'dst_port': dst_port, 'status': "Closed"}

            elif(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
                return {'dst_ip': dst_ip, 'dst_port': dst_port, 'status': "Filtered"}
        else:
            return {'dst_ip': dst_ip, 'dst_port': dst_port, 'status': "CHECK"}

    @staticmethod
    def start_full_scan(ip_target_list, port_list, timeout = 5, verbose = False):
        ip_addr_report_list = {}

        for ip_addr in ip_target_list:
            print(f"[{ip_addr}] - STARTING SCAN")
            tcp_scan_list = []
            udp_scan_list = []
            for port in port_list:
                try:
                    tcp_scan = PortScanner.tcp_scan(ip_addr, int(port), int(timeout), verbose=verbose)
                    udp_scan = PortScanner.udp_scan(ip_addr, int(port), int(timeout), verbose=verbose)
                    tcp_scan.pop('dst_ip', None)
                    udp_scan.pop('dst_ip', None)
                    tcp_scan_list.append(tcp_scan)
                    udp_scan_list.append(udp_scan)
                    
                except Exception as ex:
                    print(f"{ip_addr}]:{port} - SCAN FAILED: {str(ex)}")
                    break

                print(f"[{ip_addr}]:{port} - SCAN SUCCESSFULLY")
                ip_addr_report_list[ip_addr] = {"tcp_scan": tcp_scan_list, "udp_scan": udp_scan_list}
            
            print(f"[{ip_addr}] - SCAN FINISHED")
        return ip_addr_report_list


print(PortScanner.start_full_scan(['127.0.0.1'], [3389, 3306], verbose=False))
#3389
#[20,21,23,25,53,80,110, 111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080, 13335]