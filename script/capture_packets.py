from scapy.all import sniff, wrpcap, PcapWriter

import threading
import time
import sys

import spotify_app_control
import spotify_web_control


# Define a callback function to process each packet
def process_packet(packet):
    # Print unformatted timestamp for each packet
    print(f"Timestamp: {packet.time}")

# Start sniffing packets. Process each packet with the `process_packet` function.
def start_sniffing(file_name, timeout):
    print("Starting packet sniffing...")
    packets = sniff(iface="en0", prn=lambda x: process_packet(x), timeout=timeout)
    wrpcap(file_name, packets)


if __name__ == "__main__":    
    # Create a threads for Spotify action and packet sniffing
    if sys.argv[1] == 'app':
        spotify_thread = threading.Thread(target=spotify_app_control.spotify_action)
        file_name = "../data/spotify_app_control.pcap"
    elif sys.argv[1] == 'web':
        spotify_thread = threading.Thread(target=spotify_web_control.spotify_action)
        file_name = "../data/spotify_web_control.pcap"
    else:
        print("Wrong argument. Put app or web for packet sniffing.")
    
    sniff_thread = threading.Thread(target=start_sniffing, args=(file_name, 400))
        
    # Start the sniffing thread
    sniff_thread.start()
    spotify_thread.start()
    # time.sleep(2)
    
    # Wait for both threads to finish
    sniff_thread.join()
    spotify_thread.join()
