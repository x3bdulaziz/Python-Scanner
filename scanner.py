## made by x3bdulaziz
import os
import socket
import sys
import time
import random
import threading
import concurrent.futures

#1. check user inputs
if len(sys.argv) < 2:                                           
    print("Usage: python3 scanner.py <target_ip_or_domain>")     
    sys.exit(1)                                                  
target = sys.argv[1] # set the target host


#2. Dictionary to map port numbers to service names.
COMMON_SERVICES = {                                                  #
    21: "FTP",                                                       #
    22: "SSH",                                                       #
    23: "Telnet",                                                    #
    25: "SMTP",                                                      #
    53: "DNS",                                                       #
    80: "HTTP",                                                      # 
    135: "MSRPC (Windows)",                                          #
    139: "NetBIOS (Windows)",                                        #
    443: "HTTPS",                                                    #
    445: "SMB (Windows Share)",                                      #
    902: "VMware Server / vCenter",                                  #
    912: "VMware VirtualCenter",                                     #
    3389: "RDP (Remote Desktop)",                                    #
    5040: "Windows CDP Service"                                      #
}                                                                    #
#3. Function for grab the service version (banner).
def get_banner(s):
    try:
        s.settimeout(1.0)
        banner = s.recv(1024)
        if banner: 
            return banner.decode('utf-8', errors='ignore').strip()
    except socket.timeout:
        try:
            s.sendall(b"GET / HTTP/1.1\r\n\r\n")
            banner = s.recv(1024)
            return banner.decode('utf-8', errors='ignore').strip()
        except:
            pass
    except:
        pass
    return "No Banner Response"                                         

#4. Main scanner function for a single port.
def scanner(target,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        result = s.connect_ex((target,port))
        if result == 0:
            banner_info = get_banner(s)
            # Handile slient Windows ports formationg.
            service_nm = COMMON_SERVICES.get(port, "Unknown")
            if service_nm == "SMB (Windows Share)" and banner_info == "No Banner Response":
                clean_banner = "Microsoft-DS (Windows 10/11 or Server SMB)"
            elif service_nm == "MSRPC (Windows)" and banner_info == "No Banner Response":
                clean_banner = "Microsoft RPC Service"
            elif "NetBIOS" in service_nm:
                clean_banner = "NetBIOS Session Service"
            else:
                clean_banner = banner_info.replace('\r', ' ').replace('\n', ' ')[:60]
            
            print(f"[+] Port {port:<5} | Service: {service_nm:<25} | Banner: {clean_banner}")            

        
        s.close()
    except Exception as e:
        pass
    finally: s.close()
#5. multi-threading engine to run the scan.
def run():
    print(f"Starting scan on host: {target}")
    print("---------------------------------------------------------")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for ports in range(1,1000):
            executor.submit(scanner,target,ports)
           # time.sleep(random.randint(1,5))
           # if enable it will make the scan slow!


if __name__ == "__main__":
    try:run()
    except KeyboardInterrupt:os._exit(0)

#date: 6/11/2026
## End

