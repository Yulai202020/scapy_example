from scapy.all import IP, UDP, send

# Define the packet
message = "Hello, world!"
packet = IP(src="192.168.100.35", dst="192.168.100.37")/UDP(sport=3, dport=1234)/message

# Send the packet
send(packet)