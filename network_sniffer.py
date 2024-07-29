from scapy.all import sniff # type: ignore

def packet_callback(packet):
    print(packet.show())

def main():
    print("Starting network sniffer...")
    sniff(filter="tcp", prn=packet_callback, store=0)


if __name__ == "__main__":
    main()
     