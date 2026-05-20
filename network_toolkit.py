# ============================================
# Educational Network Analysis Toolkit
# Features:
# - Basic Port Scanner
# - Packet Sniffer
# ============================================

import socket
from scapy.all import sniff

# ============================================
# PORT SCANNER
# ============================================

def port_scanner(target, start_port, end_port):
    print(f"\n[+] Scanning {target}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

        sock.close()

    print("\n[+] Scan Complete")


# ============================================
# PACKET SNIFFER
# ============================================

def packet_callback(packet):
    print(packet.summary())


def start_sniffer(interface=None, count=20):
    print("\n[+] Starting Packet Sniffer...\n")
    sniff(iface=interface, prn=packet_callback, count=count)


# ============================================
# MAIN MENU
# ============================================

def main():
    while True:
        print("""
================================
 Educational Network Toolkit
================================
1. Port Scanner
2. Packet Sniffer
3. Exit
================================
""")

        choice = input("Select Option: ")

        if choice == "1":
            target = input("Enter Target IP/Host: ")
            start_port = int(input("Start Port: "))
            end_port = int(input("End Port: "))

            port_scanner(target, start_port, end_port)

        elif choice == "2":
            interface = input("Enter Interface (leave blank for default): ")

            if interface.strip() == "":
                interface = None

            packet_count = int(input("How many packets to capture: "))

            start_sniffer(interface, packet_count)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid Option")


if __name__ == "__main__":
    main()
