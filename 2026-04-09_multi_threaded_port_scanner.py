import socket
import threading
from queue import Queue

# Configuration
target = "127.0.0.1"
print_lock = threading.Lock()
queue = Queue()
open_ports = []

def port_scan(port):
    """Attempts to connect to a specific port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # Timeout for each attempt
    try:
        con = s.connect_ex((target, port))
        with print_lock:
            if con == 0:
                print(f"Port {port} is OPEN")
                open_ports.append(port)
        s.close()
    except:
        pass

def threader():
    """Pulls port numbers from the queue and scans them."""
    while True:
        # Get a port number from the queue
        worker = queue.get()
        port_scan(worker)
        # Signal that the job is done
        queue.task_done()

# 1. Create the threads (workers)
# Using 100 threads for high speed
for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True # Dies when the main thread dies
    t.start()

# 2. Fill the queue with port numbers (e.g., 1 to 1024)
for port in range(1, 1025):
    queue.put(port)

# 3. Wait for all threads to finish
queue.join()

print(f"\nScan complete. Open ports: {open_ports}")