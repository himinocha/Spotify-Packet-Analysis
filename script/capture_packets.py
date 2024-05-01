from scapy.all import sniff, wrpcap, PcapWriter
from scapy.all import TCP
from scapy.layers.http import HTTPRequest

import threading
import time
import sys

import spotify_app_control
import spotify_web_control

from selenium import webdriver

def handle_packet(packet):
    print(f"Timestamp: {packet.time}")
    if packet.haslayer(HTTPRequest):
        print("HTTP Request:", packet[HTTPRequest].Method, packet[HTTPRequest].Host, packet[HTTPRequest].Path)

# Define a callback function to process each packet
def process_packet(packet):
    # Print unformatted timestamp for each packet
    print(f"Timestamp: {packet.time}")

# Start sniffing packets. Process each packet with the `process_packet` function.
def start_sniffing(file_name, timeout):
    print("Starting packet sniffing...")
    # en8 for ethernet, en0 for wifi
    packets = sniff(iface="en8", prn=lambda x: process_packet(x), timeout=timeout)
    # packets = sniff(iface="en0", filter="tcp port 80 or tcp port 8080", prn=lambda x: handle_packet(x), timeout=timeout)
    # packets = sniff(
    #     lfilter= lambda pkt:TCP in pkt and (pkt[TCP].dport==80 or pkt[TCP].sport==80),
    #     prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"),
    #     timeout=timeout)
    wrpcap(file_name, packets)


if __name__ == "__main__":
    # Create a threads for Spotify action and packet sniffing
    if sys.argv[1] == 'app':
        spotify_thread = threading.Thread(target=spotify_app_control.spotify_action)
        file_name = "../data/spotify_app_control_exp_3.pcap"
    elif sys.argv[1] == 'web':
        spotify_thread = threading.Thread(target=spotify_web_control.spotify_action)
        file_name = "../data/spotify_web_control_en8.pcap"
    elif sys.argv[1] == 'selenium':
        driver = webdriver.Safari()
        driver.get('http://www.open.spotify.com')
    else:
        print("Wrong argument. Put app or web for packet sniffing.")

    file_name = "../data/spotify_web_control_en8.pcap"
    sniff_thread = threading.Thread(target=start_sniffing, args=(file_name, 400))

    # Start the sniffing thread
    sniff_thread.start()
    spotify_thread.start()
    # time.sleep(2)
    
    # Wait for both threads to finish
    if sys.argv[1] == 'selenium':
        driver.quit()
    
    # join threads
    sniff_thread.join()
    spotify_thread.join()
