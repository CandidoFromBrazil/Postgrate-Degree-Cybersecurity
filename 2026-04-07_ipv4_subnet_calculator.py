import ipaddress

def calculate_subnet(ip_with_mask):
    try:
        # Create an IPv4Network object
        # strict=False allows you to pass a host IP (e.g., 192.168.1.50/24) 
        # instead of just the network address
        network = ipaddress.IPv4Network(ip_with_mask, strict=False)

        print(f"Network Details for: {ip_with_mask}")
        print("-" * 30)
        print(f"Network Address:   {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask:       {network.netmask}")
        print(f"Wildcard Mask:     {network.hostmask}")
        print(f"Total Hosts:       {network.num_addresses}")
        print(f"Usable Hosts:      {network.num_addresses - 2 if network.prefixlen < 31 else 0}")
        
        # Get the first and last usable IP
        if network.prefixlen < 31:
            hosts = list(network.hosts())
            print(f"Host Range:        {hosts[0]} - {hosts[-1]}")
        else:
            print("Host Range:        N/A (Point-to-Point link)")

    except ValueError as e:
        print(f"Error: {e}")

# Example usage
calculate_subnet("192.168.10.50/26")