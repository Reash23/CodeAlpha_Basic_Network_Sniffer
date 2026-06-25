import socket
import struct
from datetime import datetime

packet_count = 0

# Create raw socket
conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

host = socket.gethostbyname(socket.gethostname())
conn.bind((host, 0))

conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print("=" * 65)
print("         CodeAlpha - Basic Network Sniffer")
print("=" * 65)

log = open("packets.txt", "w", encoding="utf-8")

try:

    while True:

        raw_data, addr = conn.recvfrom(65535)

        packet_count += 1

        ip_header = raw_data[:20]

        iph = struct.unpack("!BBHHHBBH4s4s", ip_header)

        version = iph[0] >> 4
        header_length = (iph[0] & 15) * 4
        ttl = iph[5]
        protocol = iph[6]

        src = socket.inet_ntoa(iph[8])
        dst = socket.inet_ntoa(iph[9])

        protocols = {
            1: "ICMP",
            6: "TCP",
            17: "UDP"
        }

        protocol_name = protocols.get(protocol, str(protocol))

        time = datetime.now().strftime("%H:%M:%S")

        print("=" * 65)
        print(f"Packet #{packet_count}")
        print(f"Time            : {time}")
        print(f"Source IP       : {src}")
        print(f"Destination IP  : {dst}")
        print(f"Protocol        : {protocol_name}")
        print(f"TTL             : {ttl}")
        print(f"Packet Size     : {len(raw_data)} Bytes")

        log.write(f"""
Packet #{packet_count}
Time: {time}
Source IP: {src}
Destination IP: {dst}
Protocol: {protocol_name}
TTL: {ttl}
Packet Size: {len(raw_data)}
----------------------------------------------------
""")

except KeyboardInterrupt:

    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

    log.close()

    print("\nSniffer Stopped Successfully.")