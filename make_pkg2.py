from scapy.all import *

# Define the message
message = "This is a test message"

# Define the destination IP address and port
dst_ip = "127.0.0.1"  # Replace with the actual IP address
dst_port = 5000  # Replace with the desired port

# Create the packet
packet = IP(dst=dst_ip) / UDP(dport=dst_port) / message

# Send the packet
send(packet)

print(f"Sent message: {message} to {dst_ip}:{dst_port}")