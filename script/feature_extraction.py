from scapy.all import rdpcap, DNSQR
import pandas as pd
import sys

packets = rdpcap(f'../data/{sys.argv[1]}.pcap')

packet_lst = []

for packet in packets:
    src_ip, dst_ip, src_port, dst_port, length, protocol, payload_size, query_name, spotify_or_not = (None,)*9

    # check for IP
    if 'IP' in packet:
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        length = packet['IP'].len
        protocol = packet['IP'].proto
    elif 'IPv6' in packet:
        src_ip = packet['IPv6'].src
        dst_ip = packet['IPv6'].dst
        length = packet['IPv6'].plen
        protocol = packet['IPv6'].nh

    # check for TCP or UDP
    if 'TCP' in packet:
        src_port = packet['TCP'].sport
        dst_port = packet['TCP'].dport
        payload_size = len(packet['TCP'].payload)
    elif 'UDP' in packet:
        src_port = packet['UDP'].sport
        dst_port = packet['UDP'].dport
        payload_size = len(packet['UDP'].payload)
    
    # extract DNS query name
    if packet.haslayer(DNSQR):
        query_name = packet[DNSQR].qname.decode('utf-8')
        if 'spotify' in query_name:
            spotify_or_not = 1
        else:
            spotify_or_not = 0
    else:
        spotify_or_not = 0
    
    packet_data = {
        'time': packet.time,
        'protocol': protocol,
        'src_ip': src_ip,
        'dst_ip': dst_ip,
        'src_port': src_port,
        'dst_port': dst_port,
        'length': length,
        'payload_size': payload_size,
        'query_name': query_name,
        'spotify_or_not': spotify_or_not
    }
    
    packet_lst.append(packet_data)



df = pd.DataFrame(packet_lst)
df['time'] = df['time'].astype(float)
df['interarrival_time'] = df['time'].diff()

# Calculate inter-arrival time per destination IP
df_sorted = df.sort_values(by=['dst_ip', 'time'])
# df_sorted['time'] = pd.to_datetime(df_sorted['time'], unit='s')
df_sorted['dst_interarrival_time'] = df_sorted.groupby('dst_ip')['time'].diff()

# save into csv
df_sorted.sort_values(by=['time']).to_csv(f'../data/{sys.argv[1]}_sorted.csv')
df_sorted.to_csv(f'../data/{sys.argv[1]}.csv')