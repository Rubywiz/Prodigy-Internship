from scapy.all import sniff, IP, TCP, UDP # type: ignore

# Callback function to process captured packets
def process_packet(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto

        # Check for TCP or UDP layer
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            src_port = tcp_layer.sport
            dst_port = tcp_layer.dport
            protocol_name = "TCP"
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            src_port = udp_layer.sport
            dst_port = udp_layer.dport
            protocol_name = "UDP"
        else:
            src_port = dst_port = None
            protocol_name = "Other"

        # Display captured packet information
        print(f"Packet captured: {protocol_name}")
        print(f"Source IP: {src_ip}:{src_port}")
        print(f"Destination IP: {dst_ip}:{dst_port}")
        print(f"Protocol: {protocol}")
        print("Payload:")
        print(packet[IP].payload)
        print("-" * 50)

# Start sniffing packets
print("Starting packet sniffing...")
sniff(prn=process_packet, store=False)
