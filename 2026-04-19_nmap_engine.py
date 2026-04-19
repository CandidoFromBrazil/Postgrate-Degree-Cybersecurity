import nmap # Make sure to install the nmap library using pip: pip install python-nmap

nm = nmap.PortScanner()
# Performs a syn-scan (-sS) on ports 22 to 80
nm.scan('127.0.0.1', '22-80', arguments='-sS')

for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    for proto in nm[host].all_protocols():
        ports = nm[host][proto].keys()
        for port in ports:
            print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")