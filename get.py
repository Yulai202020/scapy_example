from scapy.all import * 
count = 1
filter_ = "" # its filter for packets
# Capture STP frame
pkt = sniff(filter = filter_, count = count)

for i in range(count):
    # view capture
    print(pkt[i])

    # view more info
    print(pkt[i].show())

    # view 802.3 Ethernet
    print(pkt[i][0].show())

    # view logical-link control
    pkt[i][1].show()

    # view STP
    pkt[i][2].show()