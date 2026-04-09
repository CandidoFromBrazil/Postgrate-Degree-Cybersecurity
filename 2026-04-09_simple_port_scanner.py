import socket

target = "127.0.0.1" # Scanning your own machine (loopback address)

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Reduced timeout for faster scanning
    if s.connect_ex((target, port)) == 0:
        print(f"Port {port} is OPEN")
    s.close()

for p in range(1, 1025): # Scan common ports
    port_scan(p)
    print(f"Scanned port {p}")